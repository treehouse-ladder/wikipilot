---
name: download-source-images
description: |
  For each <img src> in a fetched source page, download via
  `wikipilot.images`, store under wiki/assets/<source-slug>/, and rewrite
  the source page's image refs to local paths. Preserves alt-text. Skips
  oversize images (>5 MB by default) and disallowed MIME types. All
  thresholds configurable via wikipilot.toml [images].
allowed_tools:
  - Bash
  - Read
  - Edit
---

# download-source-images

## When to use

Called by `ingest-source` immediately after the source page is written and before commit. Source pages should be self-contained — once committed they reference local image paths only, so the wiki survives the original URLs disappearing.

In practice the orchestration lives in `wikipilot.sources.ingest_source_with_images`, which is invoked by the `wikipilot ingest` CLI. This skill is the documented contract — agents do not call into Python directly; they shell out to `wikipilot ingest` and trust this skill's invariants.

## Contract

- Output filenames follow `<sha256_8>-<basename>.<ext>` to avoid collisions on shared basenames.
- Allowed MIMEs (default): `image/png`, `image/jpeg`, `image/gif`, `image/webp`, `image/svg+xml`.
- Max bytes (default): `5_242_880` (5 MB).
- Both response `Content-Type` header and a first-bytes sniff must agree before the image is accepted.
- Alt-text is preserved when rewriting `![alt](src)` and `<img alt="..." src="...">` references.
- Orphaned assets (under `wiki/assets/<slug>/` for a source that no longer exists) are cleaned up if `[images] cleanup_orphans = true`.

## How to disable

In `wikipilot.toml`:

```toml
[images]
enabled = false
```

When disabled, `ingest-source` skips this skill entirely and source pages keep their original remote image URLs.

## What this skill does NOT do

- It does not download non-image assets (PDFs, videos).
- It does not re-encode or resize images.
- It does not block ingest on a single image failure — failures are logged and the source page is still committed with the failed image references intact.
