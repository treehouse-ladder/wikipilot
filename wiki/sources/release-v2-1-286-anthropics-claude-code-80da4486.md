---
fetched_at: &id001 2026-10-01
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 80da4486dbf0594be89303aa5cc8eecf74f0100af785deda4fa777f6e08bfd5a
sources: []
title: Release v2.1.286 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.286
---

## Excerpts

> Added a count such as "2 of 5" to the permission prompt when several permission requests stack up.

> Sessions retry the previous model once when the Anthropic API refuses a model, preventing every-turn failures.

> Fixed claude --resume and --continue sometimes losing every turn after a batch of parallel tool calls.

> Added claude --desktop to open the Claude desktop app.

> Fixed log redaction to mask secrets even when key names include invisible characters, preventing secret leaks.

> Fixed cloud sessions with very large histories never waking up.