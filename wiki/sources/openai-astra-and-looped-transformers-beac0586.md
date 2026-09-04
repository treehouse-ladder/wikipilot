---
fetched_at: &id001 2026-09-04
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: beac058622d843a680ec156cfba0b6843fb7461c7dd4e381a13d606affaf320d
sources: []
title: OpenAI Astra and Looped Transformers
topic: frontier-models
url: https://sebastianraschka.com/blog/2026/openai-astra-looped-transformers.html
---

## Excerpts

> There is a lot of hype around OpenAI's Astra model being a 'recurrent depth or looped transformer'.

> The looped transformer idea is reusing layers in the transformer block. In the case of Nanbeige, the main idea is to reuse the same 22-layer stack (transformer block) twice instead of once. This effectively extends the 22-layer architecture to 44 layers without duplicating the weights.

> If a model uses more recurrent passes, it may need to generate fewer intermediate reasoning tokens, with more of its computation happening in latent activations that cannot be read as text.