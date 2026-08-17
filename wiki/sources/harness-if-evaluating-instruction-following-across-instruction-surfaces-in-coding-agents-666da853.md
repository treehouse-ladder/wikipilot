---
fetched_at: &id001 2026-08-17
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 666da8532f0288e0a34b4dca9c9db0c5119119457c2ad897b746462eb303fc7f
sources: []
title: 'Harness-IF: Evaluating Instruction Following Across Instruction Surfaces in
  Coding Agents'
topic: agentic-coding
url: https://arxiv.org/abs/2608.11727
---

## Excerpts

> When a coding agent obeys a rule, it may simply have been going to do that anyway. Existing instruction-following benchmarks cannot tell the difference: they concentrate rules in the user turn, while coding-agent benchmarks emphasize final task success.

> We introduce Harness-IF, which scores operational rules one at a time from execution evidence: 60 realistic multi-turn coding items drawn from a 642-rule library, 256 rules receiving verdicts, placed on the five configurable surfaces a deployed agent reads.

> To separate compliance from coincidence we introduce Against-Prior Accuracy (AP-Acc), which scores only rules labeled as opposing unprompted defaults, observed by re-running tasks with the rule withheld across nine probe builds.

> Across 12 frontier models, accuracy spans 72.1-85.9% and AP-Acc 66.1-78.6%; every model is worse on against-prior rules, by 3.6 to 7.4 points (mean 5.81).