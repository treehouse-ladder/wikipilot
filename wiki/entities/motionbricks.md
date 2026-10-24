---
title: "MotionBricks"
kind: entity
aliases: ["NVIDIA MotionBricks"]
sources:
  - "[[motionbricks-scalable-real-time-motions-with-modular-latent-generative-model-and-smart-primitives-45bc3aa9]]"
last_updated: 2026-10-24
last_verified: 2026-10-24
freshness_window_days: 30
profile: tool
modality: motion
tasks: ["real-time-motion-generation", "navigation-and-interaction-control", "style-prompting"]
vendor: "NVIDIA"
model_ids: ["motionbricks"]
access: ["unknown"]
open_weights_license: unknown
hardware_floor: unknown
pricing: unknown
pricing_source: null
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[motionbricks-scalable-real-time-motions-with-modular-latent-generative-model-and-smart-primitives-45bc3aa9]]"
last_release: unknown
arena_rank: []
arena_rank_source: []
---

# MotionBricks

## Summary

MotionBricks is an NVIDIA (NVlabs) real-time motion generator: one latent generative model trained on 350K production-grade mocap clips, topped with "smart primitives" — navigation targets, object-interaction keyframes and style prompts — with the network filling in everything else at a claimed 15,000 FPS [[motionbricks-scalable-real-time-motions-with-modular-latent-generative-model-and-smart-primitives-45bc3aa9]]. It shipped at SIGGRAPH 2026 with code that integrates into NVIDIA's GR00T whole-body-control stack [[motionbricks-scalable-real-time-motions-with-modular-latent-generative-model-and-smart-primitives-45bc3aa9]].

> MotionBricks delivers 15,000 FPS real-time motion generation for robots and games, trained on more than 350,000 motion clips, running at game-engine speeds, and lets creators direct and connect character movements.

> MotionBricks shipped to SIGGRAPH 2026 with code that integrates directly into NVIDIA's GR00T Whole-Body Control stack.

The project page [[motionbricks-scalable-real-time-motions-with-modular-latent-generative-model-and-smart-primitives-45bc3aa9]] says "code" shipped but does not state whether pretrained weights are public or under what licence, so `access` is `["unknown"]`.

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-24)_

## Open questions

- [ ] Are pretrained MotionBricks weights released alongside the code, and under what licence?
- [ ] Is there a game-engine (Unity / Unreal) integration path, or only the GR00T robotics stack?
- [ ] Hardware requirements for the 15,000 FPS figure.

## See also

- [[ai-in-game-dev]]
- [[rig-and-motion-tools]]
- [[hy-motion]]
- [[audio2face]]
