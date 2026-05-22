---
fetched_at: &id001 2026-05-22
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 26980c45078dbfac3c3613eb82a58e08388bc4edb93045f063bb74e51fb399f8
sources: []
title: 'SWE-Chain: Benchmarking Coding Agents on Chained Release-Level Package Upgrades'
topic: agentic-coding
url: https://arxiv.org/abs/2605.14415
---

## Excerpts

> SWE-Chain contains 12 upgrade chains across 9 real Python packages, with 155 version transitions and 1,660 grounded upgrade requirements, where each transition builds on the agent's prior codebase.

> The benchmark uses a divide-and-conquer synthesis pipeline that aligns release notes with code diffs for each version transition, ensuring the requirements are grounded in actual code changes, informative to agents, and feasible to implement.

> Across nine frontier agent-model configurations, agents achieve an average of 44.8% resolving, 65.4% precision, and 50.2% F1 under the Build+Fix regime, with Claude-Opus-4.7 (Claude Code) leading at 60.8% resolving, 80.6% precision, and 68.5% F1.

> The results show that current agents still struggle to make correct upgrades across chained package releases without breaking existing functionality.