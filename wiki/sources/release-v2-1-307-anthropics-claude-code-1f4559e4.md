---
fetched_at: &id001 2026-10-22
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 1f4559e41bf13b35880f00be8a25f4fd0d1307af9a0b5e4043ae53ceb5a3c975
sources: []
title: Release v2.1.307 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.307
---

## Excerpts

> Added the `claude_code.safety_event` OpenTelemetry event for each tool call a permission rule, auto mode, a safety check, a hook or the sandbox stopped, prompted or sent back

> Fixed HTTP MCP tool calls being sent twice when the connection closed mid-call; only read-only or idempotent tools are now retried

> Improved fork subagents launched together: each is now told which launch is its own, so forks are much less likely to try to start each other's work

> Improved recovery from unparseable tool calls: Claude Code now retries the call up to twice before ending the turn with an error

> Fixed `/permissions` > Recently denied not showing the denied shell command, and auto mode's local classifier ignoring an approval from there when it checks a retried command; approving a row now names the command, not its description