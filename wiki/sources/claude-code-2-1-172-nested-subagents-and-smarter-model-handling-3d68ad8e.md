---
title: "Claude Code 2.1.172 — Nested subagents and smarter model handling"
kind: source
url: "https://code.claude.com/docs/en/changelog"
sha256: "3d68ad8e1324eb33b763f82183f512fc6276fa6e33aa56b7b51a994d2a3e9fb9"
fetched_at: "2026-06-12"
topic: agentic-coding
image_count: 0
sources: []
last_updated: 2026-06-12
last_verified: 2026-06-12
freshness_window_days: 365
---

## Excerpts

> Claude Code 2.1.172 (June 10, 2026): sub-agents can now spawn their own sub-agents (up to 5 levels deep), and a search bar was added when browsing a marketplace's plugins in /plugin.

> The motivation for nested sub-agents is context management, not parallelism — each subagent gets a fresh context window, so nesting lets a sub-agent offload before its own context fills.

> Claude Code 2.1.173 (June 11) followed up by fixing Fable 5 model names with a [1m] suffix not being normalized and a spurious 'sandbox dependencies missing' startup warning on Windows.
