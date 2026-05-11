---
name: qmd-search
description: |
  Thin wrapper around the qmd MCP `search` tool. Searches the local wiki
  via hybrid BM25 + vector retrieval, then dedupes results against the
  last N entries in wiki/log.md so the topic-researcher doesn't re-propose
  pages whose source was added today.
allowed_tools:
  - Bash
  - Read
---

# qmd-search

## When to use

- `topic-researcher` calls this BEFORE WebSearch, on every research run, to discover what the wiki already says about a candidate concept.
- `query-answerer` calls this FIRST before falling back to WebSearch — if the wiki has the answer, no external call is needed.
- `wiki-disputes-scanner` uses this to load the candidate page sets selected by `disputes_seed.py`.

## Contract

- Input: a natural-language query string. Optional filter: `kind` (one of `topic | concept | entity | source | answer`).
- Output: ranked list of `{path, score, snippet}`. The skill dedupes against the last N (default 50) ingest entries in `wiki/log.md` so freshly-ingested sources don't keep showing up.

## Setup

The qmd MCP connector must be registered with the routine's connectors list. See `docs/qmd-setup.md` (Phase 4) for installation, and `docs/routines-setup.md` for the per-routine connector configuration.

## What this skill does NOT do

- It does not search the live web. WebSearch is a separate tool, used as a fallback for `query-answerer` and as the primary discovery mechanism for `topic-researcher`.
- It does not write to the index. `wikipilot index-wiki` is what refreshes qmd's index after writes.
