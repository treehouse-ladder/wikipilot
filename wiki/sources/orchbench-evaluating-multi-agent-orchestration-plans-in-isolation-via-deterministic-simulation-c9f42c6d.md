---
fetched_at: &id001 2026-08-19
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: c9f42c6d2de0758f271142a6ff28c5466787c2e4cb0292c55be651fcbd503e2b
sources: []
title: 'OrchBench: Evaluating Multi-Agent Orchestration Plans in Isolation via Deterministic
  Simulation'
topic: agentic-coding
url: https://arxiv.org/abs/2607.25656
---

## Excerpts

> Existing evaluations typically rely on end-to-end execution, which conflates orchestration-plan quality with worker capabilities, tool reliability, and environmental noise. OrchBench constructs directed acyclic graphs (DAGs) that encode task dependencies... Given a DAG, a per-agent context limit, and an agent budget, the evaluated planner assigns subtasks to agents and specifies cross-agent information transfers and their retention ratios.

> A deterministic simulator evaluates the resulting plan without invoking worker agents and returns interpretable measures of result quality, makespan, and token cost. The simulated scores produced by OrchBench correlate strongly with quality scores from Claude Code executions.

> We find that preserving task-critical information is more important than simply increasing the number of agents, and a systematic study of orchestration strategies across workflows containing up to 1,000 subtasks reveals previously hidden coordination failures.