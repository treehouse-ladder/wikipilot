---
fetched_at: &id001 2026-10-10
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: e75aaf1e1290080879074d3acf2d45d92837e0703187e948fe4a3908394c3ad3
sources: []
title: Release v2.1.296 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.296
---

## Excerpts

> Added CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL to run every workflow agent on one model while other subagents keep theirs.

> Updated /cost, the status line, --max-budget-usd and the SDK's cost figures to price Sonnet 5.5 cache reads at $0.10 per million tokens (was $0.20).

> Added an allow_large option to the Read tool to read text files beyond the normal size limits in one call when the whole file is needed and context has room.

> Added CLAUDE_CODE_OVERLOADED_RETRY_MAX_DELAY_MS to set a longer maximum delay for the backoff when retrying an overloaded (529) request.

> Fixed Bash permission checks auto-approving some commands that assign the BASH_ARGV0 shell variable and then use it; these now prompt for approval.

> Fixed managed-settings PreToolUse hooks that deny a tool call with "continue": false.