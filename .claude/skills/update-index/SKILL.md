---
name: update-index
description: |
  Idempotently update wiki/index.md with new pages. Adds [[wikilinks]] to
  the appropriate section (Topics, Concepts, Entities, Sources, Answers,
  Reports) without touching existing entries; existing links are left
  verbatim and "_(none yet)_" placeholders are removed when the section
  gains its first real entry.
allowed_tools:
  - Read
  - Edit
---

# update-index

## When to use

Call after every page write (sources, concepts, entities, topics, answers, reports) to keep `wiki/index.md` synchronized.

## Contract

- Append-only: never deletes existing index entries.
- Idempotent: re-running with the same set of pages is a no-op.
- Dispatches each new entry to the correct section by `kind`:
  - `topic` → `## Topics`
  - `concept` → `## Concepts`
  - `entity` → `## Entities`
  - `source` → `## Sources`
  - `answer` → `## Answers`
  - `report` → `## Reports`

## What this skill does NOT do

- It does not modify any other markdown file.
- It does not validate the wiki schema (that's `lint-wiki`).
