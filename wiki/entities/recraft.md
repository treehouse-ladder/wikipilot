---
title: "Recraft"
kind: entity
aliases: ["Recraft V4.1", "Recraft V4.1 Flash V2", "recraft-v4-1-flash-v2", "Recraft V4.1 Flash"]
profile: tool
modality: image
tasks: ["text-to-image"]
vendor: "Recraft"
model_ids: ["recraft-v4-1-flash-v2", "recraft-v4-1-flash", "recraft-v4-1"]
access: ["api", "web"]
open_weights_license: "n/a"
hardware_floor: "unknown"
pricing: "$0.007/image (recraft-v4-1-flash-v2, raster; 2026-11-17)"
pricing_source: "[[recraft-v4-1-flash-v2-the-fastest-ai-image-model-on-the-market-2b7c5ee7]]"
commercial_use: "unknown"
commercial_use_source: null
status: "active"
status_source: "[[recraft-v4-1-flash-v2-the-fastest-ai-image-model-on-the-market-2b7c5ee7]]"
last_release: "unknown"
arena_rank: []
arena_rank_source: []
sources: ["[[recraft-v4-1-flash-v2-the-fastest-ai-image-model-on-the-market-2b7c5ee7]]"]
last_updated: 2026-11-17
last_verified: 2026-11-17
freshness_window_days: 30
---

# Recraft

## Summary

Recraft is a proprietary image-generation platform (Recraft Studio web app + Recraft API). Its current speed/cost tier is **Recraft V4.1 Flash V2** (`recraft-v4-1-flash-v2`), billed at $0.007/image for raster output with no style support, and described by Recraft as the fastest and cheapest model in its API [[recraft-v4-1-flash-v2-the-fastest-ai-image-model-on-the-market-2b7c5ee7]]. In Recraft's own 23-model benchmark it ranked first at 1.1 s median prompt-to-image, ahead of FLUX.2 klein 9B at 1.4 s; DesignArena independently measured it at 1.5 s and still ranked it fastest on that board [[recraft-v4-1-flash-v2-the-fastest-ai-image-model-on-the-market-2b7c5ee7]]. It was released in November 2026, replacing the original V4.1 Flash (September 2026, same $0.007/image price) [[recraft-v4-1-flash-v2-the-fastest-ai-image-model-on-the-market-2b7c5ee7]]. The $0.007/image + ~1.1 s profile makes it a budget/throughput option for high-volume game-asset image pipelines, but it has no published quality-arena (AA-Image-T2I) placement — only speed benchmarks — and its commercial-use terms for shipping generated game assets are not stated in the ingested source.

> Recraft V4.1 Flash V2 is the fastest and cheapest model available through the Recraft API, generating raster images at $0.007 per image with no style support. [[recraft-v4-1-flash-v2-the-fastest-ai-image-model-on-the-market-2b7c5ee7]]

> In Recraft's benchmark of 23 image models, Recraft V4.1 Flash V2 ranked first at 1.1 seconds median from prompt to image, ahead of FLUX.2 klein 9B at 1.4 seconds. [[recraft-v4-1-flash-v2-the-fastest-ai-image-model-on-the-market-2b7c5ee7]]

## Disputes

## Open questions

- [ ] Recraft V4.1 Flash V2 commercial-use / licensing terms for shipping generated assets in a commercial game — not stated in the ingested source [[recraft-v4-1-flash-v2-the-fastest-ai-image-model-on-the-market-2b7c5ee7]].
- [ ] Recraft quality-arena placement (Artificial Analysis AA-Image-T2I v2.1) — only speed boards (Recraft benchmark, DesignArena latency) measured so far; no human-preference Elo.
- [ ] Recraft V4.1 Flash V2 exact release date — source states only "November 2026" (blog updated 2026-11-13).

## See also

- [[generative-media-models]]
- [[image-tools]]
