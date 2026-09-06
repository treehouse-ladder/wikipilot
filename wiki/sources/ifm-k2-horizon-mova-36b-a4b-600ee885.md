---
fetched_at: &id001 2026-09-06
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 600ee8857bfdd2e9cf5d31e1c513634801bc2869d0c137b32577f0efa5226b25
sources: []
title: IFM/K2-Horizon-MoVA-36B-A4B
topic: frontier-models
url: https://huggingface.co/IFM/K2-Horizon-MoVA-36B-A4B
---

## Excerpts

> Mixture-of-Values (MoVA) applies the same sparse routing philosophy as MoE, but inside the attention mechanism: the value projections are replaced by a learned pool of value experts, and only a small subset is activated per token. This lets the model store a much richer set of representational styles in the value space without paying for all of them at inference time, complementing the feed-forward MoE sparsity.

> K2-Horizon-MoVA-36B-A4B is a Mixture-of-Experts (MoE) model augmented with a novel Mixture-of-Values (MoVA) attention mechanism, storing approximately 36B parameters while activating only approximately 4B per token. On agentic and reasoning benchmarks it outscores open weight dense (approximately 30B model size) and MoE models up to 15x its size, and also performs competitively against closed frontier models.

> The source checkpoint supports a native context length of 524,288 tokens.