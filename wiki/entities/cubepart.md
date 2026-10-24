---
title: "CubePart"
kind: entity
aliases: ["Roblox CubePart"]
sources:
  - "[[cubepart-an-open-vocabulary-part-controllable-3d-generator-5e45953c]]"
last_updated: 2026-10-24
last_verified: 2026-10-24
freshness_window_days: 30
profile: tool
modality: 3d
tasks: ["part-controllable-3d-generation", "open-vocabulary-part-segmentation"]
vendor: "Roblox"
model_ids: ["cubepart"]
access: ["unknown"]
open_weights_license: unknown
hardware_floor: unknown
pricing: unknown
pricing_source: null
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[cubepart-an-open-vocabulary-part-controllable-3d-generator-5e45953c]]"
last_release: unknown
arena_rank: []
arena_rank_source: []
---

# CubePart

## Summary

CubePart is Roblox's generative framework for open-vocabulary, *part-controllable* 3D mesh generation: the creator defines the list of parts an object should be split into, and the model outputs an assembled set of distinct, labeled meshes that can be driven by animation, physics and gameplay scripts without manual cleanup [[cubepart-an-open-vocabulary-part-controllable-3d-generator-5e45953c]]. It was trained on a Roblox-built dataset of 460K+ assets and 2.02M parts [[cubepart-an-open-vocabulary-part-controllable-3d-generator-5e45953c]].

> CubePart outputs an assembled set of distinct, functional, and accurately-labeled meshes that match the developer's programming needs out of the box.

> To train CubePart, Roblox created a dataset featuring more than 460,000 assets-over 11 times larger than previous public datasets-and 2.02 million parts.

The newsroom post [[cubepart-an-open-vocabulary-part-controllable-3d-generator-5e45953c]] does not state whether weights, code or an API are available outside Roblox, so `access` is `["unknown"]`.

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-24)_

## Open questions

- [ ] Are CubePart weights or code released (as with Roblox's earlier Cube releases), or is it Roblox-Studio-only?
- [ ] Licence and commercial-use terms if released.
- [ ] Release date.

## See also

- [[ai-in-game-dev]]
- [[3d-tools]]
- [[hunyuan3d]]
