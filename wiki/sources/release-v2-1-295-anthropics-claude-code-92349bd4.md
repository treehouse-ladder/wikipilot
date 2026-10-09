---
fetched_at: &id001 2026-10-09
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 92349bd4a8c11233f065ffd2d5366d8153f8b44d0c35f48c19fdad0137690538
sources: []
title: Release v2.1.295 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
---

## Excerpts

> Added onFailure: "block" for command and HTTP hooks — a hook that fails to start, times out, or exits unexpectedly stops the action rather than letting it through. Added Program Status Protocol (OSC 7501) support, so compatible terminals can show whether it is working, waiting on you, or done. Added CLAUDE_CODE_RETRY_WATCHDOG_MAX_WAIT_MS to limit how long unattended retry mode waits out 429 and 529 errors. Added an optional models list to every Claude apps gateway upstream, so only listed models are sent, including on failover. Fixed claude plugin marketplace add reporting success for a marketplace whose name no plugin can be installed under.