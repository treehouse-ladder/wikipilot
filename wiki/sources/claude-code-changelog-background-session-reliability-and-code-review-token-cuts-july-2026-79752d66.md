---
fetched_at: &id001 2026-07-01
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 79752d666a23500597a42ad3a3befa366346af901ec7b88e4f37afc89baa0096
sources: []
title: Claude Code CHANGELOG — background session reliability and code-review token
  cuts (July 2026)
topic: agentic-coding
url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

## Excerpts

> Improved background agents: workers killed by a daemon restart are now automatically resumed from where they left off the next time the agents view opens.

> Background session reliability: long-running commands and workflows now survive the session's process being stopped, restarted, or updated — including on Windows, where background shells are handed off instead of being killed.

> Improved /code-review workflow: merged five cleanup finders into one, cutting token usage by roughly 25%.

> The streaming idle watchdog is now on by default for all providers — it aborts and retries when a response stream produces no events for 5 minutes.

> Fast mode for Claude Opus 4.7 has been deprecated, with removal on July 24, 2026. After removal, requests to claude-opus-4-7 with speed: "fast" will return an error. Users should migrate to fast mode for Claude Opus 4.8.