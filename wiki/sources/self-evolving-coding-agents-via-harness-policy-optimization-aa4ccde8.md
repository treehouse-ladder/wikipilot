---
fetched_at: &id001 2026-10-20
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: aa4ccde86d8a3d2eaf50d0df4ebc5c48474096e1f344b09fe1748e22d585c33f
sources: []
title: Self-Evolving Coding Agents via Harness-Policy Optimization
topic: agentic-coding
url: https://arxiv.org/abs/2610.22791
---

## Excerpts

> We present Self-HPO, a recursive self-improvement framework that alternates harness and policy optimization, using the evolving policy as its own harness proposer. In the harness step, the current policy analyzes its own failures and suggests new harness candidates; in the policy step, the policy is updated with reinforcement learning under the selected harness, and hard tasks found during training seed the next harness search. Self-HPO beats both harness-only and policy-only baselines across three coding benchmarks: on Qwen3.5-35B-A3B the average resolve rate rises from 57.8% to 64.8%, with gains in out-of-distribution settings, better pass@1 reliability, and higher pass@k.