---
fetched_at: &id001 2026-07-31
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 89303d54870d48859423fea544f4ba3f62b8f9498c59155eb544a07c46e20a55
sources: []
title: 'ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU'
topic: ai-in-game-dev
url: https://arxiv.org/abs/2607.19191
---

## Excerpts

> ABot-World-0 turns a single NVIDIA RTX 5090 GPU into a real-time interactive world simulator, enabling infinite action-conditioned world rollout at 720P and up to 16 FPS with 1.2 s action-to-first-frame latency within a peak-VRAM budget of approximately 19 GiB.

> ABot-World-0 is an action-conditioned video world model for real-time, long-horizon closed-loop interaction, supported by a multi-source data infrastructure spanning AAA games, simulation engines, and internet videos to learn controllable world dynamics.

> The model progressively distills a bidirectional action-conditioned teacher into a causal student through teacher forcing and ODE distillation, and introduces LongForcing to align long student self-rollouts with an extended-horizon teacher, mitigating accumulated distribution shift and autoregressive drift.