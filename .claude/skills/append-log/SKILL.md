---
name: append-log
description: |
  Append one well-formed entry to wiki/log.md and (optionally) write the
  per-run report at wiki/reports/YYYY-MM-DD.md. Wraps
  `wikipilot.log.append_log_entry` and `wikipilot.log.write_run_report`.
  Enforces the documented log format so every entry stays parseable with
  `grep "^## \[" wiki/log.md`.
allowed_tools:
  - Bash
  - Read
  - Edit
---

# append-log

## When to use

- After each topic finishes during a Daily Research run (one log entry per topic).
- After each Wiki Query answer is filed.
- At the end of a Weekly Health sweep.

## Log entry format (enforced)

```
## [YYYY-MM-DD] kind | subject

One-line summary.
```

Where `kind` ∈ `{daily, query, health, manual}`. The `subject` may not contain `|` (it is the field delimiter).

Examples:

```
## [2026-05-11] daily | ai-agents — 3 sources, 12 pages
## [2026-05-11] query | what is qmd? — answers/2026-05-11-what-is-qmd.md
## [2026-05-12] health | weekly sweep — 2 disputes filed
```

## Per-run report

After every routine run, write the per-run report at `wiki/reports/YYYY-MM-DD.md` (or `wiki/reports/health-YYYY-MM-DD.md` for the weekly routine). The schema is enforced by `wikipilot.log.RunReport` / `HealthReport` dataclasses; see CLAUDE.md "Per-run report" for required fields.

## What this skill does NOT do

- It does not edit historic log entries (append-only).
- It does not delete or modify any reports older than today.
