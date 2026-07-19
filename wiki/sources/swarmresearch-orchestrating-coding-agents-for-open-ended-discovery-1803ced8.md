---
fetched_at: &id001 2026-07-19
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 1803ced8938a326e9dba77824bc9423cfd1e08a97dab9d257b2d970045cf7a62
sources: []
title: 'SwarmResearch: Orchestrating Coding Agents for Open-Ended Discovery'
topic: agentic-coding
url: https://arxiv.org/abs/2607.02807
---

## Excerpts

> SwarmResearch is an orchestrator-subagent harness in which a Shepherd Agent uses global context to steer a population of Search Agents, each operating with local context in their respective git branch.

> Explorer Search Agents have fresh context windows so they are unanchored to prior work, while Optimizer Search Agents fork their parent's conversation history to continue along its detailed history of attempts.

> On open-ended optimization tasks, SwarmResearch discovers better or comparable solutions to state-of-the-art LLM-guided evolution and multi-agent techniques on 13/15 tasks, driven by higher-level exploration. Additionally, SwarmResearch's orchestrator-guided scaling discovers better-performing solutions by adapting parallelism at different search depths compared with fixed scaling of serial and parallel agents.