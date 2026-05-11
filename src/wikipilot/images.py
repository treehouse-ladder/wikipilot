"""Image fetching pipeline (Phase 5).

Source pages should be self-contained: when a researcher ingests a URL with
images, the images live alongside the source markdown in
``wiki/assets/<source-slug>/`` and the source page references them with
local paths. This module owns that fetch/store/rewrite step.

The HTTP layer is intentionally injected via the ``http_get`` callable so
tests can mock without touching the network. The default uses
:func:`requests.get` with streaming so we can short-circuit oversize
downloads mid-stream.

Public surface
--------------
- :func:`fetch_image` — fetch one URL into a destination directory; returns
  an :class:`ImageResult` with either a path or a skipped reason.
- :func:`download_for_source` — orchestration wrapper used by the
  ``download-source-images`` skill: parse refs in a source page, fetch each
  unique URL, rewrite refs, optionally clean orphaned assets.
- :func:`safe_filename` — deterministic, collision-resistant filename.
- :func:`parse_image_refs` / :func:`rewrite_refs` — markdown/HTML helpers
  used by the orchestrator and by tests.
"""

from __future__ import annotations

import contextlib
import hashlib
import re
import urllib.parse
from collections.abc import Callable, Iterable, Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol

DEFAULT_ALLOWED_MIMES: tuple[str, ...] = (
    "image/png",
    "image/jpeg",
    "image/gif",
    "image/webp",
    "image/svg+xml",
)
DEFAULT_MAX_BYTES: int = 5_242_880  # 5 MB
DEFAULT_TIMEOUT_SECONDS: float = 10.0
SNIFF_BYTES: int = 512

MIME_TO_EXT: dict[str, str] = {
    "image/png": "png",
    "image/jpeg": "jpg",
    "image/gif": "gif",
    "image/webp": "webp",
    "image/svg+xml": "svg",
}


SKIP_REASONS = {
    "DISALLOWED_MIME": "disallowed-mime",
    "MIME_MISMATCH": "mime-mismatch",
    "OVERSIZE": "oversize",
    "FETCH_ERROR": "fetch-error",
    "BAD_STATUS": "bad-status",
    "EMPTY_BODY": "empty-body",
    "NON_HTTP": "non-http",
}


@dataclass(frozen=True)
class ImageResult:
    """Outcome of attempting to fetch one image URL.

    ``path`` is set when the image was successfully written under
    ``wiki/assets/<source-slug>/``; ``skipped_reason`` is set when the image
    was rejected (oversized, disallowed MIME, fetch error). Exactly one of
    the two is non-``None``.
    """

    url: str
    path: Path | None
    mime: str | None
    bytes_written: int
    skipped_reason: str | None

    @property
    def ok(self) -> bool:
        return self.path is not None and self.skipped_reason is None


@dataclass(frozen=True)
class ImageRef:
    """A single ``![alt](src)`` or ``<img src="...">`` reference in markdown."""

    raw: str
    alt: str
    src: str
    start: int
    end: int


@dataclass(frozen=True)
class DownloadReport:
    """Outcome of :func:`download_for_source` over an entire source page.

    ``mapping`` is ``{remote_url: posix-relative-path}`` suitable for direct
    insertion into rewritten markdown. ``orphans_removed`` counts files
    pruned from the per-source assets dir when ``cleanup_orphans=True``.
    """

    results: tuple[ImageResult, ...]
    mapping: dict[str, str]
    orphans_removed: int

    @property
    def downloaded(self) -> int:
        return sum(1 for r in self.results if r.ok)

    @property
    def skipped(self) -> int:
        return sum(1 for r in self.results if not r.ok)


class HttpResponse(Protocol):
    """Minimal subset of ``requests.Response`` we depend on."""

    status_code: int
    headers: dict[str, str] | Any

    def iter_content(self, chunk_size: int) -> Iterator[bytes]: ...

    def close(self) -> None: ...


HttpGet = Callable[..., HttpResponse]


