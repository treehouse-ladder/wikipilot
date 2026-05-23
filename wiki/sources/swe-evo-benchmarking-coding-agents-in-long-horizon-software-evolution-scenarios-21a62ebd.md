---
fetched_at: &id001 2026-05-23
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 21a62ebdeff24d6b7770480ba0afc71982e7c8374579a847399c70b930199d32
sources: []
title: 'SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios'
topic: agentic-coding
url: https://arxiv.org/abs/2512.18470
---

## Excerpts

> SWE-EVO is a benchmark for long-horizon software evolution challenges, constructed from release notes of seven mature open-source Python projects comprising 48 tasks requiring multi-step modifications spanning an average of 21 files, validated against test suites averaging 874 tests per instance.

> While existing benchmarks for AI coding agents focus on isolated, single-issue tasks such as fixing a bug or adding a small feature, real-world software engineering is a long-horizon endeavor where developers interpret high-level requirements, coordinate changes across many files, and evolve codebases over multiple iterations while preserving functionality.

> Experiments reveal a striking capability gap: GPT-5.4 with OpenHands achieves only 25% on SWE-EVO versus 72.80% achieved by GPT-5.2 on SWE-Bench Verified, showing that current agents struggle with sustained, multi-file reasoning.

> The benchmark also proposes Fix Rate, a metric capturing partial progress on these complex, long-horizon tasks.