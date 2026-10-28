---
title: "Seedance"
kind: entity
aliases: ["Seedance by ByteDance", "seed.bytedance.com"]
sources:
  - "[[seedance-wins-artificial-analysis-image-to-video-with-audio-output-benchmark-1-a7869d54]]"
  - "[[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]"
  - "[[introducing-seedance-2-5-78d1ddb7]]"
  - "[[seedance-2-5-us-image-to-video-api-on-fal-f520e761]]"
last_updated: 2026-10-28
last_verified: 2026-10-28
freshness_window_days: 30
profile: tool
modality: video
tasks: ["image-to-video", "text-to-video"]
vendor: "ByteDance"
model_ids: ["seedance"]
access: ["api", "fal"]
open_weights_license: unknown
hardware_floor: unknown
pricing: "Seedance 2.5 on fal (bytedance/seedance-2.5/us), billed by output tokens: ~$0.2205/s (480p), ~$0.4730/s (720p), ~$1.164/s (1080p), $0.0214/1K tokens 480p-720p (2026-10-28); Seedance 2.0 AA-measured $9.07-$22.45/min"
pricing_source: "[[seedance-2-5-us-image-to-video-api-on-fal-f520e761]]"
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[seedance-2-5-us-image-to-video-api-on-fal-f520e761]]"
last_release: unknown
arena_rank: ["Artificial Analysis Image-to-Video (audio output, Seedance 2.0 720p): #1, Elo 1197 (2026-10-26)"]
arena_rank_source: ["[[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]"]
---

# Seedance

## Summary

Seedance is ByteDance's video generation model, supporting image-to-video and text-to-video with synchronized audio output [[seedance-wins-artificial-analysis-image-to-video-with-audio-output-benchmark-1-a7869d54]]. As of October 26, 2026, Seedance 2.0 720p ranks #1 on the Artificial Analysis Image-to-Video audio-output board (Elo 1197, AA-measured $9.07/min) and Seedance 2.0 is listed at $22.45/min on the AA-Video-I2V v1.1 (no-audio) board [[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]. Seedance 2.5 (announced 2026-10-26) generates 30-second audio-video clips in a single pass with multi-round extension and up to 50 reference inputs [[introducing-seedance-2-5-78d1ddb7]].

Seedance 2.5 is now live on fal under `bytedance/seedance-2.5/us`, billed by output tokens at $0.0214/1K tokens for 480p/720p, yielding roughly $0.2205/s (480p), $0.4730/s (720p), and $1.164/s (1080p) — no subscription or minimum required [[seedance-2-5-us-image-to-video-api-on-fal-f520e761]].

> Seedance by ByteDance ranks first on the Artificial Analysis Image-to-Video (audio output) benchmark as of October 25, 2026. Available via the Seedance API. Supports image-to-video and text-to-video with synchronized audio output.

> Dreamina Seedance 2.0 720p currently leads among Image to Video models with audio output in the Artificial Analysis Image to Video Arena with an Elo score of 1197. In that table, it is listed at $9.07 /min. [[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]

> Seedance 2.5 is able to generate high-quality, 30-second audio-video clips in a single pass, with multi-round extensions. Seedance 2.5 features one-take creation and flexible referencing, with up to 50 reference inputs. [[introducing-seedance-2-5-78d1ddb7]]

> For 480p, your request will cost roughly $0.2205 per second of generated video, for 720p, you will be charged roughly $0.4730 per second of generated video, and for 1080p, roughly $1.164 per second of generated video. You're charged $0.0214 per 1,000 tokens at both 480p and 720p, with no subscription and no minimum. [[seedance-2-5-us-image-to-video-api-on-fal-f520e761]]

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-26)_

## Open questions

- [ ] Commercial-use terms — no ingested source states whether output may ship in a commercial game.
- [ ] Artificial Analysis text-to-video benchmark placement for Seedance 2.0 / 2.5.
- [x] Seedance 2.5 API availability date and fal/Replicate endpoint ids — **resolved 2026-10-28**: `bytedance/seedance-2.5/us` live on fal [[seedance-2-5-us-image-to-video-api-on-fal-f520e761]].

## See also

- [[generative-media-models]]
