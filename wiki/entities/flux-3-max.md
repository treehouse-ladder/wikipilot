---
title: "FLUX 3 Max"
kind: entity
aliases: ["FLUX 3 Max", "flux-3-max", "BFL FLUX 3 Max"]
sources:
  - "[[flux-3-max-text-and-image-to-video-post-trained-by-fal-4991600a]]"
last_updated: 2026-10-26
last_verified: 2026-10-26
freshness_window_days: 30
profile: tool
modality: video
tasks: ["text-to-video", "image-to-video", "keyframes-to-video"]
vendor: "Black Forest Labs"
model_ids: ["fal:blackforestlabs/flux-3-max"]
access: ["api", "fal"]
open_weights_license: unknown
hardware_floor: unknown
pricing: "$0.085/s (all variants, via fal) (2026-10-26)"
pricing_source: "[[flux-3-max-text-and-image-to-video-post-trained-by-fal-4991600a]]"
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[flux-3-max-text-and-image-to-video-post-trained-by-fal-4991600a]]"
last_release: unknown
arena_rank: ["Artificial Analysis Image-to-Video (preliminary, vendor-reported): joint #1 tied with Seedance 2.5, Elo 1139 (2026-10-26)"]
arena_rank_source: ["[[flux-3-max-text-and-image-to-video-post-trained-by-fal-4991600a]]"]
---

# FLUX 3 Max

## Summary

FLUX 3 Max is a video model from Black Forest Labs' FLUX 3 foundation, post-trained by fal Research and served on fal across text-to-video, image-to-video and keyframes-to-video endpoints; text-to-video produces 5-20 second 720p clips with native audio, and the keyframes endpoint accepts up to ten keyframes [[flux-3-max-text-and-image-to-video-post-trained-by-fal-4991600a]]. fal lists $0.085/s for every variant and reports a *preliminary, vendor-reported* joint-#1 image-to-video tie with Seedance 2.5 (Elo 1139) on Artificial Analysis's provisional arena — a capability claim that the public AA I2V board does not independently corroborate as of this date (see Disputes) [[flux-3-max-text-and-image-to-video-post-trained-by-fal-4991600a]].

> FLUX 3 Max is a post-trained video model from fal Research, built with Black Forest Labs on the FLUX 3 foundation model. ... fal's model listing shows $0.085/s for each variant. [[flux-3-max-text-and-image-to-video-post-trained-by-fal-4991600a]]

## Disputes

- [[flux-3-max-text-and-image-to-video-post-trained-by-fal-4991600a]] (fal) claims FLUX 3 Max is joint #1 image-to-video on Artificial Analysis's preliminary arena (Elo 1139, tied Seedance 2.5); [[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]] shows the live AA I2V boards led by MiniMax H3 768p (Elo 1140) and Seedance 2.0 720p (audio board, Elo 1197) with FLUX 3 Max not listed as sole #1. Status: unresolved

## Open questions

- [ ] What are FLUX 3 Max commercial-use terms for game video, and what is its primary dated release announcement (reported 2026-10-19, unconfirmed)?

## See also

- [[generative-media-models]]
- [[video-tools]]
