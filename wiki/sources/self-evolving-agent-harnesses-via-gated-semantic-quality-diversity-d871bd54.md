---
fetched_at: &id001 2026-07-27
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: d871bd54e0d4a5c2a3e457fc8d32733faa01a338c7b121f38608573edafb9df7
sources: []
title: Self-Evolving Agent Harnesses via Gated Semantic Quality-Diversity
topic: agentic-coding
url: https://arxiv.org/abs/2607.13683
---

## Excerpts

> An LLM agent's real-task performance is shaped as much by the harness around its model as by the frozen model itself: its prompts, injected knowledge, runtime control, and configuration. In deployment the harness is often the only lever available, so improving it automatically is the natural way to raise performance without touching the weights.

> The hard part is not generating changes but knowing which one truly helped. Self-generated feedback is noisy, and an apparent gain can be a measurement artifact or an edit that merely overfits the tasks it was tuned on.

> We present a self-evolving agent-harness framework that separates proposing changes from crediting them: a language model diagnoses failures and proposes patches, while all sampling, measurement, and significance testing are owned by deterministic code.

> Across seven domains from three sources (terminal-bench-2, the EvoAgentBench suite, and AppWorld), the train-selected harness's credited sealed-test gains are +9 to +15.5 pp, retaining 86-147% of the training gain.