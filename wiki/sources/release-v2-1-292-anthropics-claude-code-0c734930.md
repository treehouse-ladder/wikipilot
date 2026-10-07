---
title: "Release v2.1.292 · anthropics/claude-code"
kind: source
url: "https://github.com/anthropics/claude-code/releases/tag/v2.1.292"
sha256: "0c734930"
fetched_at: "2026-10-07"
topic: "agentic-coding"
image_count: 0
sources: []
last_updated: 2026-10-07
last_verified: 2026-10-07
freshness_window_days: 365
---

## Excerpts

> Added `effort` parameter to the Agent tool for running sub-agents at specified effort levels

> Added `--marketplace <source>` flag to `claude plugin install` to automatically add and install plugins from marketplaces with policy checks

> Added prompt caching to `$.model.complete` with `cache: true` support on text blocks

> Added workflow agents to `agent.spawn` mod hook with run and index information

> Local MCP server connections now negotiate protocol version 2026-07-28 by default

> Fixed sandboxed commands reading staged `/ultrareview` upload files

> Fixed managed sandbox read-deny paths not dropping project grants mid-session

> Fixed tampered on-disk cache bypassing built-in policy plugin

> Fixed PreToolUse hook approvals and auto mode now respect permission prompts for network (UNC) paths
