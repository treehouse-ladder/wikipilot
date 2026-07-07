---
title: "Better Models: Worse Tools"
kind: source
url: https://simonwillison.net/2026/Jul/4/better-models-worse-tools/
sha256: df80d6a1
fetched_at: 2026-07-07
topic: agentic-coding
image_count: 0
sources: []
last_updated: 2026-07-07
last_verified: 2026-07-07
freshness_window_days: 365
---

## Excerpts

> Newer Claude models sometimes call Pi's edit tool with extra, invented fields in the nested edits[] array. The edit itself is usually correct but the arguments do not match the schema, so Pi rejects the tool call and asks it to try again. This is getting worse with newer Anthropic models: both Opus 4.8 and Sonnet 5 show it but none of the older models do. Armin theorizes this is because more recent Anthropic models have been specifically trained (presumably via reinforcement learning) to better use the edit tools that are baked into Claude Code.
