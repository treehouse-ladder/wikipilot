---
name: lint-wiki
description: |
  Run `wikipilot lint wiki/` and surface failures as structured JSON the
  caller can act on. Exits non-zero when any error-severity rule fails.
  Used by `wiki-linter` after a merge to catch broken wikilinks, missing
  frontmatter, malformed log entries, ownership violations, etc.
allowed_tools:
  - Bash
  - Read
---

# lint-wiki

## When to use

After every wiki write — typically dispatched by the orchestrator after `wiki-merger` finishes a topic and before `gh pr create`.

## How to use

```bash
uv run wikipilot lint wiki/ \
  --branch "$CURRENT_BRANCH" \
  --changed-path file1.md \
  --changed-path file2.md
```

Pass `--branch claude/...` and the list of changed paths so the ownership-violation rule fires correctly.

## Lint rules surfaced (see CLAUDE.md "Wiki schema → Lint rules" for the table)

| Code | Severity | Action expected from `wiki-linter` |
|---|---|---|
| `frontmatter` | error | fix missing/invalid keys |
| `log-format` | error | fix the malformed `## ` heading |
| `broken-wikilink` | error | either create the missing page or remove the wikilink |
| `ownership-violation` | error | revert the change to the human-only file |
| `orphan-page` | warning | leave; either accept or file as Open question |
| `stale-page` | warning | leave; researcher will pick up next run |
| `citation-density` | warning | move uncited claim to `## Open questions` |
| `disputes-format` / `open-questions-format` | warning | reformat to match schema |

## What this skill does NOT do

- It does not auto-fix `stale-page` or `citation-density` issues — those go to `## Open questions` for the next researcher run.
- It does not modify any file outside the changed-path list given by the caller.
