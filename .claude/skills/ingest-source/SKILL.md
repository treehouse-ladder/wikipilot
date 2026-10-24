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
  - Write
---

# ingest-source

## When to use

Call this skill from `topic-researcher` and `query-answerer` whenever a new URL needs to enter the wiki. Source pages are the evidence layer the citation discipline depends on; every `[[source-...]]` wikilink must resolve to a page produced by this skill.

## How to use

**Step 1 — write the excerpts to a file with the Write tool** (never through Bash). A JSON array of strings, one entry per verbatim quote:

```json
["Claude Fable 5 is priced at $10 per million input tokens and $50 per million output tokens.",
 "The weights are released under the MiniMax H3 Community License Agreement, which permits commercial use for organizations under $100M annual revenue."]
```

Save it as e.g. `/tmp/excerpts-<slug-ish>.json`.

**Step 2 — call the CLI, pointing at the file:**

```bash
uv run wikipilot ingest \
  --url "<url>" \
  --topic "<topic-id>" \
  --title "<title>" \
  --excerpts-file /tmp/excerpts-<slug-ish>.json
```

### Why the file, not `--excerpt "<quote>"`

Excerpts routinely contain `$` (prices, revenue thresholds, valuations). Inside a double-quoted bash argument, `$10` is a positional-parameter expansion: the shell turns `"priced at $10 per million"` into `"priced at 0 per million"` **before** the CLI ever sees it, and the corrupted text lands as the wiki's "verbatim" evidence. This happened to at least eight source pages in 2026 (GPT-5.6 Sol, Claude Fable 5, Opus 4.8, MiniMax H3, Inworld TTS-2 pricing all recorded as `0`). Writing the file with the Write tool keeps the text out of any shell.

`--excerpt "<quote>"` still works for quotes that contain no shell metacharacters, but `wikipilot ingest` now **refuses** any excerpt that looks like a shell ate a `$N` (`costs  per million`, `priced at 0 per million`, `under 0M annual revenue`, …) and exits non-zero with the offending snippet. Fix the excerpt and re-run; only pass `--allow-suspicious-excerpts` when the source genuinely reads that way (rare — e.g. a free tier described as "$0 per million" is written with the `$` and does not trip the guard).

The CLI calls `wikipilot.sources.ingest_source_with_images`, which writes the source page **and** runs the image-localization pipeline (`wikipilot.images.download_for_source`) before returning. Re-ingesting a known URL is a no-op (idempotent dedupe by SHA-256 of normalized URL).

## Contract

- Dedupe is by SHA-256 of the normalized URL (lowercased scheme/host, sorted query, fragment stripped, trailing slash stripped). If the URL is already in `wiki/sources/`, no new page is written and the existing slug is returned.
- The source page body must include verbatim `>` quote excerpts for every claim the topic-researcher cites from this URL — these are what the citation discipline rule reads.
- `freshness_window_days` defaults to 365 on source pages (they don't go stale the way synthesis pages do).
- After the source page is written, `download-source-images` runs to localize images, then `update-index` adds the page to `wiki/index.md`.

## What this skill does NOT do

- It does not synthesize concept/entity pages. The topic-researcher is responsible for producing a structured proposal that drives concept/entity edits via `wiki-merger`.
- It does not modify human-only files (`topics.yaml`, `CLAUDE.md`, `wiki/topics/<id>/purpose.md`).
