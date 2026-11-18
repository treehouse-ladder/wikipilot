---
title: "Nano Banana Pro"
kind: entity
aliases: ["Gemini 3 Pro Image", "nano-banana-pro", "Nano Banana Pro (Gemini 3 Pro Image)"]
profile: tool
modality: image
tasks: ["text-to-image", "image-editing"]
vendor: "Google DeepMind"
model_ids: ["gemini-3-pro-image", "fal:fal-ai/nano-banana-pro"]
access: ["api", "fal", "web"]
open_weights_license: "n/a"
hardware_floor: "n/a"
pricing: "fal: $0.15/image (1K/2K), $0.30/image (4K); +$0.015/request Search grounding (2026-11-18)"
pricing_source: "[[google-nano-banana-pro-advanced-ai-image-generator-and-editor-653e22b0]]"
commercial_use: "unknown"
commercial_use_source: null
status: "active"
status_source: "[[nano-banana-pro-gemini-3-pro-image-model-from-google-deepmind-db47f003]]"
last_release: 2026-11-18
arena_rank: ["Artificial Analysis AA-Image-T2I v2.1: ~rank 16-19, Elo ~1119 (2026-11-18, snapshots conflict)"]
arena_rank_source: ["[[nano-banana-pro-gemini-3-pro-image-model-elo-generation-time-and-price-analysis-2eaaaa75]]"]
sources: ["[[nano-banana-pro-gemini-3-pro-image-model-from-google-deepmind-db47f003]]", "[[developers-can-build-with-nano-banana-pro-gemini-3-pro-image-499efe55]]", "[[google-nano-banana-pro-advanced-ai-image-generator-and-editor-653e22b0]]", "[[nano-banana-pro-gemini-3-pro-image-model-elo-generation-time-and-price-analysis-2eaaaa75]]"]
last_updated: 2026-11-18
last_verified: 2026-11-18
freshness_window_days: 30
---

# Nano Banana Pro

## Summary

Nano Banana Pro (also called Gemini 3 Pro Image, model ID `gemini-3-pro-image`) is Google DeepMind's most advanced image generation and editing model as of November 2026, built on Gemini 3 Pro [[nano-banana-pro-gemini-3-pro-image-model-from-google-deepmind-db47f003]]. It is positioned as best-in-class for rendering correctly spelled, legible, multilingual text directly within images, and supports combining up to 14 input images while maintaining the consistency and resemblance of up to 5 people [[nano-banana-pro-gemini-3-pro-image-model-from-google-deepmind-db47f003]]. Output resolutions include 1K, 2K, and 4K.

Nano Banana Pro is distinct from the earlier [[nano-banana]] (Nano Banana 2 Lite) and [[nano-banana-2-1]] (Nano Banana 2.1) entities already tracked in this wiki.

For developers, it is accessible via the Gemini API and Google AI Studio in paid preview, as well as Vertex AI for enterprise; it optionally adds Google Search grounding for real-time web-data-driven outputs [[developers-can-build-with-nano-banana-pro-gemini-3-pro-image-499efe55]]. On fal, pricing is $0.15/image for standard 1K/2K outputs, $0.30/image for 4K (same rate for generation and editing), plus $0.015/request when Search grounding is activated [[google-nano-banana-pro-advanced-ai-image-generator-and-editor-653e22b0]].

Measured benchmark performance (Artificial Analysis) places Nano Banana Pro at approximately Elo 1119 on AA-Image-T2I v2.1 (rank ~16-19 out of ~50+ models), well below the board leader [[gpt-image]] (GPT Image 2.6 Sunburst, max, ~Elo 1261) [[nano-banana-pro-gemini-3-pro-image-model-elo-generation-time-and-price-analysis-2eaaaa75]]. AA snapshots conflict and a clean, single-dated reading is needed before any definitive ranking. Nano Banana Pro does **not** displace the current measured image-quality leaders.

> Nano Banana Pro, built on Gemini 3 Pro, is our most advanced image generation and editing model. It is the best model for creating images with correctly rendered and legible text directly in the image, including multilingual text. Nano Banana Pro can combine up to 14 input images and maintain the consistency and resemblance of up to 5 people. [[nano-banana-pro-gemini-3-pro-image-model-from-google-deepmind-db47f003]]

> Standard 1K and 2K outputs are charged at the base rate of 0.15 US dollars per image. 4K outputs are charged at double the standard rate (0.30 US dollars per image). The same rate applies to generation and editing. If web search is used during generation, an additional 0.015 US dollars is added per request. [[google-nano-banana-pro-advanced-ai-image-generator-and-editor-653e22b0]]

> Nano Banana Pro (Gemini 3 Pro Image) scores approximately 1119 Elo on the Artificial Analysis AA-Image-T2I v2.1 text-to-image leaderboard, in roughly 16th to 19th place, on 15,862 samples. [[nano-banana-pro-gemini-3-pro-image-model-elo-generation-time-and-price-analysis-2eaaaa75]]

## Disputes

## Open questions

- [ ] Nano Banana Pro clean, single-dated AA-Image-T2I v2.1 / AA-Image-Editing v2.1 Elo — snapshots conflict (~1119 mid-board on one read) and are not cleanly comparable to GPT Image 2.6 Sunburst (~1261); confirm against a single dated snapshot before any leader reassessment [[nano-banana-pro-gemini-3-pro-image-model-elo-generation-time-and-price-analysis-2eaaaa75]].
- [ ] Nano Banana Pro native Gemini API per-image / per-token pricing (only fal per-image billing of $0.15 at 1K/2K, $0.30 at 4K is sourced) and commercial-use / licensing terms for shipping generated assets in a commercial game [[developers-can-build-with-nano-banana-pro-gemini-3-pro-image-499efe55]].

## See also

- [[generative-media-models]]
- [[image-tools]]
- [[nano-banana]]
- [[nano-banana-2-1]]
- [[gpt-image]]
