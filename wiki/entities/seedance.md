---
title: "Seedance"
kind: entity
aliases: ["Seedance by ByteDance", "seed.bytedance.com"]
sources:
  - "[[seedance-wins-artificial-analysis-image-to-video-with-audio-output-benchmark-1-a7869d54]]"
  - "[[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]"
  - "[[introducing-seedance-2-5-78d1ddb7]]"
last_updated: 2026-10-26
last_verified: 2026-10-26
freshness_window_days: 30
profile: tool
modality: video
tasks: ["image-to-video", "text-to-video"]
vendor: "ByteDance"
model_ids: ["seedance"]
access: ["api"]
open_weights_license: unknown
hardware_floor: unknown
pricing: "AA-measured $9.07/min (Seedance 2.0 720p, audio I2V board) to $22.45/min (Seedance 2.0, AA-Video-I2V v1.1) (2026-10-26)"
pricing_source: "[[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]"
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[seedance-wins-artificial-analysis-image-to-video-with-audio-output-benchmark-1-a7869d54]]"
last_release: unknown
arena_rank: ["Artificial Analysis Image-to-Video (audio output, Seedance 2.0 720p): #1, Elo 1197 (2026-10-26)"]
arena_rank_source: ["[[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]"]
---

# Seedance

## Summary

Seedance is ByteDance's video generation model, supporting image-to-video and text-to-video with synchronized audio output [[seedance-wins-artificial-analysis-image-to-video-with-audio-output-benchmark-1-a7869d54]]. As of October 26, 2026, Seedance 2.0 720p ranks #1 on the Artificial Analysis Image-to-Video audio-output board (Elo 1197, AA-measured $9.07/min) and Seedance 2.0 is listed at $22.45/min on the AA-Video-I2V v1.1 (no-audio) board [[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]. Seedance 2.5 (announced 2026-10-26) generates 30-second audio-video clips in a single pass with multi-round extension and up to 50 reference inputs [[introducing-seedance-2-5-78d1ddb7]].

> Seedance by ByteDance ranks first on the Artificial Analysis Image-to-Video (audio output) benchmark as of October 25, 2026. Available via the Seedance API. Supports image-to-video and text-to-video with synchronized audio output.

> Dreamina Seedance 2.0 720p currently leads among Image to Video models with audio output in the Artificial Analysis Image to Video Arena with an Elo score of 1197. In that table, it is listed at $9.07 /min. [[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]

> Seedance 2.5 is able to generate high-quality, 30-second audio-video clips in a single pass, with multi-round extensions. Seedance 2.5 features one-take creation and flexible referencing, with up to 50 reference inputs. [[introducing-seedance-2-5-78d1ddb7]]

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-26)_

## Open questions

- [ ] Commercial-use terms — no ingested source states whether output may ship in a commercial game.
- [ ] Artificial Analysis text-to-video benchmark placement for Seedance 2.0 / 2.5.
- [ ] Seedance 2.5 API availability date and fal/Replicate endpoint ids.

## See also

- [[generative-media-models]]
