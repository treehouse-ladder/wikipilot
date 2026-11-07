---
title: "Nano Banana 2.1"
kind: entity
aliases: ["Nano Banana 2.1", "nano-banana-2.1", "Gemini 3.6 Flash Image"]
sources:
  - "[[nano-banana-2-1-model-card-google-deepmind-2783cdec]]"
last_updated: 2026-11-07
last_verified: 2026-11-07
freshness_window_days: 30
profile: tool
modality: image
tasks: ["text-to-image", "image-editing"]
vendor: "Google DeepMind"
model_ids: []
access: ["api"]
open_weights_license: unknown
hardware_floor: unknown
pricing: unknown
pricing_source: null
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

Nano Banana 2.1 is Google DeepMind's image generation + editing model "based on Gemini 3.6 Flash" [[nano-banana-2-1-model-card-google-deepmind-2783cdec]]. Per the model card it "outperforms previous Nano Banana models to deliver better visual design, mask-based editing, subject consistency, and more natural-looking images" [[nano-banana-2-1-model-card-google-deepmind-2783cdec]]. It is a distinct, newer model from [[nano-banana]] (Nano Banana 2 Lite = `gemini-3.1-flash-image`, built on Gemini 3.1 Flash); the DeepMind model-cards index lists Nano Banana 2.1 as updated 2026-10-06 [[nano-banana-2-1-model-card-google-deepmind-2783cdec]]. An Artificial Analysis snapshot places it at approximately Elo 1176 on AA-Image-T2I v2.1 and Elo 1152 on AA-Image-Editing v2.1 — below the current image leader GPT Image 2.5 Sunburst — but captures conflict and the exact standing needs confirmation against the live board [[nano-banana-2-1-model-card-google-deepmind-2783cdec]]. Pricing, the exact Gemini API model id, and commercial-use terms are not stated in the model card.

> Nano Banana 2.1 is based on Gemini 3.6 Flash. [[nano-banana-2-1-model-card-google-deepmind-2783cdec]]

> It outperforms previous Nano Banana models to deliver better visual design, mask-based editing, subject consistency, and more natural-looking images. [[nano-banana-2-1-model-card-google-deepmind-2783cdec]]

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-11-07)_

## Open questions

- [ ] Exact Gemini API model id for Nano Banana 2.1 (`gemini-3.6-flash-image`?) — not stated in the ingested model card.
- [ ] Per-image / per-1K pricing on the Gemini API.
- [ ] Commercial-use terms for shipping generated assets in a commercial game.
- [ ] Confirmed Artificial Analysis AA-Image-T2I / AA-Image-Editing Elo against a dated live snapshot (captures conflict: ~1176 T2I, ~1152 editing).

## See also

- [[generative-media-models]]
- [[nano-banana]]
- [[gpt-image]]
