---
fetched_at: &id001 2026-05-29
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 8a5bbbe86d573446734d8f4c25dc81a68763bd7c2a1318c86a5d774123b5c475
sources: []
title: 'Claude Opus 4.8: a modest but tangible improvement'
topic: agentic-coding
url: https://simonwillison.net/2026/May/28/claude-opus-4-8/
---

## Excerpts

> Notes on Claude Opus 4.8, which Anthropic call a modest but tangible improvement over Opus 4.7. Both the reliable knowledge cutoff and the training data cutoff are January 2026, the same as for 4.7.

> Claude Opus 4.8 accepts role: system messages immediately after a user turn in the messages array, which lets you append updated instructions later in a long-running conversation without restating the full system prompt, preserving prompt cache hits and reducing input cost on agentic loops.