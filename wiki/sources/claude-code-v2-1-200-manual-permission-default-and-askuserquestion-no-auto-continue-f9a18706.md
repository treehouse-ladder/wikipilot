---
fetched_at: &id001 2026-07-05
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: f9a1870648a6375ad1696cb5e922e6bf27ec5e9b06a477d00303743635d3eeb4
sources: []
title: Claude Code v2.1.200 — Manual permission default and AskUserQuestion no-auto-continue
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.200
---

## Excerpts

> Changed the "default" permission mode to "Manual" across the CLI, --help, VS Code, and JetBrains; --permission-mode manual and "defaultMode": "manual" are accepted alongside default.

> Changed AskUserQuestion dialogs to no longer auto-continue by default; users can opt into an idle timeout via /config.

> Improved /code-review workflow: merged five cleanup finders into one, cutting token usage by roughly 25%.

> Improved background session reliability: long-running commands and workflows now survive the session's process being stopped, restarted, or updated — including on Windows, where background shells are handed off instead of being killed.