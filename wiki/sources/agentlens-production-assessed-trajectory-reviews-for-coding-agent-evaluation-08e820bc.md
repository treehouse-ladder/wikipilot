---
fetched_at: &id001 2026-07-24
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 08e820bcd6acda0caf4151831f112c24120a8ab3853059ff833c8c395c40613b
sources: []
title: 'AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation'
topic: agentic-coding
url: https://arxiv.org/abs/2607.06624
---

## Excerpts

> AgentLens is a production-assessed benchmark for interactive code agents. While most code-agent benchmarks reduce a run to a single bit—did the task pass?—the people who actually use these agents experience the entire trajectory: how the agent follows instructions, uses its tools, verifies its own work, recovers from mistakes, and talks to them along the way. AgentLens evaluates that whole trajectory.

> It pairs formal verification, where an objective check exists, with LLM-written trajectory reviews and side-by-side comparisons, so that each run yields a readable explanation of why the score is what it is. This makes AgentLens useful for more than ranking models: the authors use it to diagnose model behavior, compare successive versions of their own agent, and catch product regressions in a nightly evaluation pipeline.