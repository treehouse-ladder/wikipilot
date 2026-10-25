---
fetched_at: &id001 2026-10-25
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: d4e3b3d8fe42d48585c4a319cfa71dae7ae771e98a37147bb392880d7e56fe46
sources: []
title: 'Verifying Coordination in Parallel Coding Agents: NP-Bench and a Scheduling
  Planner'
topic: agentic-coding
url: https://arxiv.org/abs/2610.07261
---

## Excerpts

> Each passes its own tests while the merged result is broken, a failure mode single-agent evaluation misses. Most coordination tools treat this reactively, watching for a conflict and then warning, but under agent-speed concurrency the warning arrives after the wasted edit. The authors frame coordination as scheduling: take each work item's declared scope, partition the work into disjoint scopes, and order merges along the producer-consumer dependency graph, all up front. This planner is built into Nerveplane, a local-first system. NP-Bench compares three arms (no coordination, reactive detection, proactive planning) and checks integration against a real git merge. In simulation the planner raised clean-integration success from 1/9 to 9/9 scenarios and cut merge conflicts from 13 to 0; on a live breaking contract change clean-integration rose from 0 under both baselines to 1.0 on a frontier model and 0.6 on a small one. A cross-session memory cut the repeated-mistake rate from 1.00 to 0.00.