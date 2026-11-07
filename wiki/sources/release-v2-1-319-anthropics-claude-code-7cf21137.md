---
fetched_at: &id001 2026-11-07
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 7cf21137c37e547b10a35af8b343d6a8538c49933b210b798d3222ba7e5f4e15
sources: []
title: Release v2.1.319 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.319
---

## Excerpts

> Auto mode behind gateways: calls the server can't verify are now asked about or denied, with no fallback to the local classifier. Set CLAUDE_CODE_AUTO_MODE_SERVER=0 to keep the old behavior.

> Fixed a sandbox escape when creating a worktree, a Bash permission bypass using a crafted environment prefix, and a sed command that could skip the permission check in accept-edits and auto mode.

> Added permissions.denyInsteadOfPrompting so a tool call that would wait on a prompt is denied and the turn continues. MCP tasks can now run in the background.

> In -p mode, resuming with a pending deferred tool call no longer silently drops the call; the prompt is held back and the run exits 1.