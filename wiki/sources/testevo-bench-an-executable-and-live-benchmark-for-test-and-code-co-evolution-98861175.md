---
fetched_at: &id001 2026-07-08
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 98861175ef6d91827f9164bda0a62cbf25d2159704aa515f90f3e0eef6109c51
sources: []
title: 'TestEvo-Bench: An Executable and Live Benchmark for Test and Code Co-Evolution'
topic: agentic-coding
url: https://arxiv.org/abs/2607.02469
---

## Excerpts

> TestEvo-Bench is a benchmark of test and code co-evolution tasks mined from software repositories, with two tracks: in test generation, the agent shall write new tests to capture the new software behavior; in test update, the agent shall adapt failing existing tests to the changed software behavior. Each task is anchored to a real commit history and packaged with environment configuration to support execution-grounded metrics such as pass rate, coverage, and mutation score. The current snapshot contains 746 test generation and 509 test update tasks, curated from 59,950 candidate co-evolution records across 152 open-source Java projects. Each task records the timestamp of the test and code changes, and new tasks are periodically mined by our automated pipeline, so evaluation can be restricted to tasks postdating a model's training cutoff to reduce data leakage risk. State-of-the-art agents that combine strong harnesses (Claude Code, Gemini CLI, and SWE-Agent) with strong foundation models (Claude Opus 4.7 and Gemini 3.1 Pro) achieve up to 77.5% success rate on test generation and 74.6% on test update.