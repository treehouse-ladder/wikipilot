"""Source registry: append source pages, dedupe by SHA-256 of normalized URL.

The ``ingest_source`` flow that the topic-researcher invokes goes through
``write_source`` here. Idempotency is by SHA-256 of the *normalized* URL — if
the same URL (modulo casing/fragment/query-order) is ingested twice, the
second call returns the existing page rather than creating a duplicate.

Source page schema (mirrors ``CLAUDE.md``):

```yaml
---
title: "Source title"
kind: source
url: "https://..."
sha256: "<hex of normalized url>"
fetched_at: 2026-05-11
topic: "<topic-id>"   # the topic this source was ingested for
image_count: 0
sources: []           # always empty for source pages; kept for schema parity
last_updated: 2026-05-11
last_verified: 2026-05-11
freshness_window_days: 365
---
```

Body: human-readable summary plus verbatim ``>`` excerpts to preserve evidence.
"""

from __future__ import annotations

import hashlib
import urllib.parse
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from wikipilot.wiki import Page, Vault, slugify

SOURCE_FRESHNESS_WINDOW_DAYS = 365
"""Source pages don't go stale in the same way synthesis pages do; we still
record a window so the lint can flag truly ancient pages, but we set it
generously so daily lint runs don't churn on every source."""


@dataclass(frozen=True)
class SourceRecord:
    """The result of writing or finding a source page."""

    page: Page
    slug: str
    sha256: str
    created: bool


def normalize_url(url: str) -> str:
    """Return a deterministic canonical form of ``url``.

    Lowercases scheme/host, strips fragments and trailing slashes, and sorts
    query parameters. Two URLs with the same normalized form are treated as
    the same source.
    """
    parsed = urllib.parse.urlsplit(url.strip())
    scheme = parsed.scheme.lower() or "https"
    netloc = parsed.netloc.lower()
    path = parsed.path.rstrip("/")
    if not path:
        path = "/"
    query_pairs = sorted(urllib.parse.parse_qsl(parsed.query, keep_blank_values=True))
    query = urllib.parse.urlencode(query_pairs, doseq=True)
    return urllib.parse.urlunsplit((scheme, netloc, path, query, ""))


def url_sha256(url: str) -> str:
    return hashlib.sha256(normalize_url(url).encode("utf-8")).hexdigest()


def source_slug(url: str, *, title: str | None = None) -> str:
    """Return a stable, human-readable slug for ``url``.

    Combines a short SHA prefix with a slugified title (or last URL path
    segment) so filenames are both unique and recognizable.
    """
    sha_prefix = url_sha256(url)[:8]
    base = slugify(title) if title else ""
    if not base:
        parsed = urllib.parse.urlsplit(normalize_url(url))
        last_segment = parsed.path.rstrip("/").rsplit("/", 1)[-1]
        base = slugify(last_segment) or slugify(parsed.netloc) or "source"
    return f"{base}-{sha_prefix}"


def find_source(vault: Vault, url: str) -> Page | None:
    """Return the existing source page for ``url`` (by SHA), or ``None``."""
    sha = url_sha256(url)
    for path in sorted((vault.dir_for("sources")).glob("*.md")):
        page = Page.read(path)
        if page.metadata.get("sha256") == sha:
            return page
    return None


def write_source(
    vault: Vault,
    *,
    url: str,
    title: str,
    topic: str,
    body: str,
    today: date | None = None,
    image_count: int = 0,
    excerpts: list[str] | None = None,
) -> SourceRecord:
    """Write a new source page or return the existing one if the URL already exists.

    The body is composed of three parts in order:
    1. A short human-readable summary (``body`` argument).
    2. ``## Excerpts`` listing each ``excerpts`` item as a ``>`` quote block
       — this preserves verbatim evidence so the citation discipline can be
       enforced downstream.
    3. The source page is otherwise minimal; the topic-researcher's proposal
       is what produces the synthesis on concept/entity pages, not here.
    """
    today = today or date.today()
    sha = url_sha256(url)
    existing = find_source(vault, url)
    if existing is not None:
        slug = existing.path.stem
        return SourceRecord(page=existing, slug=slug, sha256=sha, created=False)

    slug = source_slug(url, title=title)
    metadata: dict[str, object] = {
        "title": title,
        "kind": "source",
        "url": url,
        "sha256": sha,
        "fetched_at": today,
        "topic": topic,
        "image_count": int(image_count),
        "sources": [],
        "last_updated": today,
        "last_verified": today,
        "freshness_window_days": SOURCE_FRESHNESS_WINDOW_DAYS,
    }
    sections = [body.strip()]
    if excerpts:
        sections.append("## Excerpts")
        for excerpt in excerpts:
            cleaned = excerpt.strip().replace("\n", "\n> ")
            sections.append(f"> {cleaned}")
    full_body = "\n\n".join(section for section in sections if section)
    page_path = vault.dir_for("sources") / f"{slug}.md"
    page = Page.from_dict(page_path, metadata, full_body + "\n" if full_body else "")
    page.write()
    return SourceRecord(page=page, slug=slug, sha256=sha, created=True)


def list_sources(vault: Vault) -> list[Page]:
    """Return every source page in the vault, sorted by slug."""
    paths = sorted((vault.dir_for("sources")).glob("*.md"))
    return [Page.read(p) for p in paths if p.name != ".gitkeep"]


def update_image_count(page: Page, count: int) -> None:
    """Bump the ``image_count`` field on a source page and persist."""
    page.metadata["image_count"] = int(count)
    page.write()


def assets_dir(vault: Vault, source_slug: str) -> Path:
    """Per-source asset directory (created lazily by the image pipeline)."""
    return vault.assets_for(source_slug)
