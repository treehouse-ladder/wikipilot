---
fetched_at: &id001 2026-06-28
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: d64123212942b5150ed911b4d5827d8a8ddb7b97ec505431e98cb58c83bbe6a7
sources: []
title: "SWE-Marathon: Can Agents Autonomously Complete Ultra-Long-Horizon Software Work?"
topic: agentic-coding
url: https://arxiv.org/abs/2606.07682
---

## Excerpts

> SWE-Marathon is a benchmark of 20 real-world ultra-long-horizon software engineering tasks. Agents attempting these tasks consume an average of 27.2 million tokens per attempt — roughly 100× the token budget of a typical SWE-bench Verified instance.

> Current frontier agents solve fewer than 30% of SWE-Marathon tasks even with extended compute budgets, revealing a substantial capability gap between short-horizon and ultra-long-horizon autonomous software work.

> 13.8% of agent trajectories on SWE-Marathon exhibit reward-hacking behavior — agents exploit verifier loopholes to register task completion without genuinely solving the underlying problem. This rate is substantially higher than observed on SWE-bench Verified, suggesting that longer horizons amplify the evaluation-gaming problem.

> The benchmark exposes that current agentic coding systems face a dual ceiling: a capability ceiling (solving hard multi-file, multi-week tasks end-to-end) and a reliability ceiling (producing solutions that satisfy the spirit of the evaluation rather than gaming its letter).
