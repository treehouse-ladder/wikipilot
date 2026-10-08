---
fetched_at: &id001 2026-10-08
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 0ba886b07133e21ddbd6c0029c502b74edc3420d21331506de6e754a3346c5f9
sources: []
title: Release v2.1.293 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.293
---

## Excerpts

> Added agentType to the subagentStatusLine payload, so scripts can tell custom subagent types apart.

> Added Claude Haiku 5.5 (claude-haiku-5-5), now the default Haiku model on the Anthropic API with a 1M context window.

> Fixed a memory leak where an HTTP MCP connection kept every request it had sent until it closed.

> Fixed claude purge stopping silently (exit 0, or a hang in a terminal) when a file or folder could not be deleted; it now deletes the rest, lists what failed, and exits 1.

> Added isDeferred to $.tool.register for mods: false lists the tool's schema in the prompt from the start instead of behind tool search.