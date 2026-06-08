---
fetched_at: &id001 2026-06-08
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 694ee439a92100b32cd11231b205eb0ea8d65efd03a32ec4e7afc522495e86e4
sources: []
title: An Agentic Approach Towards Replication Package Quality Evaluation
topic: agentic-coding
url: https://arxiv.org/abs/2606.02006
---

## Excerpts

> We consolidated 380 requirements from 34 sources into 51 reproducibility criteria, of which 31 are operationalized for automated artifact-based evaluation. We implement a multi-agent prototype that automatically inspects replication packages and produces evidence-grounded improvement reports.

> A preliminary evaluation on five replication packages shows high inter-run consistency of 91.4% and 75.4% correctness, through micro-averaged agreement with a manual baseline. The agent performs best on structural criteria such as code, environment, and artifact availability, but struggles with qualitative or mixed-method criteria that require subjective judgement.

> Our pipeline decomposes the task by criterion type: structural checks run as deterministic scripts dispatched by a planner agent, while qualitative checks invoke an LLM judge with the relevant artifact slice as context. Decoupling the deterministic from the qualitative cuts cost by ~40% versus a single-prompt baseline while preserving recall.