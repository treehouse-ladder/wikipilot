---
fetched_at: &id001 2026-09-12
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 98ebc4a5c5a6d75402823d76e2f7a104e22793c974d8ab5938fd1ca804e9d30f
sources: []
title: Release v2.1.268 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
---

## Excerpts

> Fixed WebFetch hanging indefinitely on a server that keeps the response open without finishing; a fetch now fails after 300 seconds. Set CLAUDE_CODE_WEBFETCH_DEADLINE_MS to override the deadline (0 turns it off). Added browser-tab icons for published artifacts, chosen by Claude to match each page.