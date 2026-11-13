---
title: "MiniMax H3-Image"
kind: entity
aliases: ["MiniMax H3 Image", "H3-Image", "MiniMaxAI/MiniMax-H3-Image"]
sources:
  - "[[minimax-h3-image-bringing-4k-image-generation-into-the-10-second-era-0e365028]]"
  - "[[minimax-h3-image-4k-ai-image-generator-and-editor-4b0c4b72]]"
last_updated: 2026-11-13
last_verified: 2026-11-13
freshness_window_days: 30
profile: tool
modality: image
tasks: ["text-to-image", "reference-based-generation", "image-editing"]
vendor: "MiniMax"
model_ids: ["MiniMaxAI/MiniMax-H3-Image"]
access: ["api", "open-weights", "fal"]
open_weights_license: "MiniMax-H3-Image Community License Agreement"
hardware_floor: unknown
pricing: "API: ~$0.022/image at 1K, ~$0.023 at 2K, ~$0.069 at 4K; launch-week 50% off 4K brings it to ~$0.034/image (2026-11-13)"
pricing_source: "[[minimax-h3-image-4k-ai-image-generator-and-editor-4b0c4b72]]"
commercial_use: "open-weights: free for research/personal/commercial within license terms; revenue-above-threshold and hosted API services require separate commercial license from MiniMax (2026-11-13)"
commercial_use_source: "[[minimax-h3-image-4k-ai-image-generator-and-editor-4b0c4b72]]"
status: active
status_source: "[[minimax-h3-image-bringing-4k-image-generation-into-the-10-second-era-0e365028]]"
last_release: unknown
arena_rank: []
arena_rank_source: []
---

# MiniMax H3-Image

## Summary

MiniMax H3-Image is a 33.1B-parameter diffusion transformer distilled to 6 sampling steps with no classifier-free guidance [[minimax-h3-image-bringing-4k-image-generation-into-the-10-second-era-0e365028]]. It generates images at up to 4K (4096 × 4096) resolution in under 10 seconds and accepts up to 16 reference images for reference-based generation and image editing [[minimax-h3-image-bringing-4k-image-generation-into-the-10-second-era-0e365028]]. The model handles text-to-image, reference-based generation, and image editing from a unified API.

> H3-Image can produce a 4K (4096 x 4096) image in under 10 seconds and accepts up to 16 reference images. [[minimax-h3-image-bringing-4k-image-generation-into-the-10-second-era-0e365028]]

> H3-Image is a 33.1B-parameter diffusion transformer distilled to 6 sampling steps with no classifier-free guidance. [[minimax-h3-image-bringing-4k-image-generation-into-the-10-second-era-0e365028]]

H3-Image is available on the MiniMax API Platform, MiniMax Code (via API), Hailuo AI (web), and on fal.ai; open weights are released on Hugging Face under the MiniMax-H3-Image Community License Agreement [[minimax-h3-image-bringing-4k-image-generation-into-the-10-second-era-0e365028]] [[minimax-h3-image-4k-ai-image-generator-and-editor-4b0c4b72]]. The community license permits free use for research, personal, and commercial creation within its terms; hosted API services and revenue above a threshold require separate commercial licensing from MiniMax [[minimax-h3-image-4k-ai-image-generator-and-editor-4b0c4b72]]. Community GGUF and low-VRAM quantizations are also available on Hugging Face.

> H3-Image is available on the MiniMax API Platform, MiniMax Code, and Hailuo AI, and the open weights are released on Hugging Face under the MiniMax-H3-Image Community License Agreement. [[minimax-h3-image-bringing-4k-image-generation-into-the-10-second-era-0e365028]]

API pricing (as of launch, 2026-11-13): ~$0.022 per image at 1K resolution, ~$0.023 at 2K, ~$0.069 at 4K, with a limited-time 50% launch discount bringing 4K to ~$0.034 per image [[minimax-h3-image-4k-ai-image-generator-and-editor-4b0c4b72]]. H3-Image has not yet appeared on any third-party benchmark or arena board.

> MiniMax's official pricing lists H3-Image standard text-to-image at about $0.022 per image at 1K, about $0.023 at 2K, and about $0.069 at 4K, with a limited-time 50 percent launch discount bringing 4K to about $0.034 per image. [[minimax-h3-image-4k-ai-image-generator-and-editor-4b0c4b72]]

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-11-13)_

## Open questions

- [ ] Does H3-Image appear on the Artificial Analysis T2I v2.1 board, and if so at what Elo — the existing top-of-board is GPT Image 2.5 Sunburst (Elo 1196)?
- [ ] What is the exact revenue threshold in the community license beyond which commercial use requires a separate MiniMax license?
- [ ] Hardware floor for running the 33.1B open-weights model (VRAM requirement for quantized vs. BF16 inference)?
- [ ] Exact release date for `last_release` (sources carry no ISO date, only launch-week pricing context).

## See also

- [[generative-media-models]]
- [[minimax-h3]]
- [[image-tools]]
