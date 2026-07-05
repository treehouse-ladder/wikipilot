---
fetched_at: &id001 2026-07-05
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: e36be334d348272165991373012c8fa0cf407196845cf3e077ad8932b263d434
sources: []
title: Fable's judgement
topic: agentic-coding
url: https://simonwillison.net/2026/Jul/3/judgement/
---

## Excerpts

> For all coding tasks use your judgement to decide an appropriate lower power model and run that in a subagent.

> Tasks that are primarily writing or editing code should spawn an Agent with a model override—using Sonnet for substantive implementation and Haiku for trivial or mechanical edits—with a self-contained prompt, and then reviewing the result in the main loop before committing.

> Implementation work rarely needs the top-tier model, while judgment, review, and synthesis stay with the main loop.