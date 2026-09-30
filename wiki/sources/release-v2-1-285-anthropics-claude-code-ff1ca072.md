---
fetched_at: &id001 2026-09-30
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: ff1ca072bf39e4719a02d6be0df8531603f501d134fa83117cc1193a23023f71
sources: []
title: Release v2.1.285 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
---

## Excerpts

> Added CLAUDE_CODE_DISABLE_WEB_FETCH environment variable to turn off the WebFetch tool

> Added <server>.<key>=<value> to claude plugin install --config, so a bundled .mcpb MCP server's own settings can be set at install time and it starts without visiting /plugin -> Configure

> Fixed claude -p with CLAUDE_CODE_FORK_SUBAGENT=1: a subagent's own Agent call now runs in the foreground, so the subagent gets the child's result

> Added claude plugin configure <plugin> to show a plugin's options and which are unset, or save new values read from stdin with --values-stdin

> Fixed synchronous hooks hanging Claude Code while a background process the hook started (for example some-daemon &) kept its output open; the hook now finishes shortly after its own process exits