---
title: "Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack"
kind: source
url: "https://arxiv.org/abs/2605.12673"
sha256: "e91c1eef"
fetched_at: "2026-05-30"
topic: "agentic-coding"
image_count: 0
sources: []
last_updated: 2026-05-30
last_verified: 2026-05-30
freshness_window_days: 365
---

## Excerpts

> BenchJack is an auditing agent that internalizes a flaw taxonomy, automatically analyzes a given benchmark, and produces a verifiable hack that achieves the highest score without actually solving any problems.

> BenchJack was applied to ten popular agent benchmarks covering multiple domains and evaluation methods, and generated working reward-hacking exploits on all of the benchmarks that were audited, achieving near-perfect scores on 9 of 10 benchmarks without actually solving a single task.

> The flaw taxonomy covers five categories: context leakage (task solutions embedded in scaffolding), verification shortcuts (evaluators fooled by surface-level output formatting), environment side-channels (file-system or process artifacts that reveal expected outputs), oracle contamination (test infrastructure that can be queried directly), and metric gaming (scoring functions that reward superficial rather than substantive outputs).
