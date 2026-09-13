---
fetched_at: &id001 2026-09-13
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 2a68cabb6c20de64eba595ba7cfd0e611a2edccd815714f5e6eca37ce0453678
sources: []
title: Release v2.1.270 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.270
---

## Excerpts

> Added --json to claude plugin install, uninstall, update, enable and disable, and errorDetails/noteDetails to each row of claude plugin list --json.

> Fixed every turn failing with HTTP 400 on third-party Anthropic-compatible endpoints (ANTHROPIC_BASE_URL) since 2.1.265: a regex in the Artifact tool's input schema that those endpoints reject.

> Fixed sustained high CPU usage: a busy loop in long-running idle sessions no longer pins a CPU core, and rapid terminal focus reports during a session recap no longer keep the CPU high.

> Fixed long-context 429s on Fable models showing the usage-credits consent prompt instead of the 1M-context message on Pro and Team plans.