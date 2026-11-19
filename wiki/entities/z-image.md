---
title: "Z-Image"
kind: entity
aliases: ["Z-Image-Turbo", "Z-Image Turbo", "z-image-turbo", "Tongyi-MAI/Z-Image", "Z Image"]
sources:
  - "[[tongyi-mai-z-image-turbo-hugging-face-4542559f]]"
last_updated: 2026-11-19
last_verified: 2026-11-19
freshness_window_days: 30
profile: tool
modality: image
tasks: ["text-to-image"]
vendor: "Alibaba / Tongyi-MAI"
model_ids: ["z-image-turbo", "z-image"]
access: ["open-weights"]
open_weights_license: "apache-2.0"
hardware_floor: "16 GB VRAM"
pricing: unknown
pricing_source: null
commercial_use: "Apache-2.0 (commercial use allowed)"
commercial_use_source: "[[tongyi-mai-z-image-turbo-hugging-face-4542559f]]"
status: active
status_source: "[[tongyi-mai-z-image-turbo-hugging-face-4542559f]]"
last_release: unknown
arena_rank: []
arena_rank_source: []
---

# Z-Image

## Summary

**Z-Image** is a 6B-parameter image-generation model family from Alibaba's Tongyi-MAI team, available as open weights under the Apache-2.0 license [[tongyi-mai-z-image-turbo-hugging-face-4542559f]]. The family currently has four variants, anchored by **Z-Image-Turbo** (a distilled version) and **Z-Image** (the foundation model).

**Z-Image-Turbo** is the efficiency tier — it matches or exceeds leading competitors using only **8 NFEs (Number of Function Evaluations)**, achieving sub-second inference latency on enterprise-grade H800 GPUs and fitting comfortably within **16 GB VRAM** on consumer devices [[tongyi-mai-z-image-turbo-hugging-face-4542559f]]. Its capabilities include photorealistic image generation, bilingual text rendering (English and Chinese), and robust instruction adherence.

> Z-Image-Turbo — A distilled version of Z-Image that matches or exceeds leading competitors with only 8 NFEs (Number of Function Evaluations). It offers sub-second inference latency on enterprise-grade H800 GPUs and fits comfortably within 16G VRAM consumer devices. It excels in photorealistic image generation, bilingual text rendering (English & Chinese), and robust instruction adherence. [[tongyi-mai-z-image-turbo-hugging-face-4542559f]]

**Z-Image** (foundation) focuses on high-quality generation, rich aesthetics, strong diversity, and controllability — suited for creative generation, fine-tuning, and downstream development [[tongyi-mai-z-image-turbo-hugging-face-4542559f]].

> Z-Image — The foundation model behind Z-Image-Turbo. Z-Image focuses on high-quality generation, rich aesthetics, strong diversity, and controllability, well-suited for creative generation, fine-tuning, and downstream development. [[tongyi-mai-z-image-turbo-hugging-face-4542559f]]

Both models use a **Scalable Single-Stream DiT (S3-DiT)** architecture — text, visual semantic tokens, and image VAE tokens are concatenated at the sequence level as a unified input stream, maximizing parameter efficiency compared to dual-stream approaches [[tongyi-mai-z-image-turbo-hugging-face-4542559f]].

> We adopt a Scalable Single-Stream DiT (S3-DiT) architecture. In this setup, text, visual semantic tokens, and image VAE tokens are concatenated at the sequence level to serve as a unified input stream, maximizing parameter efficiency compared to dual-stream approaches. [[tongyi-mai-z-image-turbo-hugging-face-4542559f]]

The Apache-2.0 license makes commercial use permitted, including for game-asset pipelines. The 16 GB VRAM floor puts it within reach of a standard gaming workstation. No independent quality-arena placements (AA-Image, DesignArena) are known yet.

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-11-19)_

## Open questions

- [ ] Independent quality-arena placement (AA-Image-T2I, DesignArena) — not in ingested sources.
- [ ] API/cloud access path (fal, Replicate, etc.) — model card only shows Hugging Face open weights.
- [ ] Exact release date — not stated in ingested sources.
- [ ] Per-image pricing if any cloud endpoint exists.
- [ ] Does the 16 GB VRAM floor apply to Z-Image-Turbo at full precision, or to a quantized variant?

## See also

- [[generative-media-models]]
- [[image-tools]]
- [[flux]]
- [[minimax-h3-image]]
- [[qwen-image]]
