---
fetched_at: &id001 2026-08-31
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 2180229dc69461fd7a9db67934416c2b7de3fb17530e9674843fb78869753685
sources: []
title: Claude Code v2.1.251 — model-switch hooks, foreground subagent streaming, and
  prompt-cache observability
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
---

## Excerpts

> Added PreModelSwitch and PostModelSwitch hook events (block, confirm, or annotate a model switch); SessionStart resume hooks now receive session staleness and the estimated re-cache cost.

> Added live streaming of a foreground subagent's tool calls and results to Remote Control clients (background subagents, the default, still show status only).

> Added a per-session prompt-cache line to /cost (hit ratio, misses, tokens re-cached, warm/cold).