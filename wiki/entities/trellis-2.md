---
title: "TRELLIS.2"
kind: entity
aliases: ["TRELLIS 2", "TRELLIS.2-4B", "Trellis 2", "microsoft/TRELLIS.2-4B"]
sources:
  - "[[trellis-2-native-and-compact-structured-latents-for-3d-generation-711104a6]]"
  - "[[microsoft-trellis-2-4b-hugging-face-model-card-40579db9]]"
last_updated: 2026-10-24
last_verified: 2026-10-24
freshness_window_days: 30
profile: tool
modality: 3d
tasks: ["3d-generation", "pbr-texturing"]
vendor: "Microsoft Research"
model_ids: ["microsoft/TRELLIS.2-4B"]
access: ["open-weights"]
open_weights_license: "MIT"
hardware_floor: unknown
pricing: "free — open weights under MIT (2026-06-05)"
pricing_source: "[[microsoft-trellis-2-4b-hugging-face-model-card-40579db9]]"
commercial_use: "permitted — MIT license (2026-06-05)"
commercial_use_source: "[[trellis-2-native-and-compact-structured-latents-for-3d-generation-711104a6]]"
status: active
status_source: "[[microsoft-trellis-2-4b-hugging-face-model-card-40579db9]]"
last_release: unknown
arena_rank: []
arena_rank_source: []
---

# TRELLIS.2

## Summary

TRELLIS.2-4B is a 4B-parameter open 3D generative model from Microsoft Research, Tsinghua University and USTC, released on Hugging Face under the MIT license, that generates fully textured assets with full PBR materials (including transparency/translucency) at 512³–1536³ resolution [[microsoft-trellis-2-4b-hugging-face-model-card-40579db9]]. Generation time scales with resolution: roughly 3 s at 512³, 17 s at 1024³ and 60 s at 1536³, and the project page states explicitly that the MIT release is for commercial use [[trellis-2-native-and-compact-structured-latents-for-3d-generation-711104a6]].

> The model is released on Hugging Face supporting resolutions ranging from 512 cubed to 1536 cubed, available under the MIT license.

> At 512 cubed it generates a fully textured asset in approximately 3 seconds (2s shape + 1s material); at 1024 cubed in approximately 17 seconds; at 1536 cubed in approximately 60 seconds. Released under MIT license for commercial use.

Because the weights are MIT-licensed [[microsoft-trellis-2-4b-hugging-face-model-card-40579db9]], `pricing` is recorded as free for self-hosting; any hosted (fal / Replicate) pricing is not yet on record.

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-24)_

## Open questions

- [ ] VRAM floor at 512³ / 1024³ / 1536³ — the sources give latency but not memory (`hardware_floor` is `unknown`).
- [ ] fal / Replicate endpoints and their per-generation price.
- [ ] Release date of TRELLIS.2-4B.
- [ ] Third-party arena placement.

## See also

- [[ai-in-game-dev]]
- [[3d-tools]]
- [[hunyuan3d]]
- [[assetgen]]
