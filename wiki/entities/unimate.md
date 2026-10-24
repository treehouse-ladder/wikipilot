---
title: "UniMate"
kind: entity
aliases: ["Linzhan/UniMate"]
sources:
  - "[[unimate-one-unified-model-to-animate-diverse-skeletons-b8768176]]"
last_updated: 2026-10-24
last_verified: 2026-10-24
freshness_window_days: 30
profile: tool
modality: motion
tasks: ["text-to-motion", "arbitrary-skeleton-animation"]
vendor: unknown
model_ids: ["Linzhan/UniMate"]
access: ["open-weights"]
open_weights_license: "CC-BY-NC-4.0 (checkpoints); MIT (code)"
hardware_floor: unknown
pricing: unknown
pricing_source: null
commercial_use: "not permitted for the checkpoints — CC BY-NC 4.0 (2026-10-11)"
commercial_use_source: "[[unimate-one-unified-model-to-animate-diverse-skeletons-b8768176]]"
status: active
status_source: "[[unimate-one-unified-model-to-animate-diverse-skeletons-b8768176]]"
last_release: unknown
arena_rank: []
arena_rank_source: []
---

# UniMate

## Summary

UniMate is a text-conditioned flow-matching model whose pretrained checkpoints generate motion for skeletons of any topology — animals, humanoids and rigged objects — in fixed 60-frame (2 s, 30 fps) samples with per-joint position, rotation and velocity output [[unimate-one-unified-model-to-animate-diverse-skeletons-b8768176]]. The model card is candid about limits: there is no unified contact model, so contact-rich motion can slide, drift or penetrate the ground unless foot-locking or IK post-processing is applied [[unimate-one-unified-model-to-animate-diverse-skeletons-b8768176]]. Checkpoints are CC BY-NC 4.0 (non-commercial) while the code is MIT, which is why `commercial_use` is recorded as not permitted for the weights [[unimate-one-unified-model-to-animate-diverse-skeletons-b8768176]].

> Pretrained checkpoints of UniMate, a text-conditioned flow-matching model that generates motion for skeletons of any topology: animals, humanoids and rigged objects.

> Checkpoints: CC BY-NC 4.0. Code: MIT.

The Hugging Face namespace is an individual account (`Linzhan`), and the card [[unimate-one-unified-model-to-animate-diverse-skeletons-b8768176]] does not name an institution, so `vendor` is `unknown`.

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-24)_

## Open questions

- [ ] Which institution or lab is behind UniMate (paper venue / affiliation)?
- [ ] VRAM floor.
- [ ] Release date of the checkpoints.

## See also

- [[ai-in-game-dev]]
- [[rig-and-motion-tools]]
- [[hy-motion]]
- [[mocapanything]]
- [[tokenrig]]
