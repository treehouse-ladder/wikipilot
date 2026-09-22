---
fetched_at: &id001 2026-09-22
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: c9c36d9e98c5bf408cafb1a14ebbee51298c584c6694d58118283ae8a9c7b83f
sources: []
title: 'Subagents vs Agent Skills: Executing Reusable Knowledge for Long-Horizon Agentic
  Tasks'
topic: agentic-coding
url: https://arxiv.org/abs/2609.09233
---

## Excerpts

> Agent skills are typically executed by loading their skill instructions into an agent's context and relying on the agent to follow them. As task horizons grow, however, this approach becomes increasingly brittle, because reasoning quality degrades as more information accumulates in the context window.

> Rather than loading skill instructions into the main context, subagent execution spawns fresh context windows dedicated to solving individual subtasks. Subagent execution outperforms agent-skill execution when skill packages expose clear input-output contracts and their instructions encode the procedural knowledge needed to fulfill those contracts.

> For stronger models, such as GPT 5.3 Codex and Kimi K2.6, subagents lower peak context length on over 80% of tasks. For weaker models, the reduction is smaller and sometimes reverses.

> The tradeoff is additional communication overhead, as extra tokens are required to coordinate between the main agent and its subagents.