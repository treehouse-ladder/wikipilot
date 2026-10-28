---
title: "Wan 3.0"
kind: entity
aliases: ["Wan", "Wan 3", "Wan 3.0", "wan-3.0", "Alibaba Wan", "Wan 3.0 Prime"]
profile: tool
modality: video
tasks: ["text-to-video", "image-to-video", "video-editing"]
vendor: "Alibaba"
model_ids: ["fal:alibaba/wan-3.0", "fal:alibaba/wan-3.0-prime"]
access: ["api", "fal"]
open_weights_license: unknown
hardware_floor: unknown
pricing: "fal: $0.05/s (480p), $0.10/s (720p), $0.20/s (1080p); Wan 3.0 Prime $0.068/$0.14/$0.28 per s (2026-10-28)"
pricing_source: "[[wan-3-0-text-to-video-api-on-fal-581fd1f9]]"
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[wan-3-0-text-to-video-api-on-fal-581fd1f9]]"
last_release: unknown
arena_rank: ["Artificial Analysis Text-to-Video (AA-Video-T2V v2.1, with audio): #1, Elo 1174 (2026-10-28)", "Artificial Analysis Video Editing (AA-Video-Editing v1.1): #1, Elo 1198 (2026-10-28)"]
arena_rank_source: ["[[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]]", "[[aa-video-editing-v1-1-leaderboard-top-ai-video-models-1743cee9]]"]
sources: ["[[wan-3-0-text-to-video-api-on-fal-581fd1f9]]", "[[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]]", "[[aa-video-editing-v1-1-leaderboard-top-ai-video-models-1743cee9]]"]
last_updated: 2026-10-28
last_verified: 2026-10-28
freshness_window_days: 30
---

# Wan 3.0

## Summary

Wan 3.0 is Alibaba's text-to-video / image-to-video model, reachable on fal via `alibaba/wan-3.0` (text-to-video and image-to-video) and a higher-rate `alibaba/wan-3.0-prime` tier [[wan-3-0-text-to-video-api-on-fal-581fd1f9]]. As of 2026-10-28 it leads two Artificial Analysis video boards: #1 on text-to-video (AA-Video-T2V v2.1, with audio) at Elo 1174 [[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]] and #1 on video editing (AA-Video-Editing v1.1) at Elo 1198 [[aa-video-editing-v1-1-leaderboard-top-ai-video-models-1743cee9]]. fal prices it per second of output by resolution.

> Wan 3.0 on fal is priced at $0.05 per second at 480p, $0.10 per second at 720p, and $0.20 per second at 1080p. [[wan-3-0-text-to-video-api-on-fal-581fd1f9]]

> Wan 3.0 currently leads AA-Video-T2V v2.1 with an Elo score of 1174. [[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]]

> Wan 3.0 leads AA-Video-Editing v1.1 at Elo 1198, ahead of Dreamina Seedance 2.5 at 1155 and Hyperflow H3 at 1153. [[aa-video-editing-v1-1-leaderboard-top-ai-video-models-1743cee9]]

## Disputes

_none yet_

## Open questions

- [ ] Is Wan 3.0 released as open weights, and under what license / hardware floor?
- [ ] Commercial-use / licensing terms for shipping Wan 3.0 output in a commercial game.

## See also

- [[generative-media-models]]
- [[video-tools]]
- [[minimax-h3]]
- [[seedance]]
