---
fetched_at: &id001 2026-06-22
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 0019f733096c8548d29554ddcaf7f7807fdb5cbe12c83b99370b2fab9f03b84f
sources: []
title: 'Position: Coding Benchmarks Are Misaligned with Agentic Software Engineering'
topic: agentic-coding
url: https://arxiv.org/abs/2606.17799
---

## Excerpts

> Coding agents have become a major mode of software engineering, but the benchmarks used to compare them were designed in a pre-agent era: they collapse model, harness, and environment into a single end-to-end score, typically computed against one reference solution, with no component-level signal for iteration.

> A coding agent in practice is not a model but a system harness—a composite of models, harnesses, contexts, environments, and feedback signals, any one of which can move the benchmark score by margins comparable to those between adjacent model generations.

> Benchmarks like SWE-Bench, HumanEval, MBPP, LiveCodeBench, and BigCodeBench all share the same structure: a single model, harness, and environment together produce a single number—an end-to-end system score with no signal at the level of individual components—which is often compared against a single reference solution.