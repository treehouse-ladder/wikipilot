---
title: "MiniMax H3-Image"
kind: entity
aliases: ["MiniMax H3 Image", "H3-Image", "MiniMaxAI/MiniMax-H3-Image"]
sources:
  - "[[minimax-h3-image-bringing-4k-image-generation-into-the-10-second-era-0e365028]]"
  - "[[minimax-h3-image-4k-ai-image-generator-and-editor-4b0c4b72]]"
  - "[[aa-image-t2i-v2-1-open-weights-leaderboard-top-ai-image-models-cbe6c9ba]]"
last_updated: 2026-11-14
last_verified: 2026-11-14
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
arena_rank: ["AA-Image-T2I v2.1 Open Weights: #1 (Elo 1067) (2026-11-14)"]
arena_rank_source: ["[[aa-image-t2i-v2-1-open-weights-leaderboard-top-ai-image-models-cbe6c9ba]]"]
---

# MiniMax H3-Image

## Summary

MiniMax H3-Image is a 33.1B-parameter diffusion transformer distilled to 6 sampling steps with no classifier-free guidance [[minimax-h3-image-bringing-4k-image-generation-into-the-10-second-era-0e365028]]. It generates images at up to 4K (4096 × 4096) resolution in under 10 seconds and accepts up to 16 reference images for reference-based generation and image editing [[minimax-h3-image-bringing-4k-image-generation-into-the-10-second-era-0e365028]]. The model handles text-to-image, reference-based generation, and image editing from a unified API.

> H3-Image can produce a 4K (4096 x 4096) image in under 10 seconds and accepts up to 16 reference images. [[minimax-h3-image-bringing-4k-image-generation-into-the-10-second-era-0e365028]]

> H3-Image is a 33.1B-parameter diffusion transformer distilled to 6 sampling steps with no classifier-free guidance. [[minimax-h3-image-bringing-4k-image-generation-into-the-10-second-era-0e365028]]

H3-Image is available on the MiniMax API Platform, MiniMax Code (via API), Hailuo AI (web), and on fal.ai; open weights are released on Hugging Face under the MiniMax-H3-Image Community License Agreement [[minimax-h3-image-bringing-4k-image-generation-into-the-10-second-era-0e365028]] [[minimax-h3-image-4k-ai-image-generator-and-editor-4b0c4b72]]. The community license permits free use for research, personal, and commercial creation within its terms; hosted API services and revenue above a threshold require separate commercial licensing from MiniMax [[minimax-h3-image-4k-ai-image-generator-and-editor-4b0c4b72]]. Community GGUF and low-VRAM quantizations are also available on Hugging Face.

> H3-Image is available on the MiniMax API Platform, MiniMax Code, and Hailuo AI, and the open weights are released on Hugging Face under the MiniMax-H3-Image Community License Agreement. [[minimax-h3-image-bringing-4k-image-generation-into-the-10-second-era-0e365028]]

API pricing (as of launch, 2026-11-13): ~$0.022 per image at 1K resolution, ~$0.023 at 2K, ~$0.069 at 4K, with a limited-time 50% launch discount bringing 4K to ~$0.034 per image [[minimax-h3-image-4k-ai-image-generator-and-editor-4b0c4b72]]. API pricing (as of launch, 2026-11-13): ~$0.022 per image at 1K resolution, ~$0.023 at 2K, ~$0.069 at 4K, with a limited-time 50% launch discount bringing 4K to ~$0.034 per image [[minimax-h3-image-4k-ai-image-generator-and-editor-4b0c4b72]].

> MiniMax's official pricing lists H3-Image standard text-to-image at about $0.022 per image at 1K, about $0.023 at 2K, and about $0.069 at 4K, with a limited-time 50 percent launch discount bringing 4K to about $0.034 per image. [[minimax-h3-image-4k-ai-image-generator-and-editor-4b0c4b72]]

As of 2026-11-14, MiniMax H3-Image ranks **#1 on the Artificial Analysis AA-Image-T2I v2.1 Open Weights Leaderboard** at Elo 1067, ahead of Alibaba Qwen-Image-2.1 and FLUX 3 Image Klein [[aa-image-t2i-v2-1-open-weights-leaderboard-top-ai-image-models-cbe6c9ba]]. Note: H3-Image does not appear on the main (all-models) T2I v2.1 board — this ranking is on the open-weights-only sub-leaderboard.

> MiniMax's H3-Image (Hugging Face) tops the open-weights text-to-image board at Elo 1067, with Alibaba's Qwen-Image-2.1 and Black Forest Labs' FLUX 3 Image Klein following close behind. [[aa-image-t2i-v2-1-open-weights-leaderboard-top-ai-image-models-cbe6c9ba]]

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-11-13)_

## Open questions

- [x] Does H3-Image appear on the Artificial Analysis T2I v2.1 board? — Confirmed on the **open-weights sub-board**: #1 at Elo 1067 [[aa-image-t2i-v2-1-open-weights-leaderboard-top-ai-image-models-cbe6c9ba]]. Not currently listed on the main (all-models) T2I v2.1 board.
- [ ] What is the exact revenue threshold in the community license beyond which commercial use requires a separate MiniMax license?
- [ ] Hardware floor for running the 33.1B open-weights model (VRAM requirement for quantized vs. BF16 inference)?
- [ ] Exact release date for `last_release` (sources carry no ISO date, only launch-week pricing context).

## See also

- [[generative-media-models]]
- [[minimax-h3]]
- [[image-tools]]