_MD_IMG_RE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<src>[^)\s]+)(?:\s+\"[^\"]*\")?\)")
_HTML_IMG_RE = re.compile(
    r"<img\b(?P<attrs>[^>]*?)\s*/?>",
    re.IGNORECASE,
)
_HTML_SRC_RE = re.compile(r"""src\s*=\s*['"](?P<src>[^'"]+)['"]""", re.IGNORECASE)
_HTML_ALT_RE = re.compile(r"""alt\s*=\s*['"](?P<alt>[^'"]*)['"]""", re.IGNORECASE)


def safe_filename(url: str, ext: str) -> str:
    """Deterministic, collision-resistant filename for a downloaded image.

    Format: ``<sha256_8>-<basename>.<ext>``. The SHA prefix prevents
    collisions when two URLs share the same basename; the basename keeps the
    filename recognizable in Obsidian.
    """
    sha = hashlib.sha256(url.encode("utf-8")).hexdigest()[:8]
    parsed = urllib.parse.urlsplit(url)
    last = parsed.path.rstrip("/").rsplit("/", 1)[-1]
    base = re.sub(r"[^A-Za-z0-9._-]+", "-", last).strip(".-")
    if not base:
        base = "image"
    base = re.sub(rf"\.{re.escape(ext)}$", "", base, flags=re.IGNORECASE)
    base = re.sub(r"\.[A-Za-z0-9]{1,5}$", "", base) or "image"
    return f"{sha}-{base}.{ext.lower()}"


def parse_image_refs(markdown: str) -> list[ImageRef]:
    """Return every image reference in ``markdown`` (markdown + HTML forms)."""
    refs: list[ImageRef] = []
    for match in _MD_IMG_RE.finditer(markdown):
        refs.append(
            ImageRef(
                raw=match.group(0),
                alt=match.group("alt"),
                src=match.group("src"),
                start=match.start(),
                end=match.end(),
            )
        )
    for match in _HTML_IMG_RE.finditer(markdown):
        attrs = match.group("attrs")
        src_match = _HTML_SRC_RE.search(attrs)
        if not src_match:
            continue
        alt_match = _HTML_ALT_RE.search(attrs)
        refs.append(
            ImageRef(
                raw=match.group(0),
                alt=alt_match.group("alt") if alt_match else "",
                src=src_match.group("src"),
                start=match.start(),
                end=match.end(),
            )
        )
    refs.sort(key=lambda ref: ref.start)
    return refs


def rewrite_refs(markdown: str, mapping: dict[str, str]) -> str:
    """Replace remote image URLs with local paths in ``markdown``.

    ``mapping`` is ``{remote_url: local_path}``. Markdown ``![alt](src)``
    and HTML ``<img src="...">`` are both rewritten; alt-text is preserved.
    """
    if not mapping:
        return markdown
    refs = parse_image_refs(markdown)
    if not refs:
        return markdown
    out: list[str] = []
    cursor = 0
    for ref in refs:
        out.append(markdown[cursor : ref.start])
        new_src = mapping.get(ref.src)
        if new_src is None:
            out.append(ref.raw)
        elif ref.raw.startswith("!["):
            out.append(f"![{ref.alt}]({new_src})")
        else:
            out.append(_rewrite_html_src(ref.raw, new_src))
        cursor = ref.end
    out.append(markdown[cursor:])
    return "".join(out)


def _rewrite_html_src(html: str, new_src: str) -> str:
    return _HTML_SRC_RE.sub(lambda m: f'src="{new_src}"', html, count=1)


def sniff_mime(prefix: bytes) -> str | None:
    """Best-effort first-bytes MIME sniff for the formats we accept.

    Returns ``None`` when the bytes don't match any known image signature so
    the caller can decide whether to fall back to the response header alone.
    """
    if not prefix:
        return None
    if prefix.startswith(b"\x89PNG\r\n\x1a\n"):
        return "image/png"
    if prefix.startswith(b"\xff\xd8\xff"):
        return "image/jpeg"
    if prefix.startswith(b"GIF87a") or prefix.startswith(b"GIF89a"):
        return "image/gif"
    if prefix[:4] == b"RIFF" and prefix[8:12] == b"WEBP":
        return "image/webp"
    head = prefix[:512].lstrip().lower()
    if head.startswith(b"<svg") or head.startswith(b"<?xml"):
        return "image/svg+xml"
    return None


