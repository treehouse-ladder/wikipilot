---
fetched_at: &id001 2026-05-21
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 20e9d0e734a8fb4e4f9a2ddd9aead33317e737c2b751bc601b6bec0173ab5237
sources: []
title: Qwen3.6-27B on Hugging Face
topic: frontier-models
url: https://huggingface.co/Qwen/Qwen3.6-27B
---

## Excerpts

> The model has a context length of 262,144 tokens natively and is extensible up to 1,010,000 tokens.

> By default, only the thinking blocks generated in handling the latest user message is retained, resulting in a pattern commonly as interleaved thinking. The model supports a preserve_thinking option that can be enabled when making API calls to maintain full reasoning context across multiple turns.

> Maintaining full reasoning context can enhance decision consistency and, in many cases, reduce overall token consumption by minimizing redundant reasoning, which is particularly beneficial for agent scenarios.