---
fetched_at: &id001 2026-11-18
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 8f7a055a1b360233ad87f8f6e9ed14545bc77431e59e77c825c7cd5ff6f24435
sources: []
title: Release v2.1.327 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.327
---

## Excerpts

> /install-github-app now asks for confirmation before modifying a repository to prevent accidental changes

> Added claude mcp add-json <name> - to read the server's JSON from stdin, so tokens can stay off the command line; not available inside a Claude Code session

> Added /tui classic as the name for the non-fullscreen renderer; /tui default still works

> Changed auto mode to ignore more allow rules that run any package, like Bash(pnpm dlx *), and path or version forms of ones it already ignored (/usr/bin/npm run:*); the safety check decides those