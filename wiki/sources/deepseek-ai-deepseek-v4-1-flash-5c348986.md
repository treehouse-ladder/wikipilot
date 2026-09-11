---
fetched_at: &id001 2026-09-11
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 5c348986a15182f2f224ee2c5a6783ea3639c49ff1a68a3a3897f524fb0853e2
sources: []
title: deepseek-ai/DeepSeek-V4.1-Flash
topic: frontier-models
url: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
---

## Excerpts

> DeepSeek-V4.1-Flash is a multimodal Mixture-of-Experts (MoE) model with 552B backbone parameters and support for contexts of up to one million tokens. The model activates only 8B parameters per token during prefill and 16B during decode.

> DeepSeek-V4.1-Flash adopts a Causal Encoder-Decoder (CED) architecture: a 40-layer Transformer organized as a 20-layer causal encoder followed by a 20-layer decoder. It has 384 routed experts with 1 shared and 6 routed per token.

> The model supports a continuously controllable reasoning effort setting (integer 1-100) that trades inference cost for accuracy.

> Tests by multiple parties put the open-weight model ahead of its much larger DeepSeek-V4-Pro on performance, cost, speed and total runtime.