---
fetched_at: &id001 2026-06-19
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: cad2c0cea715a071d52bf44543468159221d7324425d6e2dff96f104edda7b30
sources: []
title: 'FastContext: Training Efficient Repository Explorer for Coding Agents'
topic: agentic-coding
url: https://arxiv.org/abs/2606.14066
---

## Excerpts

> Locating relevant code consumes substantial token budget and pollutes the agent's context with irrelevant snippets. FastContext is a dedicated exploration subagent that separates repository exploration from solving, invoked on demand to issue parallel tool calls and return concise file paths and line ranges as focused context.

> FastContext is powered by specialized exploration models spanning 4B--30B parameters, bootstrapped from strong reference-model trajectories and refined with task-grounded rewards for broad first-turn search, multi-turn evidence gathering, and precise citation generation.

> Integrating FastContext improves end-to-end resolution rates up to 5.5% while reducing coding-agent token consumption up to 60%.