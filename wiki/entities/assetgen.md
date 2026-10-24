---
title: "AssetGen"
kind: entity
aliases: ["AssetGen Flash"]
sources:
  - "[[assetgen-deployable-3d-asset-generation-at-interactive-speed-7fcd9e74]]"
last_updated: 2026-10-24
last_verified: 2026-10-24
freshness_window_days: 30
profile: tool
modality: 3d
tasks: ["image-to-3d", "mesh-simplification", "normal-baking", "uv-unwrapping"]
vendor: unknown
model_ids: ["assetgen", "assetgen-flash"]
access: ["unknown"]
open_weights_license: unknown
hardware_floor: unknown
pricing: unknown
pricing_source: null
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[assetgen-deployable-3d-asset-generation-at-interactive-speed-7fcd9e74]]"
last_release: unknown
arena_rank: []
arena_rank_source: []
---

# AssetGen

## Summary

AssetGen is an image-to-3D system built for deployment: from one reference image it produces, in 30 seconds, a mesh with baked normals, a color texture and a controlled polygon budget suitable for real-time (including mobile) rendering, with an "AssetGen Flash" variant at 14 seconds for interactive and agentic loops [[assetgen-deployable-3d-asset-generation-at-interactive-speed-7fcd9e74]]. Geometry uses a coarse-to-refine VecSet framework with GPU-side simplification, cleaning, normal baking and parallel UV unwrapping [[assetgen-deployable-3d-asset-generation-at-interactive-speed-7fcd9e74]].

> Given one reference image, in 30 seconds it produces a high-quality mesh with baked normals, a color texture, and a controlled polygon budget suitable for real-time rendering, including mobile use cases.

> The AssetGen Flash variant further reduces latency to 14 seconds for interactive and agentic creation loops.

The ingested source is the arXiv abstract only [[assetgen-deployable-3d-asset-generation-at-interactive-speed-7fcd9e74]]; it does not name the publishing organisation or any release channel, so `vendor` and `access` are `unknown`.

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-24)_

## Open questions

- [ ] Which lab publishes AssetGen (the abstract on record does not say)?
- [ ] Are weights, code or a hosted endpoint available?
- [ ] Licence / commercial-use terms.

## See also

- [[ai-in-game-dev]]
- [[3d-tools]]
- [[trellis-2]]
