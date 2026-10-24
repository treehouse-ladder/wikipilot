---
title: "MoCapAnything"
kind: entity
aliases: ["MoCapAnything V2", "MocapAnything"]
sources:
  - "[[mocapanything-v2-end-to-end-motion-capture-for-arbitrary-skeletons-d09ec008]]"
last_updated: 2026-10-24
last_verified: 2026-10-24
freshness_window_days: 30
profile: tool
modality: motion
tasks: ["video-to-motion", "markerless-mocap", "arbitrary-skeleton-retargeting"]
vendor: unknown
model_ids: ["mocapanything-v2"]
access: ["unknown"]
open_weights_license: unknown
hardware_floor: unknown
pricing: unknown
pricing_source: null
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[mocapanything-v2-end-to-end-motion-capture-for-arbitrary-skeletons-d09ec008]]"
last_release: unknown
arena_rank: []
arena_rank_source: []
---

# MoCapAnything

## Summary

MoCapAnything V2 is a video-to-animation (markerless mocap) framework for arbitrary skeletons in which both the Video-to-Pose and Pose-to-Rotation stages are learnable and jointly optimized — replacing the non-differentiable IK stage of earlier designs that left bone-axis twist ambiguous [[mocapanything-v2-end-to-end-motion-capture-for-arbitrary-skeletons-d09ec008]]. On Truebones Zoo and Objaverse it cuts rotation error from ~17° to ~10° (6.54° on unseen skeletons) at ~20× the inference speed of mesh-based pipelines [[mocapanything-v2-end-to-end-motion-capture-for-arbitrary-skeletons-d09ec008]].

> Experiments on Truebones Zoo and Objaverse show that the method reduces rotation error from ~17 degrees to ~10 degrees, and to 6.54 degrees on unseen skeletons, while achieving ~20x faster inference than mesh-based pipelines.

Only the arXiv abstract is on record [[mocapanything-v2-end-to-end-motion-capture-for-arbitrary-skeletons-d09ec008]]; it names no organisation, release channel or licence, so `vendor` and `access` are `unknown`.

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-24)_

## Open questions

- [ ] Publishing lab / affiliation.
- [ ] Are code or weights released, and under what licence?
- [ ] Does it export to FBX / engine-ready formats?

## See also

- [[ai-in-game-dev]]
- [[rig-and-motion-tools]]
- [[unimate]]
- [[tokenrig]]
