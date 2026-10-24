---
title: "NVIDIA Audio2Face"
kind: entity
aliases: ["Audio2Face", "A2F", "Audio2Face-3D"]
sources:
  - "[[nvidia-open-sources-audio2face-animation-model-b26d433b]]"
last_updated: 2026-10-24
last_verified: 2026-10-24
freshness_window_days: 30
profile: tool
modality: motion
tasks: ["audio-to-facial-animation", "lip-sync"]
vendor: "NVIDIA"
model_ids: ["audio2face"]
access: ["open-weights"]
open_weights_license: unknown
hardware_floor: unknown
pricing: unknown
pricing_source: null
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[nvidia-open-sources-audio2face-animation-model-b26d433b]]"
last_release: unknown
arena_rank: []
arena_rank_source: []
---

# NVIDIA Audio2Face

## Summary

Audio2Face generates facial animation — lip-sync and emotional expression — from an audio track by analysing phonemes and intonation; NVIDIA has open-sourced the models, the SDK and the training framework so teams can fine-tune for their own characters [[nvidia-open-sources-audio2face-animation-model-b26d433b]]. The SDK's C++ and Python source is MIT-licensed; the blog does not state the licence that applies to the model weights themselves, so `open_weights_license` stays `unknown` [[nvidia-open-sources-audio2face-animation-model-b26d433b]].

> NVIDIA is open sourcing the Audio2Face models and SDK, as well as the Audio2Face training framework, so anyone can fine-tune and customize the pre-existing models for specific use cases.

> The SDK contains C++ and Python source code through the MIT license.

Filed under `modality: motion` — it produces animation data from audio, not a rig [[nvidia-open-sources-audio2face-animation-model-b26d433b]].

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-24)_

## Open questions

- [ ] Licence on the Audio2Face model weights (the MIT statement covers the SDK source) and its commercial-use terms.
- [ ] GPU requirement for real-time inference.
- [ ] Release date of the open-source drop.

## See also

- [[ai-in-game-dev]]
- [[rig-and-motion-tools]]
- [[motionbricks]]
- [[inworld-realtime-tts-2]]
