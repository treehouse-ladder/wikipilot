---
name: disputes-scan
description: |
  Driver for scripts/disputes_seed.py. Selects candidate page sets for the
  Weekly Health routine's LLM-judge sweep, using overlap heuristics
  (shared concepts/backlinks, recently-touched, oldest-last_verified).
  Outputs a structured JSON list of `{trigger, pages[]}` candidate sets the
  wiki-disputes-scanner agent reads.
allowed_tools:
  - Bash
  - Read
---

# disputes-scan

## When to use

Once per Weekly Health run, before fanning out the disputes-scanner subagents in parallel.

## Contract

- Input: the wiki vault root.
- Output: JSON of the form
  ```json
  {
    "candidate_sets": [
      {"trigger": "source_<slug>", "pages": ["path/a.md", "path/b.md"]},
      {"trigger": "stale_sweep",   "pages": ["path/c.md", "path/d.md"]}
    ]
  }
  ```
- Per the plan:
  - For each new source ingested in the last 7 days, find concepts it touches and pick the top-K (default K=10) pages by overlap.
  - Also pick the top-K oldest-`last_verified` pages for general staleness review.

## What this skill does NOT do

- It does not file dispute proposals — that's the disputes-scanner agent.
- It does not modify any wiki page.
- It does not call the qmd MCP. The candidate selection is purely metadata-driven.
