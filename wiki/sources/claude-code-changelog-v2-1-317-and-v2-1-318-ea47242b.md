---
fetched_at: &id001 2026-11-06
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: ea47242bcd03cf52548c80cd070a33355efbac07e6b675fa2e759f1aade617b1
sources: []
title: Claude Code CHANGELOG — v2.1.317 and v2.1.318
topic: agentic-coding
url: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

## Excerpts

> Added an `effort` option to a mod's `$.model.fork`, so a quick side job can run at `low` whatever effort the session uses; the result reports the effort sent

> Fixed stdio MCP servers that exit on the version probe being re-probed on every start; a server that dies in under 3s for its own reason is also pinned to the legacy handshake for 7 days

> Improved MCP tool errors: a call made before the tool is loaded now returns its input schema

> Fixed workflows re-running finished agents when resumed after a usage limit

> Fixed idle compaction replacing a conversation with a reply that was not a summary

> Fixed the "Now using usage credits" notice reappearing about every 30 seconds while a background subagent is running

> Changed subagents and teammates on a different model from the main conversation to use that model's saved effort level or its default, instead of the session's effort level

> [VSCode] Fixed forked conversations dropping messages: only one of the tool calls Claude ran in parallel was kept, and the last messages a compaction kept were lost, which could leave Claude's answer without the question it answered

> Fixed skills synced from claude.ai being lost or downloaded again every ten minutes when they can't be written to disk

> Fixed project and local MCP servers disconnecting after the first turn in some Claude desktop sessions

> Added `onFailure: "block"` for Agent SDK hook callbacks, so a callback that fails blocks the action instead of letting it run

> Fixed `DISABLE_PROMPT_CACHING_OPUS` and `DISABLE_PROMPT_CACHING_SONNET` having no effect on `[1m]`, other-region and undated spellings of the default model