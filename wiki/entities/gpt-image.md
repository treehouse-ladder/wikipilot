---
title: "GPT Image 2.5"
kind: entity
aliases: ["GPT Image 2.5 Flare", "GPT Image 2.5 Sunburst", "gpt-image-2.5-flare", "gpt-image-2.5-sunburst"]
sources:
  - "[[gpt-image-2-5-flare-and-sunburst-released-by-openai-cf34266e]]"
  - "[[aa-image-t2i-v2-1-leaderboard-top-ai-image-models-634924f7]]"
  - "[[text-to-image-leaderboard-best-ai-image-generators-ba150d9e]]"
  - "[[introducing-images-2-6-295354ff]]"
  - "[[gpt-image-2-6-sunburst-model-e5a487dd]]"
last_updated: 2026-11-05
last_verified: 2026-11-05
freshness_window_days: 30
profile: tool
modality: image
tasks: ["text-to-image", "image-editing", "inpainting", "outpainting"]
vendor: "OpenAI"
model_ids: ["gpt-image-2.5-flare", "gpt-image-2.5-sunburst", "gpt-image-2.6-flare", "gpt-image-2.6-sunburst"]
access: ["api"]
open_weights_license: unknown
hardware_floor: unknown
pricing: "gpt-image-2.6-sunburst $30/1M output tokens (API) (2026-11-04)"
pricing_source: "[[gpt-image-2-6-sunburst-model-e5a487dd]]"
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[gpt-image-2-5-flare-and-sunburst-released-by-openai-cf34266e]]"
last_release: 2026-11-04
arena_rank:
  - "Artificial Analysis Text-to-Image (AA-Image-T2I v2.1): #1, Elo 1196 (2026-10-26)"
  - "Artificial Analysis Image Editing (AA-Image-Editing v2.1): #1, Elo 1199 (2026-10-26)"
arena_rank_source:
  - "[[aa-image-t2i-v2-1-leaderboard-top-ai-image-models-634924f7]]"
  - "[[aa-image-t2i-v2-1-leaderboard-top-ai-image-models-634924f7]]"
---

# GPT Image 2.5

## Summary

GPT Image 2.5 ships as two variants: **Flare** (speed and cost priority) and **Sunburst** (quality priority), both available in the OpenAI API as `gpt-image-2.5-flare` and `gpt-image-2.5-sunburst` respectively [[gpt-image-2-5-flare-and-sunburst-released-by-openai-cf34266e]]. Both variants support editing, inpainting, and outpainting via the image edit endpoint in addition to generation. As of 2026-10-26, Sunburst leads both the Artificial Analysis text-to-image board (AA-Image-T2I v2.1, Elo 1196) and the image editing board (AA-Image-Editing v2.1, Elo 1199) [[aa-image-t2i-v2-1-leaderboard-top-ai-image-models-634924f7]]; on the arena.ai leaderboard (6M+ votes, Oct 7 2026 snapshot) Sunburst ranks #1 at 1425 Elo [[text-to-image-leaderboard-best-ai-image-generators-ba150d9e]].

> GPT Image 2.5 Flare and Sunburst are the latest image generation models from OpenAI, available in the API as gpt-image-2.5-flare and gpt-image-2.5-sunburst. Flare prioritizes speed and cost, Sunburst prioritizes quality. Both support editing, inpainting, and outpainting via the image edit endpoint.

> The text-to-image board has GPT Image 2.5 Sunburst (max) in first, at Elo 1196 across 13,586 comparisons. Flare (max) is second at 1190, and GPT Image 2 (high) is third at 1171. Sunburst also leads Artificial Analysis's image editing board, at Elo 1199. [[aa-image-t2i-v2-1-leaderboard-top-ai-image-models-634924f7]]

> The overall board, dated Oct 7, 2026 and built on 6M+ votes, puts GPT-Image-2.5 Sunburst first at 1425 (+/-7). GPT-Image-2.5 Flare is second (1398), and GPT-Image-2 (Medium) is third (1383). 82 models appear in that snapshot. [[text-to-image-leaderboard-best-ai-image-generators-ba150d9e]]

OpenAI released GPT Image 2.6 on 2026-11-04: `gpt-image-2.6-flare` and `gpt-image-2.6-sunburst` are available in the API, and Images 2.6 is live in ChatGPT and Codex [[introducing-images-2-6-295354ff]]. Sunburst is the quality-first variant with higher-quality generation and greater image consistency across edits; the developer model page prices `gpt-image-2.6-sunburst` at $30 per 1M output tokens [[gpt-image-2-6-sunburst-model-e5a487dd]]. This supersedes the GPT Image 2.5 (Flare/Sunburst) release as OpenAI's current image model (frontmatter updated with model_ids `gpt-image-2.6-flare` / `gpt-image-2.6-sunburst` and last_release 2026-11-04). GPT Image 2.5 Sunburst (max) remains #1 on the Artificial Analysis AA-Image-T2I v2.1 and AA-Image-Editing v2.1 boards; GPT Image 2.6 is not yet arena-ranked as of 2026-11-05 [[aa-image-t2i-v2-1-leaderboard-top-ai-image-models-634924f7]].

> GPT-Image-2.6 Sunburst and GPT-Image-2.6 Flare are available in the API. Images 2.6 is available in ChatGPT and Codex. [[introducing-images-2-6-295354ff]]

> Price: $30 per 1M output tokens. [[gpt-image-2-6-sunburst-model-e5a487dd]]

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-26)_

## Open questions

- [ ] Per-image pricing for Flare and Sunburst (2.5 variants) — no ingested source states a figure.
- [ ] Commercial-use terms — no ingested source states whether output may ship in a commercial game.
- [ ] GPT Image 2.6 commercial-use / licensing terms for game-shipping not stated in ingested sources.
- [ ] GPT Image 2.6 not yet on the AA image boards as of 2026-11-05.

## See also

- [[generative-media-models]]
