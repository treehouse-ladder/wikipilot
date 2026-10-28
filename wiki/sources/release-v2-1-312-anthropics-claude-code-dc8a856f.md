---
fetched_at: &id001 2026-10-28
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: dc8a856f8c6596f8198bd36adb3cc0afcc9ecb003c0bba0186f0856d0e28448b
sources: []
title: Release v2.1.312 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.312
---

## Excerpts

> Changed prompt and agent hooks to run at most 24 at a time per session, sub-agents included, plus at most 12 that have waited longer than their event's timeout; a `timeout` under 1 second now counts as 1 second

> Fixed Claude overwriting a very large CLAUDE.md, rules file or @-included file in a subdirectory after seeing only its start; Write now asks Claude to read it all or edit in place

> Fixed per-directory and `paths:` skills not being found after a Bash `cd` deeper into a git repository

> Changed Bedrock, Vertex, Foundry and Mantle to use the shorter system prompt for model names Claude Code doesn't recognize, such as custom deployment names and inference profile ARNs, even when they front Sonnet or Haiku; set `CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT=0` to keep the full prompt

> Changed a subagent's `autoCompactWindow` to lower the window set by `CLAUDE_CODE_AUTO_COMPACT_WINDOW`, where it had no effect before; it still never raises that window