---
title: "Nano Banana 2.1"
kind: entity
aliases: ["Nano Banana 2.1", "nano-banana-2.1", "Gemini 3.6 Flash Image"]
sources:
  - "[[nano-banana-2-1-model-card-google-deepmind-2783cdec]]"
  - "[[nano-banana-2-1-text-to-image-api-on-fal-76f8d675]]"
last_updated: 2026-11-10
last_verified: 2026-11-10
freshness_window_days: 30
profile: tool
modality: image
tasks: ["text-to-image", "image-editing"]
vendor: "Google DeepMind"
model_ids: ["fal:google/nano-banana-2.1"]
access: ["api", "fal"]
open_weights_license: unknown
hardware_floor: unknown
pricing: "~$0.04/image at 1K, ~$0.06 at 2K, ~$0.13 at 4K resolution via fal (token-based: $35.294/M image output tokens) (2026-11-10)"
pricing_source: "[[nano-banana-2-1-text-to-image-api-on-fal-76f8d675]]"
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[nano-banana-2-1-model-card-google-deepmind-2783cdec]]"
last_release: 2026-10-06
arena_rank: []
arena_rank_source: []
---

# Nano Banana 2.1

## Summary

Nano Banana 2.1 is Google DeepMind's image generation + editing model "based on Gemini 3.6 Flash" [[nano-banana-2-1-model-card-google-deepmind-2783cdec]]. Per the model card it "outperforms previous Nano Banana models to deliver better visual design, mask-based editing, subject consistency, and more natural-looking images" [[nano-banana-2-1-model-card-google-deepmind-2783cdec]]. It is a distinct, newer model from [[nano-banana]] (Nano Banana 2 Lite = `gemini-3.1-flash-image`, built on Gemini 3.1 Flash); the DeepMind model-cards index lists Nano Banana 2.1 as updated 2026-10-06 [[nano-banana-2-1-model-card-google-deepmind-2783cdec]]. An Artificial Analysis snapshot places it at approximately Elo 1176 on AA-Image-T2I v2.1 and Elo 1152 on AA-Image-Editing v2.1 — below the current image leader GPT Image 2.5 Sunburst — but captures conflict and the exact standing needs confirmation against the live board [[nano-banana-2-1-model-card-google-deepmind-2783cdec]].

**Pricing on fal confirmed (2026-11-10).** Nano Banana 2.1 is available on fal as `google/nano-banana-2.1` (model id: `fal:google/nano-banana-2.1`). fal bills on a per-token basis: image output tokens cost $35.294/M. In practice, a 16:9 text-to-image output at medium thinking costs approximately $0.04 at 1K resolution, $0.06 at 2K, and $0.13 at 4K per image [[nano-banana-2-1-text-to-image-api-on-fal-76f8d675]]. Exact Gemini API model id and commercial-use terms remain unstated.

> Nano Banana 2.1 is available on fal (google/nano-banana-2.1). Through fal's API, billing is per token: 1.764 USD per million input tokens, 8.823 USD per million text and thinking output tokens, and 35.294 USD per million image output tokens. For one 16:9 text-to-image output with a short prompt at medium thinking, fal's billing came to about 0.0396 USD at 1K, 0.0593 USD at 2K, and 0.1335 USD at 4K per image. [[nano-banana-2-1-text-to-image-api-on-fal-76f8d675]]

> Nano Banana 2.1 is based on Gemini 3.6 Flash. [[nano-banana-2-1-model-card-google-deepmind-2783cdec]]

> It outperforms previous Nano Banana models to deliver better visual design, mask-based editing, subject consistency, and more natural-looking images. [[nano-banana-2-1-model-card-google-deepmind-2783cdec]]

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-11-10)_

## Open questions

- [ ] Exact Gemini API model id for Nano Banana 2.1 (`gemini-3.6-flash-image`?) — not stated in the ingested model card.
- [ ] Per-image pricing directly on the Gemini API (fal pricing confirmed 2026-11-10; Gemini API native pricing unknown).
- [ ] Commercial-use terms for shipping generated assets in a commercial game.
- [ ] Confirmed Artificial Analysis AA-Image-T2I / AA-Image-Editing Elo against a dated live snapshot (captures conflict: ~1176 T2I, ~1152 editing).

## See also

- [[generative-media-models]]
- [[nano-banana]]
- [[gpt-image]]
