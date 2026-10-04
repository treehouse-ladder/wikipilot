---
fetched_at: &id001 2026-10-04
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: ec08581411bc9dc6e098771d531a4ac8c397eed73192c9e62646bde33fcb18ad
sources: []
title: Release v2.1.289 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.289
---

## Excerpts

> Added agent.spawn for teammates, one agent id across plugin hook events, and idle and waiting states in $.agent.list(). | Fixed Bash deny and ask rules missing a command behind an environment variable prefix with an expanded value (for example TZ="$HOME" rm -rf build) when the sandbox auto-allows commands. | Fixed Read deny rules not applying to files @-mentioned, changed, or selected in the IDE through a symlink. | Fixed a deny or ask rule on a nested part of a compound shell command not holding over a user-installed mod's approval on managed machines. | Fixed a user-installed plugin being able to rewrite the descriptions of an organization-managed MCP server's sign-in tools.