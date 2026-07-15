---
title: "PERFOPT-Bench: Evaluating Coding Agents on Software Performance Optimization"
kind: source
url: "https://arxiv.org/abs/2607.07744"
sha256: "0c17f7ce"
fetched_at: 2026-07-15
topic: agentic-coding
image_count: 0
sources: []
last_updated: 2026-07-15
last_verified: 2026-07-15
freshness_window_days: 365
---

## Excerpts

> Each task provides a correct but deliberately suboptimal codebase and asks the agent to improve a target performance metric; scoring requires hidden correctness tests, verified-speedup measurement, and trajectory-level audit. [...] Performance optimization is a distinct agentic task: agents must profile executions, diagnose cross-layer bottlenecks, edit code without breaking correctness, and verify that gains are reproducible rather than measurement artifacts. [...] We evaluate 7 agent stacks with different LLMs and agent frameworks on 12 long-horizon optimization tasks. Optimization performance is workload-dependent rather than determined by model identity alone: no single stack dominates, and changing the agent framework can materially change the same LLM's per-task speedup profile.