def _normalize_mime(value: str | None) -> str | None:
    if not value:
        return None
    return value.split(";", 1)[0].strip().lower()


def _default_http_get(url: str, *, timeout: float) -> HttpResponse:
    import requests  # imported lazily so test fakes don't pay the cost

    return requests.get(url, stream=True, timeout=timeout)


def fetch_image(
    url: str,
    *,
    dest_dir: Path,
    timeout: float = DEFAULT_TIMEOUT_SECONDS,
    max_bytes: int = DEFAULT_MAX_BYTES,
    allowed_mimes: Iterable[str] = DEFAULT_ALLOWED_MIMES,
    http_get: HttpGet | None = None,
) -> ImageResult:
    """Fetch ``url`` into ``dest_dir`` with size + MIME enforcement.

    Both response ``Content-Type`` and a first-bytes magic-number sniff must
    point at an allowed MIME before the file is written. If they disagree,
    the result is skipped with reason ``mime-mismatch`` so the caller can
    log and move on without committing a misnamed asset.

    The fetch is streamed; if the server doesn't return ``Content-Length``
    we still hard-stop once the cumulative chunk count exceeds
    ``max_bytes``, leaving no partial file behind.
    """
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme not in {"http", "https"}:
        return ImageResult(
            url=url,
            path=None,
            mime=None,
            bytes_written=0,
            skipped_reason=SKIP_REASONS["NON_HTTP"],
        )

    allowed = tuple(_normalize_mime(m) or "" for m in allowed_mimes)
    getter = http_get or _default_http_get
    try:
        response = getter(url, timeout=timeout)
    except Exception:  # noqa: BLE001 — fetch errors are explicitly captured here
        return ImageResult(
            url=url,
            path=None,
            mime=None,
            bytes_written=0,
            skipped_reason=SKIP_REASONS["FETCH_ERROR"],
        )

    try:
        status = getattr(response, "status_code", 0)
        if status >= 400:
            return ImageResult(
                url=url,
                path=None,
                mime=None,
                bytes_written=0,
                skipped_reason=SKIP_REASONS["BAD_STATUS"],
            )

        headers = getattr(response, "headers", {}) or {}
        header_mime = _normalize_mime(_lookup_header(headers, "Content-Type"))
        header_length = _lookup_header(headers, "Content-Length")
        try:
            advertised_bytes = int(header_length) if header_length is not None else None
        except (TypeError, ValueError):
            advertised_bytes = None
        if advertised_bytes is not None and advertised_bytes > max_bytes:
            return ImageResult(
                url=url,
                path=None,
                mime=header_mime,
                bytes_written=0,
                skipped_reason=SKIP_REASONS["OVERSIZE"],
            )
        if header_mime is not None and header_mime not in allowed:
            return ImageResult(
                url=url,
                path=None,
                mime=header_mime,
                bytes_written=0,
                skipped_reason=SKIP_REASONS["DISALLOWED_MIME"],
            )

        chunks: list[bytes] = []
        sniffed_mime: str | None = None
        total = 0
        for chunk in response.iter_content(chunk_size=8192):
            if not chunk:
                continue
            chunks.append(chunk)
            total += len(chunk)
            if total > max_bytes:
                return ImageResult(
                    url=url,
                    path=None,
                    mime=header_mime,
                    bytes_written=0,
                    skipped_reason=SKIP_REASONS["OVERSIZE"],
                )
            if sniffed_mime is None and total >= min(SNIFF_BYTES, max_bytes):
                sniffed_mime = sniff_mime(b"".join(chunks)[:SNIFF_BYTES])
        if total == 0:
            return ImageResult(
                url=url,
                path=None,
                mime=header_mime,
                bytes_written=0,
                skipped_reason=SKIP_REASONS["EMPTY_BODY"],
            )
        if sniffed_mime is None:
            sniffed_mime = sniff_mime(b"".join(chunks)[:SNIFF_BYTES])

        chosen_mime = header_mime or sniffed_mime
        if chosen_mime is None or chosen_mime not in allowed:
            return ImageResult(
                url=url,
                path=None,
                mime=chosen_mime,
                bytes_written=0,
                skipped_reason=SKIP_REASONS["DISALLOWED_MIME"],
            )
        if (
            sniffed_mime is not None and header_mime is not None and sniffed_mime != header_mime
            # SVG over HTML/text or PNG with `image/jpeg` header is the kind
            # of mismatch we want to catch — header and bytes must agree.
        ):
            return ImageResult(
                url=url,
                path=None,
                mime=chosen_mime,
                bytes_written=0,
                skipped_reason=SKIP_REASONS["MIME_MISMATCH"],
            )

        ext = MIME_TO_EXT.get(chosen_mime)
        if ext is None:
            return ImageResult(
                url=url,
                path=None,
                mime=chosen_mime,
                bytes_written=0,
                skipped_reason=SKIP_REASONS["DISALLOWED_MIME"],
            )

        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_path = dest_dir / safe_filename(url, ext)
        body = b"".join(chunks)
        dest_path.write_bytes(body)
        return ImageResult(
            url=url,
            path=dest_path,
            mime=chosen_mime,
            bytes_written=len(body),
            skipped_reason=None,
        )
    finally:
        with contextlib.suppress(Exception):
            response.close()


