---
name: query-back-fill
description: |
  Given a freshly-written answer page, find the K most-related concept and
  entity pages (by qmd similarity + frontmatter sources overlap) and add a
  [[answer-slug]] reference to each under their ## See also section.
  Append-only and idempotent so answers compound without polluting their
  hosts.
allowed_tools:
  - Bash
  - Read
  - Edit
---

# query-back-fill

## When to use

After `query-answerer` writes a new `wiki/answers/YYYY-MM-DD-<slug>.md`. This is what makes the Wiki Query routine's answers *compound* with the rest of the wiki — every answer becomes discoverable from any of its related concept/entity pages.

## Contract

- Input: path to the newly-written answer page.
- For the top K (default: 5) most-related concept/entity pages:
  - Read the page.
  - Append `- [[answer-slug]]` under `## See also`. Create the section if missing.
  - Append-only: never delete or reorder existing `## See also` entries.
  - Idempotent: if the answer's wikilink is already present, no-op.
  - Bump `last_updated` (not `last_verified`) and write back.

## How "related" is computed

1. Frontmatter overlap: pages sharing at least one `[[source-...]]` wikilink in `sources` get a strong boost.
2. Title and `## Summary` similarity via `qmd-search` over the answer's question.
3. Top K by combined score.

## What this skill does NOT do

- It does not modify the answer page itself (the answer-page is owned by the query-answerer).
- It does not bump `last_verified` on back-filled pages (the back-fill is mechanical, not a re-verification).
- It does not back-fill into source pages (those are append-only after creation).
