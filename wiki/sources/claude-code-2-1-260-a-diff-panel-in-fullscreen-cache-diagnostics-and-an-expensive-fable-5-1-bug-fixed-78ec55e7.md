---
title: "Claude Code 2.1.260: a diff panel in fullscreen, cache diagnostics, and an expensive Fable 5.1 bug fixed"
kind: source
url: https://clauding.de/en/posts/claude-code-2-1-260
sha256: 78ec55e7a2f1d3c9b4e8f0a7d6c5b2e1f9a3d8c7b6e5a4f2d1c0b9e8a7f6d5c4
fetched_at: 2026-09-05
topic: agentic-coding
image_count: 0
sources: []
last_updated: 2026-09-05
last_verified: 2026-09-05
freshness_window_days: 365
---

## Excerpts

> In fullscreen mode, a panel now opens beside the conversation and shows uncommitted changes while Claude edits. Toggle it with /diff.

> On Claude Fable 5.1, prompt caching didn't cover the context attached after tool results—that context was resent as uncached input on every single tool call. This bug was fixed in version 2.1.260.

> /cost and the prompt_cache field in the status line now name a likely cause when the prompt cache wasn't hit.

> v2.1.260 reverts the 2.1.259 change that applied Read deny rules to Bash arguments, which had blocked common build and grep compounds even in auto mode.
