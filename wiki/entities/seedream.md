---
title: "Seedream 5.5"
kind: entity
aliases: ["Seedream", "Seedream 5.0 Pro", "seedream-5.0-pro", "Seedream 5.0"]
sources:
  - "[[introducing-seedream-5-0-pro-it-understands-design-fbaad63d]]"
  - "[[seedream-5-0-pro-api-multimodal-ai-image-model-12934420]]"
  - "[[more-realistic-images-more-stable-editing-across-100-rounds-introducing-seedream-5-5-3d7aaab5]]"
  - "[[seedream-5-5-text-to-image-api-on-fal-adff6dde]]"
last_updated: 2026-11-14
last_verified: 2026-11-14
freshness_window_days: 30
profile: tool
modality: image
tasks: ["text-to-image", "image-editing", "infographic-generation"]
vendor: "ByteDance"
model_ids: ["fal:fal-ai/seedream/v5.0/pro", "fal:bytedance/seedream/v5.5/text-to-image"]
access: ["api", "fal"]
open_weights_license: unknown
hardware_floor: unknown
pricing: "Seedream 5.5: $0.03/image at 1K or 1.5K, $0.0405/image at 2K (fal, 2026-11-14); Seedream 5.0 Pro: $0.0675/image up to 1536×1536, $0.135/image above (fal); Lite $0.035/image (up to 3072×3072), Flash $0.027/image (2026-11-10)"
pricing_source: "[[seedream-5-5-text-to-image-api-on-fal-adff6dde]]"
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[more-realistic-images-more-stable-editing-across-100-rounds-introducing-seedream-5-5-3d7aaab5]]"
last_release: 2026-11-14
arena_rank: []
arena_rank_source: []
---

# Seedream 5.5

## Summary

Seedream 5.0 Pro is ByteDance's multimodal image creation model, with headline features of dense infographic generation, interactive precision editing, layer separation, and multilingual text rendering in up to 14 languages at up to 2048×2048 resolution [[introducing-seedream-5-0-pro-it-understands-design-fbaad63d]]. ByteDance notes there is still room to improve in finer-grained text rendering and pixel-level editing consistency [[introducing-seedream-5-0-pro-it-understands-design-fbaad63d]].

> Seedream 5.0 Pro is ByteDance's multimodal image creation model. Its headline features are dense infographic generation, interactive precision editing, layer separation, and multilingual text rendering. [[introducing-seedream-5-0-pro-it-understands-design-fbaad63d]]

> Seedream 5.0 Pro renders native text in up to 14 languages and outputs up to 2048x2048. ByteDance notes there is still room to improve in finer-grained text rendering and pixel-level editing consistency. [[introducing-seedream-5-0-pro-it-understands-design-fbaad63d]]

Seedream 5.0 Pro is available on fal at $0.0675/image for images up to 1536×1536 and $0.135/image above that [[seedream-5-0-pro-api-multimodal-ai-image-model-12934420]]. Lighter variants are also on fal: Seedream 5.0 Lite at $0.035/image (up to 3072×3072) and Seedream 5.0 Flash at $0.027/image [[seedream-5-0-pro-api-multimodal-ai-image-model-12934420]].

> fal describes Seedream 5.0 Pro as ByteDance's flagship text-to-image model. On fal, text-to-image pricing is 0.0675 USD per image up to 1536x1536 and 0.135 USD per image above that. fal also lists Seedream 5.0 Lite at 0.035 USD per image for text-to-image (up to 3072x3072) and a Seedream 5.0 Flash variant at 0.027 USD per image. [[seedream-5-0-pro-api-multimodal-ai-image-model-12934420]]

**Seedream 5.5 (2026-11-14)** introduces native RGBA image generation (full and partial transparency) and pixel-level multi-turn editing stable across 100 successive rounds, with leading text structure and text-to-image realism compared to other major models [[more-realistic-images-more-stable-editing-across-100-rounds-introducing-seedream-5-5-3d7aaab5]]. A Pro version of the 5.5 series is forthcoming. On fal, Seedream 5.5 is priced at $0.03/image at 1K or 1.5K resolution and $0.0405/image at 2K [[seedream-5-5-text-to-image-api-on-fal-adff6dde]].

> Seedream 5.5 introduces native RGBA generation, producing images with full and partial transparency. Its multi-turn editing preserves unedited regions at the pixel level and reduces detail loss and image degradation across successive edits, supporting work on the same image across 100 rounds. [[more-realistic-images-more-stable-editing-across-100-rounds-introducing-seedream-5-5-3d7aaab5]]

> Pricing on fal is 0.03 USD per image at 1K or 1.5K resolution, and 0.0405 USD per image at 2K. [[seedream-5-5-text-to-image-api-on-fal-adff6dde]]

_no contradictions or gaps known yet (last reviewed: 2026-11-14)_

## Disputes

## Open questions

- [ ] Commercial-use terms for game-shippable outputs — not stated in ingested sources.
- [ ] Arena placement on Artificial Analysis or other image benchmarks.
- [ ] Whether Seedream 5.0 Pro is available directly on a ByteDance/Seed API (beyond fal).

## See also

- [[generative-media-models]]
