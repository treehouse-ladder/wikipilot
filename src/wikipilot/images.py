"""Image fetching pipeline (full implementation lands in Phase 5).

Phase 1 ships only the dataclass shapes and the safe-filename helper so
``sources.py`` and the lint checker have stable types to import. The actual
HTTP fetch + content-type sniff + asset cleanup arrive in Phase 5 alongside
the ``download-source-images`` skill that drives this module.
"""

from __future__ import annotations

import hashlib
import re
import urllib.parse
from dataclasses import dataclass

DEFAULT_ALLOWED_MIMES: tuple[str, ...] = (
    "image/png",
    "image/jpeg",
    "image/gif",
    "image/webp",
    "image/svg+xml",
)
DEFAULT_MAX_BYTES: int = 5_242_880  # 5 MB

MIME_TO_EXT: dict[str, str] = {
    "image/png": "png",
    "image/jpeg": "jpg",
    "image/gif": "gif",
    "image/webp": "webp",
    "image/svg+xml": "svg",
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
    path: str | None
    mime: str | None
    bytes_written: int
    skipped_reason: str | None


@dataclass(frozen=True)
class ImageRef:
    """A single ``![alt](src)`` or ``<img src="...">`` reference in markdown."""

    raw: str
    alt: str
    src: str
    start: int
    end: int


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
