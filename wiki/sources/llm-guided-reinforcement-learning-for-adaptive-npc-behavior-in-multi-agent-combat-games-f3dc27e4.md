---
fetched_at: &id001 2026-09-05
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: f3dc27e4625e3605f5dc3bfed389e7f12d63c9433e2735211c691c744740d3ea
sources: []
title: LLM-Guided Reinforcement Learning for Adaptive NPC Behavior in Multi-Agent
  Combat Games
topic: ai-in-game-dev
url: https://arxiv.org/abs/2609.02931
---

## Excerpts

> Scripted and rule-based non-player characters (NPCs) in combat video games often exhibit predictable behaviors that experienced players can exploit, while reinforcement learning (RL) agents typically retain a fixed policy after training and cannot readily adapt their strategy to different opponents.

> We investigate a runtime strategy-selection framework in which a large language model (LLM) guides a trained RL policy without modifying its underlying behavior. We train five NPC agents with a shared PPO policy in Unity and compare a baseline configuration, in which the policy acts independently, with an LLM-augmented configuration in which a locally hosted Mistral 7B model, accessed through Ollama, reads the live game state every five seconds and assigns one of four tactical tags.

> The evaluation uses three scripted opponent types across 600 episodes with Mann-Whitney U test analysis.