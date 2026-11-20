---
fetched_at: &id001 2026-11-20
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: f3d370a5121afbf2b74a441ed17e14480982c4fee8de87420c27e4050b730e64
sources: []
title: Release v2.1.329 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.329
---

## Excerpts

> Fixed a runaway loop in Code Mode filling the machine's memory; it is now stopped at a limit

> Changed Code Mode so a PreToolUse hook that errors no longer refuses a script's tool call, as outside Code Mode; set "onFailure": "block" on a command, HTTP or MCP tool hook that must refuse

> Added a trust dialog warning that says where a folder's hooks are declared

> Added this session's scheduled tasks, /loop wakeups, the goal and this conversation's forks to /tasks; x stops one after asking

> In new signed-in sessions, most scheduled tasks saved by earlier versions need scheduling again, though --resume of their own session still runs them

> Fixed ~/.claude.json sometimes being reset to defaults when a network stall or file lock made it unreadable and cleared during a save

> Fixed /code-review <pr number> sometimes reviewing the checked-out branch instead of the pull request without saying so