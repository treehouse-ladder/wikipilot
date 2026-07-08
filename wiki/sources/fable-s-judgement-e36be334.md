---
fetched_at: &id001 2026-07-08
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

> For all coding tasks use your judgement to decide an appropriate lower power model and run that in a subagent. When a task is primarily writing or editing code, spawn an Agent with a model override (sonnet for substantive implementation, haiku for trivial/mechanical edits) and a self-contained prompt, then review the result in the main loop before committing. Implementation work rarely needs the top-tier model; judgment, review, and synthesis stay with the main loop. So far it seems to be working well, getting a ton of work done with my Fable allowance shrinking less quickly than before.