def _lookup_header(headers: Any, name: str) -> str | None:
    if hasattr(headers, "get"):
        for key in (name, name.lower(), name.upper()):
            value = headers.get(key)
            if value is not None:
                return str(value)
    return None


def download_for_source(
    *,
    source_content: str,
    assets_dir: Path,
    relative_assets_path: str,
    timeout: float = DEFAULT_TIMEOUT_SECONDS,
    max_bytes: int = DEFAULT_MAX_BYTES,
    allowed_mimes: Iterable[str] = DEFAULT_ALLOWED_MIMES,
    cleanup_orphans: bool = True,
    http_get: HttpGet | None = None,
) -> tuple[str, DownloadReport]:
    """Localize every fetchable image in ``source_content``.

    Returns the rewritten content and a :class:`DownloadReport`. The caller
    is responsible for persisting both the new content and the per-source
    ``image_count`` (typically via :func:`wikipilot.sources.update_image_count`).

    ``relative_assets_path`` is the prefix used in the rewritten refs (e.g.
    ``"../assets/<source-slug>"``) — it must point at ``assets_dir`` from
    the source page's location so Obsidian and Markdown viewers resolve the
    image without a base-URL hop.
    """
    refs = parse_image_refs(source_content)
    unique_urls: list[str] = []
    seen: set[str] = set()
    for ref in refs:
        if ref.src in seen:
            continue
        if ref.src.startswith(("data:", "/", "./", "../")):
            # Already a local or inline ref; leave it alone.
            continue
        seen.add(ref.src)
        unique_urls.append(ref.src)

    results: list[ImageResult] = []
    mapping: dict[str, str] = {}
    rel_prefix = relative_assets_path.rstrip("/")
    for url in unique_urls:
        result = fetch_image(
            url,
            dest_dir=assets_dir,
            timeout=timeout,
            max_bytes=max_bytes,
            allowed_mimes=allowed_mimes,
            http_get=http_get,
        )
        results.append(result)
        if result.ok and result.path is not None:
            filename = result.path.name
            mapping[url] = f"{rel_prefix}/{filename}"

    new_content = rewrite_refs(source_content, mapping)

    orphans_removed = 0
    if cleanup_orphans and assets_dir.exists():
        keep = {Path(local).name for local in mapping.values()}
        for path in assets_dir.iterdir():
            if path.is_file() and path.name not in keep:
                path.unlink()
                orphans_removed += 1

    return new_content, DownloadReport(
        results=tuple(results),
        mapping=mapping,
        orphans_removed=orphans_removed,
    )
