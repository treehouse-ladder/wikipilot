---
fetched_at: &id001 2026-10-05
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 388f3c12da84e0d334fdd8b1e0f7f95bda7abedbbf6658344b87e85a7ffc6414
sources: []
title: Cross-Benchmark Transfer from RL on Agentic Coding Tasks
topic: agentic-coding
url: https://arxiv.org/abs/2610.00890
---

## Excerpts

> Coding agents often fail in the last mile: they build most of a feature but drop a requirement, test only the cases their implementation already handles, break behavior that was supposed to stay intact, or validate against an unchecked assumption.

> We post-train Kimi K2.7 Code, a 1T-parameter (32B active) open-weight mixture-of-experts model, with RL alone on 1,700 tasks: 1,000 repository tasks graded by hidden fail-to-pass tests and by pass-to-pass tests of existing behavior, and 700 terminal tasks graded by expert-written hidden verifiers.

> One epoch of GSPO on a rank-32 LoRA adapter improves pass@1 on each of the six external benchmarks evaluated, across three agent harnesses: SWE-Bench Pro (60.1 to 64.8), DeepSWE (31.0 to 43.4), Terminal-Bench 2.1 (67.4 to 82.0), Terminal-Bench 3 (1.4 to 12.1), Terminal-Bench 4 (0.0 to 7.6), and SWE-Marathon (5.0 to 25.0).