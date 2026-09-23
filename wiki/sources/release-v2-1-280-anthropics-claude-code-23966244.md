---
fetched_at: &id001 2026-09-23
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 23966244d47d35ba5ef9a285316c86388a48696eb1f3e480ee0084e78425f2c7
sources: []
title: Release v2.1.280 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.280
---

## Excerpts

> Added Claude Opus 5.5 (claude-opus-5-5), now the default Opus model — 1M context, $4/$20 per Mtok with $0.20/Mtok cache reads

> Added CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH to change the 2,048-character cap on MCP tool descriptions and server instructions for every MCP server in the session.

> Fixed auto mode retrying an action over and over when a safety check declined to review it; the action is now denied once.

> Fixed writes through a symlinked path being judged by their in-tree spelling; the prompt names where the write lands, and acceptEdits, allow rules and auto mode no longer approve one landing outside.