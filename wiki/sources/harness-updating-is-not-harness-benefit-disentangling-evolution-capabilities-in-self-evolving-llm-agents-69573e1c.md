---
fetched_at: &id001 2026-06-07
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 69573e1c029c6c0d086ed4af4ce1862d410cbca1855d9920b31f997ad2a25679
sources: []
title: 'Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities
  in Self-Evolving LLM Agents'
topic: agentic-coding
url: https://arxiv.org/abs/2605.30621
---

## Excerpts

> LLM agents are increasingly deployed as systems built around editable external harnesses, including prompts, skills, memories and tools, that shape task execution without changing model parameters. Harness self-evolution adapts such agents by updating these harnesses from execution evidence.

> We analyze two key capabilities: (i) harness-updating, the capability to produce useful persistent harness updates from execution evidence; (ii) harness-benefit, the capability to benefit from updated harnesses during task solving. The gain may come from the evolver producing higher-quality harness updates, or from the task-solving agent using the updated harnesses more effectively during task solving, and end-to-end scores cannot disentangle these contributions.

> Harness-updating is flat in base capability: when the task-solving agent is fixed and the evolver model is varied, models from different capability tiers produce harness updates that lead to surprisingly similar gains, and no evolver dominates across all substrates. Even the Qwen3.5-9B evolver produces harness updates whose downstream gains match those of Claude Opus 4.6, despite a large gap in base capability.

> Harness-benefit is non-monotonic across base-capability tiers, with mid-tier models (e.g., GPT-OSS-120B) benefiting most from updated harness, and strong-tier models (e.g., Claude Opus 4.6) reaching the performance ceiling and benefiting less. These findings suggest investing capability budget in the task-solving agent rather than the evolver.