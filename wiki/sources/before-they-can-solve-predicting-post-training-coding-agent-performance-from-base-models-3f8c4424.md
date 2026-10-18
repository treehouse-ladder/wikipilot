---
fetched_at: &id001 2026-10-18
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 3f8c4424303b37f14f65df31701c73859750a98be102b506176f66890c905416
sources: []
title: 'Before They Can Solve: Predicting Post-Training Coding-Agent Performance from
  Base Models'
topic: agentic-coding
url: https://arxiv.org/abs/2610.10478
---

## Excerpts

> standard end-to-end pass@K is a weak fit here because many base checkpoints cannot reliably produce the tool calls needed to finish a task. In their experiments on ten pairs of open-source base and post-trained models, the Spearman correlation with post-trained SWE-Bench Verified pass@1 ranged from 0.830 (RepoBench XFirst) to -0.394 (HumanEval).

> It replays each trajectory to find a decisive step, the first step whose cumulative patch turns failing tests into passing ones. It then scores base checkpoints with three probes at that step: Decisive-Action BPB, Patch MCQ, and prefix-conditioned pass@K.