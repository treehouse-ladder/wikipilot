---
title: "HY-Motion"
kind: entity
aliases: ["HY-Motion 1.0", "Tencent HY-Motion", "tencent/HY-Motion"]
sources:
  - "[[hy-motion-1-0-text-to-3d-human-motion-and-character-animation-generation-16c365c2]]"
last_updated: 2026-10-24
last_verified: 2026-10-24
freshness_window_days: 30
profile: tool
modality: motion
tasks: ["text-to-motion", "character-animation"]
vendor: "Tencent"
model_ids: ["tencent/HY-Motion"]
access: ["open-weights"]
open_weights_license: unknown
hardware_floor: unknown
pricing: unknown
pricing_source: null
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[hy-motion-1-0-text-to-3d-human-motion-and-character-animation-generation-16c365c2]]"
last_release: unknown
arena_rank: []
arena_rank_source: []
---

# HY-Motion

## Summary

HY-Motion 1.0 is Tencent's open-weight text-to-3D-human-motion model, shipped in a 1.0B-parameter full variant and a 0.46B distilled variant, exporting SMPL-H and FBX so clips import into Unity and Unreal character rigs without a retargeting step [[hy-motion-1-0-text-to-3d-human-motion-and-character-animation-generation-16c365c2]]. Text conditioning covers locomotion, gestures and interactions with style control ("slow walk", "aggressive sprint") that would otherwise require separate mocap or hand-keyed animation [[hy-motion-1-0-text-to-3d-human-motion-and-character-animation-generation-16c365c2]]. The model card is described as a "permissive license" without naming it, so `open_weights_license` and `commercial_use` stay `unknown`.

> HY-Motion 1.0 is Tencent's open-weight text-to-3D human motion generation model. It ships in two variants: a 1.0B parameter full model and a 0.46B parameter distilled variant for lighter inference budgets.

> The model generates human motion directly from text descriptions and exports to SMPL-H and FBX formats, making its output directly importable into Unity and Unreal Engine character animation rigs without requiring intermediate retargeting steps.

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-24)_

## Open questions

- [ ] Exact licence name for the HY-Motion weights and whether it permits commercial use (source only says "permissive").
- [ ] VRAM floor for the 1.0B and 0.46B variants.
- [ ] Release date.

## See also

- [[ai-in-game-dev]]
- [[rig-and-motion-tools]]
- [[unimate]]
- [[motionbricks]]
- [[hunyuan3d]]
