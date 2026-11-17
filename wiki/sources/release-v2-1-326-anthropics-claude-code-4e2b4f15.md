---
fetched_at: &id001 2026-11-17
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 4e2b4f1543d148003d9a74b767a72230b5413c58fe8687b737882e83448700f5
sources: []
title: Release v2.1.326 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.326
---

## Excerpts

> Added support for turning on Code Mode while agent teams are enabled; if you already turned it on, sessions with teams on now start in Code Mode

> Added a startup warning when an `--allowedTools`, `--disallowedTools` or `--tools` value has an entry that doesn't look like a complete rule

> Added a message explaining why MCP servers stop loading when an administrator adds `managed-mcp.json` during a session

> Fixed `cp` of a file being refused when only its source was covered by an `Edit` deny rule

> Fixed Bash commands that delete or overwrite files (`find -delete`, `cat a > b`, `sort -o`) being summed up in the transcript as a search or a read

> Fixed background sessions losing the LLM gateway your shell exported after a crash, after a reopen from another folder, or when the background service lacks it: they now stop before any model request

> Fixed the background service ending your own processes, such as an SSH login, when a process number on its list had been reused by another user's process

> Fixed empty placeholder files, including `.git/config.lock`, sometimes being left in the project on Linux when Claude Code was stopped during a sandboxed command

> Fixed settings files with values nested thousands of levels deep crashing Claude Code or applying only some of the time; values past 64 levels are now dropped with a warning