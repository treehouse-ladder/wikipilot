---
fetched_at: &id001 2026-05-23
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: dafbe4d6722ee1268e5663e0dc37823e0d2d0f6c9c3efa54f35b3dfa23111714
sources: []
title: 'SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative
  Tasks'
topic: agentic-coding
url: https://arxiv.org/abs/2603.24755
---

## Excerpts

> SlopCodeBench is a benchmark of 36 problems and 196 checkpoints where agents repeatedly extend their own solutions. Unlike prior iterative benchmarks, the evolving specifications demand architectural decisions but leave internal structure to the agent.

> Quality degrades across checkpoints, with structural erosion rising in 77% of trajectories and verbosity in 75.5%. Compared to 473 open-source Python repositories, agent code is 2.3x more verbose and 2.0x more eroded, and the human repositories degrade less often and by smaller margins across their git histories.

> The benchmark measures two forms of degradation: structural erosion (concentrated complexity) and verbosity (redundant code). Explicit quality guidance reduces initial verbosity and erosion by up to a third, without affecting degradation rates.

> SlopCodeBench provides the first measurement of code degradation under iterative extension, revealing that agents pass checkpoints while producing code that erodes and bloats with each turn.