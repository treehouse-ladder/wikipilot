---
fetched_at: &id001 2026-09-29
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: cdf0d63217ad659b5e61b732736ea2b2ba71d6b335decffa38a7f5975f20b0dd
sources: []
title: Release v2.1.284 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
---

## Excerpts

> Added Claude Sonnet 5.5 (claude-sonnet-5-5), now the default Sonnet model on the Anthropic API — 1M context, $2/$10 per Mtok with $0.20/Mtok cache reads

> Interactive terminal and VS Code sessions now start in auto mode when no permission mode is configured, on every plan and provider; permissions.defaultMode still overrides it.

> Added a "Yes, but ask again next time" answer to auto mode's prompt before a read outside the working directories, so you can allow that one read and still be asked about later ones.

> Ultracode is now its own toggle in /effort (Tab, or /effort ultracode [on|off]): it no longer forces xhigh effort and stays on at any effort level.

> Fixed "Prompt is too long" errors that persisted after compacting: when the compacted request is still too long, Claude Code now compacts once more, keeping less of the recent conversation.

> Fixed MCP tool calls in a resumed session failing with "No such tool available" while their server was still connecting; the call now waits up to 10 seconds for the server.