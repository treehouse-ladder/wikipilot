---
fetched_at: &id001 2026-11-10
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: ace31f3b0bb1b6f07ef93a70e921fede0960c848287ce911677409ebd0b28f56
sources: []
title: Release v2.1.321 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.321
---

## Excerpts

> Added Claude Fable 5.2 (`claude-fable-5-2`), now the default Fable model — 1M context, $8/$40 per Mtok with $0.20/Mtok cache reads

> Added `--settings <file>` to `claude remote-control`, which applies a settings file to every session it starts; if the file changes, no new session starts until you restart `claude remote-control`

> Fixed MCP OAuth requests sending secrets such as refresh tokens to another host when a server redirected them

> Fixed a case where a read-only Bash command ran outside the sandbox without a permission prompt

> Fixed a case where Bash permission checks judged a file write from the wrong folder and didn't prompt

> Fixed deny rules and protected-file prompts not applying to the file that a `cp` or `mv` into a directory writes

> Fixed auto mode losing a background subagent's report that had started a turn when the conversation was compacted before Claude answered it

> Fixed a large hook output pointing Claude to a file that held another hook's output from the same tool call