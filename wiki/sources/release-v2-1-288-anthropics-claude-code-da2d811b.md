---
fetched_at: &id001 2026-10-03
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: da2d811b9d25331f1ec1ddb3754170c8c92a1c98e15122cf58472609a3128a00
sources: []
title: Release v2.1.288 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.288
---

## Excerpts

> The sandboxing.md documentation was substantially expanded to explain the shell sandbox boundary, what stays outside it, default filesystem and network access, excludedCommands, credential masking, allowed-host behavior, managed-setting locks, and concrete troubleshooting for SSH, Docker, localhost, and host-allowlist failures.

> Added $.ui.selection() for mods: returns the text you last selected in fullscreen mode and, when the selection lies within one transcript row, that row.

> Added --max-findings <n>|all to /code-review to report more or fewer findings than the usual limit.

> Changed the background command time limit to apply only in unattended sessions, while terminal, desktop app and VS Code sessions have no limit.

> Fixed resume occasionally loading a transcript cut short; non-interactive sessions and subagents now continue from partial responses.