---
title: "Meshy"
kind: entity
aliases: ["Meshy AI", "Meshy-7", "Meshy 7.1", "meshy.ai"]
sources:
  - "[[meshy-7-1-ultra-4k-detail-richness-benchmark-45c8801a]]"
  - "[[meshy-7-is-live-higher-fidelity-image-to-3d-generation-with-ultra-mode-f27c1d9b]]"
  - "[[meshy-6-smarter-geometry-faster-workflows-limitless-3d-creativity-3d2a1b1b]]"
  - "[[meshy-brings-ai-agents-to-3d-creation-meshy-3d-agent-beta-launches-f384359e]]"
  - "[[meshy-raises-nearly-400-million-at-a-1-5-billion-valuation-the-largest-round-to-date-in-ai-3d-629b40da]]"
last_updated: 2026-10-24
last_verified: 2026-10-24
freshness_window_days: 30
profile: tool
modality: 3d
tasks: ["text-to-3d", "image-to-3d", "multi-image-to-3d", "retexture", "low-poly-mode"]
vendor: "Meshy"
model_ids: ["meshy-6", "meshy-7", "meshy-7.1"]
access: ["web", "api"]
open_weights_license: unknown
hardware_floor: unknown
pricing: unknown
pricing_source: null
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[meshy-7-1-ultra-4k-detail-richness-benchmark-45c8801a]]"
last_release: unknown
arena_rank: []
arena_rank_source: []
---

# Meshy

## Summary

Meshy is a hosted AI 3D-generation platform (web app plus API) whose current model line is Meshy 7.1; it covers text-to-3D, image-to-3D, multi-image-to-3D and retexturing, and the 7.1 release added an "Ultra 4K" geometry mode that scales generation from 2048³ to 4096³ voxels with raw meshes up to 80 million triangles before simplification [[meshy-7-1-ultra-4k-detail-richness-benchmark-45c8801a]]. The 7.1 model is open to all registered users, but Ultra 2K/4K resolution and downloads are gated to subscribers, and Ultra 4K is single-view only [[meshy-7-1-ultra-4k-detail-richness-benchmark-45c8801a]]. Meshy's own "Detail Richness" benchmark ranks 7.1 first at 1K/2K/4K — a vendor-run benchmark, so it is reported here as a claim rather than recorded in `arena_rank` [[meshy-7-1-ultra-4k-detail-richness-benchmark-45c8801a]].

> A new Ultra 4K mode scales geometry generation from 2048 cubed to 4096 cubed, and as of this release is the only 3D generative model to reach it, with raw meshes up to 80 million triangles before simplification.

Meshy 7 (the previous step) introduced the `ultra_mode` API parameter, a multi-view generation model for the Multi-Image to 3D API, and a new texturing model for the Retexture API [[meshy-7-is-live-higher-fidelity-image-to-3d-generation-with-ultra-mode-f27c1d9b]]. Meshy 6 brought a dedicated Low Poly Mode aimed at game developers and "upgraded APIs" [[meshy-6-smarter-geometry-faster-workflows-limitless-3d-creativity-3d2a1b1b]].

> Meshy 7 introduces the ultra_mode parameter, which enables Ultra generation for even finer surface detail. For the Multi-Image to 3D API, Meshy 7 is Meshy's multi-view generation model, which conditions on all of your input views together and drives texturing from them.

> A dedicated Low Poly Mode built specifically for game developers produces efficient wireframes optimized for real-time performance, making assets easier to integrate into game engines without extensive manual retopology.

On the product side, Meshy 3D Agent Beta (a chat-based, multi-step ideation-to-asset workflow) became available to all users on meshy.ai on June 4, 2026 [[meshy-brings-ai-agents-to-3d-creation-meshy-3d-agent-beta-launches-f384359e]]. Commercially, Meshy raised nearly $400M in a Series B at a $1.5B valuation and reported 12M+ registered users and 100M+ models created as of July 2026 [[meshy-raises-nearly-400-million-at-a-1-5-billion-valuation-the-largest-round-to-date-in-ai-3d-629b40da]].

> At launch, Meshy 3D Agent Beta became available to all users on meshy.ai from June 4, 2026.

> As of July 2026, the company's annual recurring revenue is growing about 12x year over year, with more than 12 million registered users and over 100 million models created.

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-24)_

## Open questions

- [ ] Pricing (per-credit / per-generation cost and plan tiers) — no ingested source states a figure; the sweep should cite meshy.ai pricing or docs.meshy.ai.
- [ ] Commercial-use terms per plan (free vs subscribed) — only "subscribed users can download 7.1 models" is on record.
- [ ] Exact release dates for Meshy 7 and 7.1 (sources carry no dates; `last_release` is `unknown`).
- [ ] Is Meshy listed on any third-party board (Artificial Analysis image-to-3D arena, etc.)? Only the vendor-run Detail Richness benchmark is cited.
- [ ] fal / Replicate endpoint ids, if any (`model_ids` carries vendor ids only).

## See also

- [[ai-in-game-dev]]
- [[3d-tools]]
- [[tripo]]
- [[hyper3d-rodin]]
- [[hunyuan3d]]
