---
fetched_at: &id001 2026-06-07
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 5f71be826c04c567def1a007e96a7bf41e986fe3aaced604dddfdd8b805ec1e4
sources: []
title: 'Retrospective Harness Optimization: Improving LLM Agents via Self-Preference
  over Trajectory Rollouts'
topic: agentic-coding
url: https://arxiv.org/abs/2606.05922
---

## Excerpts

> AI agents rely on a harness of skills, tools, and workflows to solve complex problems. Continually improving this harness is essential for adapting to new tasks. However, existing optimization methods typically require ground-truth validation sets, yet such labeled data is difficult to acquire in practical deployment settings.

> We introduce Retrospective Harness Optimization (RHO), a self-supervised method that optimizes the agent harness using only past trajectories. Specifically, RHO selects a diverse coreset of challenging tasks from past trajectories and re-solves them in parallel. The agent analyzes these rollouts using self-validation and self-consistency, then generates candidate harness updates and selects the most effective one by its own pairwise self-preference.

> We evaluate RHO across three diverse domains, spanning software engineering, technical work, and knowledge work.