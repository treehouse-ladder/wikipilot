---
fetched_at: &id001 2026-06-17
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 06be4ecd870fe99ee996fd0859e5b7bacaed80fc4fcf37a9038fca9078128293
sources: []
title: 'Bayesian-Agent: Posterior-Guided Skill Evolution for LLM Agent Harnesses'
topic: agentic-coding
url: https://arxiv.org/abs/2606.08348
---

## Excerpts

> Bayesian-Agent is a native and cross-harness framework that treats reusable skills and SOPs as hypotheses about whether a frozen model will succeed under a particular prompt, context, and harness environment.

> Bayesian-Agent records verified trajectory evidence, maintains a feature-conditioned categorical posterior over each skill, and maps posterior state into inspectable actions such as patch, split, compress, retire, and explore. Model-facing prompts receive executable guardrails and failure-mode patches, while posterior summaries remain available for audit.

> These assets can improve task execution without changing model weights, but they are often revised by heuristic reflection or by reusing observed successes and failures as if counts alone were reliable belief.