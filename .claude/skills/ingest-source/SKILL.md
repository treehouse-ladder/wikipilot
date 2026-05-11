---
name: ingest-source
description: |
  Fetch a URL and write a source page under wiki/sources/<slug>.md with the
  documented frontmatter (url, sha256, fetched_at, topic, image_count) and
  verbatim > quote excerpts. Idempotent: re-ingesting the same URL is a
  no-op (dedupe by SHA-256 of normalized URL). After writing the source
  page, downloads any in-page images via download-source-images and updates
  wiki/index.md via update-index.
allowed_tools:
  - Bash
  - Read
  - Edit
---

# ingest-source

## When to use

Call this skill from `topic-researcher` and `query-answerer` whenever a new URL needs to enter the wiki. Source pages are the evidence layer the citation discipline depends on; every `[[source-...]]` wikilink must resolve to a page produced by this skill.

## How to use

```bash
uv run wikipilot ingest --url "<url>" --topic "<topic-id>" --title "<title>"
```

Phase 5 wires the underlying `wikipilot ingest` subcommand. Until then, the dry-run path in `wikipilot.dryrun.apply_proposal` exercises the same `wikipilot.sources.write_source` helper this skill calls at runtime.

## Contract

- Dedupe is by SHA-256 of the normalized URL (lowercased scheme/host, sorted query, fragment stripped, trailing slash stripped). If the URL is already in `wiki/sources/`, no new page is written and the existing slug is returned.
- The source page body must include verbatim `>` quote excerpts for every claim the topic-researcher cites from this URL — these are what the citation discipline rule reads.
- `freshness_window_days` defaults to 365 on source pages (they don't go stale the way synthesis pages do).
- After the source page is written, `download-source-images` runs to localize images, then `update-index` adds the page to `wiki/index.md`.

## What this skill does NOT do

- It does not synthesize concept/entity pages. The topic-researcher is responsible for producing a structured proposal that drives concept/entity edits via `wiki-merger`.
- It does not modify human-only files (`topics.yaml`, `CLAUDE.md`, `wiki/topics/<id>/purpose.md`).
