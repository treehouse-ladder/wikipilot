---
title: "TokenRig (Skin Tokens)"
kind: entity
aliases: ["TokenRig", "Skin Tokens", "SkinTokens"]
sources:
  - "[[skin-tokens-a-learned-compact-representation-for-unified-autoregressive-rigging-d27f3879]]"
last_updated: 2026-10-24
last_verified: 2026-10-24
freshness_window_days: 30
profile: tool
modality: rig
tasks: ["auto-rigging", "skeleton-generation", "skinning-weights"]
vendor: unknown
model_ids: ["tokenrig"]
access: ["unknown"]
open_weights_license: unknown
hardware_floor: unknown
pricing: unknown
pricing_source: null
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[skin-tokens-a-learned-compact-representation-for-unified-autoregressive-rigging-d27f3879]]"
last_release: unknown
arena_rank: []
arena_rank_source: []
---

# TokenRig (Skin Tokens)

## Summary

TokenRig is a unified autoregressive auto-rigging framework that models an entire rig — skeleton hierarchy plus skinning weights — as a single token sequence, built on "SkinTokens", a learned discrete representation of skinning weights [[skin-tokens-a-learned-compact-representation-for-unified-autoregressive-rigging-d27f3879]]. Given a mesh it emits a complete skeleton and weights importable into standard animation pipelines; the paper reports 98–133% better skinning accuracy than prior SOTA and 17–22% better bone prediction after RL refinement [[skin-tokens-a-learned-compact-representation-for-unified-autoregressive-rigging-d27f3879]].

> Given an input 3D mesh, it generates a complete skeleton hierarchy and skin weights that can be directly imported into standard 3D pipelines for character animation and simulation.

Only the arXiv abstract is on record [[skin-tokens-a-learned-compact-representation-for-unified-autoregressive-rigging-d27f3879]]; it names no organisation, code release or licence, so `vendor` and `access` are `unknown`.

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-24)_

## Open questions

- [ ] Publishing lab / affiliation.
- [ ] Are code or weights released, and under what licence?
- [ ] Inference hardware requirements.

## See also

- [[ai-in-game-dev]]
- [[rig-and-motion-tools]]
- [[unimate]]
- [[mocapanything]]
