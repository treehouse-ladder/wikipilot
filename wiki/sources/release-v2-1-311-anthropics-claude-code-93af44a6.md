---
fetched_at: &id001 2026-10-28
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 93af44a64968d818864ad4ac51cc24a79be5a9f792f27c5842419b0a78fb0d34
sources: []
title: Release v2.1.311 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.311
---

## Excerpts

> Fixed subagents being unable to use MCP tools from servers that finish connecting after the subagent starts

> Fixed `SubagentStop` hooks running about twice a minute for each running subagent instead of once when it finishes

> Fixed standard-context sessions stopping with "Usage credits required for 1M context" when a request ran over 200K tokens; Claude Code now compacts the conversation and continues

> Fixed a subagent's isolated worktree being removed while a background subagent it started was still working in it

> Fixed background agents in auto mode that wait on their own shells starting a new main conversation turn on every wake

> Added `--hold-idle-file` and `--max-hold-min` to `self-hosted-runner`, to keep an idle session while your host reports processes it left running