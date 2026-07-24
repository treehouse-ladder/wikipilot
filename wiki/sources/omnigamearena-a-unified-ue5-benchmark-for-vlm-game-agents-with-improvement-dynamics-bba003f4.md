---
fetched_at: &id001 2026-07-24
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: bba003f4b202a0566b226bab32f18b81e942993ec48b88f2863180cf5ef234fe
sources: []
title: 'OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement
  Dynamics'
topic: ai-in-game-dev
url: https://arxiv.org/abs/2606.09826
---

## Excerpts

> OmniGameArena is a real-time benchmark of twelve newly built Unreal Engine 5 games spanning Solo (7), PvP (3), and Coop (2) with unified action interfaces, and the Improvement Dynamics Curve (IDC), an agentic-reflection harness in which a tool-using reflector LLM autonomously refines a bounded skill prompt across multiple rounds.

> Game benchmarks for VLM agents typically report a single first-attempt score per (agent, game) pair, focus on single-agent Solo play, and lack unified protocols for evaluating heterogeneous agent classes (commercial VLMs, open-weight VLMs, and specialized game policies) on the same footing. OmniGameArena addresses these gaps.

> Across twelve agents on the cold-start leaderboard, no single VLM dominates, and commercial agents hold a wide gap over open-weight VLMs and specialized policies. Among the four top agents that run through IDC, all four improve over their cold-start baseline through reflection, yet peak performance is typically reached mid-curve rather than at the final round.

> Most notably, origin-task improvement and held-out variant transfer can diverge in experiments; this divergence is hidden by single-round leaderboard scores and is a central observable IDC exposes.