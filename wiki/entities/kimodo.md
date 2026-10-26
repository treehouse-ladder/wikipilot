---
title: "Kimodo"
kind: entity
aliases: ["NVIDIA Kimodo", "Kimodo-SOMA-RP", "Kimodo-G1", "nv-tlabs/kimodo"]
sources:
  - "[[kimodo-scaling-controllable-human-motion-generation-fe9ff887]]"
  - "[[nvidia-kimodo-soma-rp-v1-1-hugging-face-3543d52b]]"
last_updated: 2026-10-26
last_verified: 2026-10-26
freshness_window_days: 60
profile: tool
modality: motion
tasks: ["text-to-motion", "constrained-motion-generation", "human-motion", "robot-motion"]
vendor: "NVIDIA"
model_ids: ["kimodo-soma-rp-v1.1", "kimodo-soma-rp-v1.2", "kimodo-g1", "kimodo-smpl-x"]
access: ["open-weights"]
open_weights_license: "SOMA-SEED-v1.1: commercial; G1 variants: NVIDIA Open Model License; SMPL-X variant: non-commercial research only"
hardware_floor: unknown
pricing: "open-weights (self-hosted; free)"
pricing_source: "[[kimodo-scaling-controllable-human-motion-generation-fe9ff887]]"
commercial_use: "SOMA-SEED-v1.1 commercial-ready; G1 variants under NVIDIA Open Model License; at least one SMPL-X variant research-only (2026-10-26)"
commercial_use_source: "[[nvidia-kimodo-soma-rp-v1-1-hugging-face-3543d52b]]"
status: active
status_source: "[[kimodo-scaling-controllable-human-motion-generation-fe9ff887]]"
last_release: 2026-10-15
arena_rank: []
arena_rank_source: []
---

# Kimodo

## Summary

Kimodo is NVIDIA Research's open-weights kinematic motion diffusion model for controllable human and humanoid robot motion generation. It is trained on 700 hours of optical motion capture data and accepts multi-modal constraints alongside text: full-body keyframes, sparse joint positions and rotations, 2D waypoints, and dense 2D paths [[kimodo-scaling-controllable-human-motion-generation-fe9ff887]]. This constraint-conditioning distinguishes it from pure text-to-motion models — a designer can steer foot placement or waypoint path compliance, making it more directly applicable to in-engine animation pipelines than unconstrained generation.

> Kimodo is controlled through text and constraints to generate high-quality 3D human and robot motions. Constraints include full-body keyframes, sparse joint positions and rotations, 2D waypoints, and dense 2D paths. [[kimodo-scaling-controllable-human-motion-generation-fe9ff887]]

> Kimodo is trained on 700 hours of optical motion capture data. [[kimodo-scaling-controllable-human-motion-generation-fe9ff887]]

The release (GitHub `nv-tlabs/kimodo`) bundles code, a CLI to generate motions on both human and robot skeletons, an interactive timeline demo, a benchmark built on the BONES-SEED dataset, and annotations. Models are available for SOMA, Unitree G1, and SMPL-X skeletons; the newest variants (`Kimodo-SOMA-RP-v1.2`) are dated 2026-10-15 [[kimodo-scaling-controllable-human-motion-generation-fe9ff887]].

**Licensing is per-variant, not uniform.** The SOMA-SEED-v1.1 variant is commercial-ready; the Unitree G1 variants ship under the NVIDIA Open Model License; at least one SMPL-X variant is non-commercial research only. Studios must check model-card-level terms before committing a variant to a production pipeline [[nvidia-kimodo-soma-rp-v1-1-hugging-face-3543d52b]].

> Licensing varies by variant: one SMPL-X model is for non-commercial research use only, the SOMA-SEED-v1.1 model is ready for commercial use, and the G1 models are released under the NVIDIA Open Model License. [[nvidia-kimodo-soma-rp-v1-1-hugging-face-3543d52b]]

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-26)_

## Open questions

- [ ] Does Kimodo's constraint-controllable output (keyframes / 2D waypoints / dense 2D paths) export engine-ready FBX/BVH that retargets cleanly onto Unity/Unreal character rigs, or does the SMPL-X/SOMA/G1 skeleton output still need manual retargeting? [[kimodo-scaling-controllable-human-motion-generation-fe9ff887]]
- [ ] Which specific Kimodo model variants are safe for a commercial game pipeline — only SOMA-SEED-v1.1 and the NVIDIA-Open-Model-License G1 variants, or do the RP (rotation-prediction) SOMA/SMPL-X variants also permit commercial use? [[nvidia-kimodo-soma-rp-v1-1-hugging-face-3543d52b]]

## See also

- [[ai-in-game-dev]]
- [[rig-and-motion-tools]]
