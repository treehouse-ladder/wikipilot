---
fetched_at: &id001 2026-08-21
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 9d6bd7a9e4de1d74b0698867ddabcc7c3e165ec721fefe530d0606be393ffd77
sources: []
title: 'Agent Lightning v1.0: Towards Harnessed Agentic RL'
topic: agentic-coding
url: https://arxiv.org/abs/2608.17528
---

## Excerpts

> Harnessed agentic RL is a paradigm where the deploy-time harness directly participates in model post-training. It differs fundamentally from traditional agentic RL: the harness, rather than the training engine, owns the environment interaction loop, while the trainer observes only sequences of LLM request-response pairs.

> Agent Lightning v1.0 is a lightweight framework for harnessed agentic RL implemented in approximately 3,500 lines of code and supports arbitrary agent harnesses [such as mini-SWE-agent, OpenHands, OpenCode, Claude Code, and Codex]. Using only 6K training examples and modest compute, RL improves Qwen3.5-9B on SWE-bench Verified from 41.8% to 56.4%, a 14.6-point absolute gain.

> Harnessed agentic RL introduces challenges in retokenization, sample merging, advantage calculation, loss normalization, and backend scheduling, which can substantially affect training stability and effectiveness.