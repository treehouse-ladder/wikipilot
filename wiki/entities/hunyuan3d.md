---
title: "Hunyuan3D"
kind: entity
aliases: ["Hunyuan3D 2.0", "Hunyuan3D 2.1", "Hunyuan3D-PolyGen", "Hunyuan3D Studio", "Tencent Hunyuan3D"]
sources:
  - "[[hunyuan3d-2-1-from-images-to-high-fidelity-3d-assets-with-production-ready-pbr-material-b0de5940]]"
  - "[[hunyuan3d-2-0-scaling-diffusion-models-for-high-resolution-textured-3d-assets-generation-05cee78a]]"
  - "[[tencent-hunyuan3d-polygen-a-model-for-art-grade-3d-assets-1d7dc610]]"
  - "[[hunyuan3d-studio-end-to-end-ai-pipeline-for-game-ready-3d-asset-generation-99606a27]]"
last_updated: 2026-10-24
last_verified: 2026-10-24
freshness_window_days: 30
profile: tool
modality: 3d
tasks: ["image-to-3d", "text-to-3d", "pbr-texturing", "polygon-generation", "part-level-generation"]
vendor: "Tencent"
model_ids: ["hunyuan3d-2.0", "hunyuan3d-2.1", "hunyuan3d-polygen"]
access: ["open-weights"]
open_weights_license: unknown
hardware_floor: "6 GB VRAM shape-only / 16 GB shape+texture (Hunyuan3D 2.0)"
pricing: unknown
pricing_source: null
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[tencent-hunyuan3d-polygen-a-model-for-art-grade-3d-assets-1d7dc610]]"
last_release: unknown
arena_rank: []
arena_rank_source: []
---

# Hunyuan3D

## Summary

Hunyuan3D is Tencent's family of open 3D generation models. Hunyuan3D 2.1 is a fully open-sourced, end-to-end system that produces assets with production-ready PBR materials from a single image, with outputs described as ready for Unity and Unreal; it was the first release in the line to ship full weights *and* training code [[hunyuan3d-2-1-from-images-to-high-fidelity-3d-assets-with-production-ready-pbr-material-b0de5940]]. The licence name is not stated in the ingested sources, so `open_weights_license` stays `unknown`.

> For the first time, the system releases full model weights and training code, enabling community developers to directly fine-tune and extend the model for diverse downstream applications.

Hunyuan3D 2.0 pairs a shape model (Hunyuan3D-DiT) with a texture model (Hunyuan3D-Paint) and gives the only hardware figure on record: 6 GB VRAM for shape generation, 16 GB for shape plus texture [[hunyuan3d-2-0-scaling-diffusion-models-for-high-resolution-textured-3d-assets-generation-05cee78a]].

> It takes 6 GB VRAM for shape generation and 16 GB for shape and texture generation in total.

Hunyuan3D-PolyGen targets "art-grade" output — clean topology, rigging/UV-friendly structure, 10K+ faces via a BPT representation — with Tencent reporting a 70% asset-time reduction and 35% better topology neatness than SOTA [[tencent-hunyuan3d-polygen-a-model-for-art-grade-3d-assets-1d7dc610]]. Hunyuan3D Studio wraps part-level generation, polygon generation and semantic UV into one concept-to-game-ready pipeline [[hunyuan3d-studio-end-to-end-ai-pipeline-for-game-ready-3d-asset-generation-99606a27]].

> Leveraging high-compression BPT representation, it can generate models with 10K+ faces.

> At its core, Hunyuan3D Studio integrates a suite of advanced neural modules (such as Part-level 3D Generation, Polygon Generation, Semantic UV, etc.) into a cohesive and user-friendly system

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-24)_

## Open questions

- [ ] Which licence do the Hunyuan3D 2.x / PolyGen weights carry, and what are the commercial-use terms?
- [ ] Is there a Hunyuan3D 3.x release? No ingested source covers one; this page tracks 2.0 / 2.1 / PolyGen / Studio only.
- [ ] Hosted access: Tencent Cloud API, fal (`fal-ai/hunyuan3d-v21`?) or Replicate endpoints — none cited yet, so `access` lists open weights only.
- [ ] Release dates per version (`last_release` is `unknown`).
- [ ] Third-party arena placement.

## See also

- [[ai-in-game-dev]]
- [[3d-tools]]
- [[trellis-2]]
- [[hy-motion]]
- [[meshy]]
