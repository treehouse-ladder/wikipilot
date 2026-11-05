---
fetched_at: &id001 2026-11-05
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 4841cbfc0576617fe72e1e8a20ee1c9da1daf24086a1a4024deec5562c0da1eb
sources: []
title: 'Axion 1.0: Open Agent Foundation Models, Simplified'
topic: frontier-models
url: https://arxiv.org/abs/2611.03233
---

## Excerpts

> Axion 1.0 is a fully open agent foundation model built on a deliberately simple training recipe: post-training uses two lightweight supervised fine-tuning stages followed by reinforcement learning over agent trajectories, skipping mid-training, direct preference optimization, and on-policy distillation.

> Axion 1.0 performs strongly across a range of agentic benchmarks and is competitive with leading commercial models on several of them.

> Beyond the model weights, we release the data construction and filtering pipeline, verification steps, prompts, and training code so that others can reproduce and extend the work.

> A 35B reproduction checkpoint (a Mixture-of-Experts model with roughly 35B total and about 3B active parameters) is released under Apache 2.0; the paper also covers a 122B variant. The project is from ByteDance (code at github.com/bytedance/axion1_0).

> The 35B reproduction checkpoint scores 52.8 on HLE, 35.3 on BioMysteryBench, 60.4 on SEAL-0, 45.9 on HiPhO, 85.0 on FrontierScience Olympiad, and 55.0 on FrontierScience Research, using approximately 18K SFT examples.