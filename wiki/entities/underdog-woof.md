---
title: "Underdog Woof"
kind: entity
aliases: ["Underdog-Woof", "Woof TTS"]
sources:
  - "[[underdog-woof-a-40-6-mb-cpu-text-to-speech-model-b55589ca]]"
last_updated: 2026-11-11
last_verified: 2026-11-11
freshness_window_days: 30
profile: tool
modality: voice
tasks: ["text-to-speech"]
vendor: "Conway Research"
model_ids: ["underdog-woof"]
access: ["open-weights"]
open_weights_license: "underdog-non-commercial-1.0"
hardware_floor: "laptop CPU (no GPU required)"
pricing: "free for personal, research, teaching and non-profit use; commercial license from conway.tech (price undisclosed) (2026-11-11)"
pricing_source: "[[underdog-woof-a-40-6-mb-cpu-text-to-speech-model-b55589ca]]"
commercial_use: "non-commercial only under underdog-non-commercial-1.0; commercial license available from Conway Research on request (2026-11-11)"
commercial_use_source: "[[underdog-woof-a-40-6-mb-cpu-text-to-speech-model-b55589ca]]"
status: active
status_source: "[[underdog-woof-a-40-6-mb-cpu-text-to-speech-model-b55589ca]]"
last_release: 2026-11-11
arena_rank: []
arena_rank_source: []
---

# Underdog Woof

## Summary

Underdog Woof is a 40.6 MB English TTS model from Conway Research with two voices (Juno and Mira), running entirely on a laptop CPU with no GPU and no dependencies beyond numpy [[underdog-woof-a-40-6-mb-cpu-text-to-speech-model-b55589ca]]. The model has 38.24M parameters, generates 24 kHz mono audio, and stores both voices in a single weights file using an audio decoder adapted from Kyutai's Mimi codec.

> Underdog Woof is a small English text-to-speech model with two voices, Juno and Mira. It runs on a laptop CPU with nothing but numpy, from a single 40.6 MB file. [[underdog-woof-a-40-6-mb-cpu-text-to-speech-model-b55589ca]]

**Performance benchmarks (Gradium TTS Hard Cases, English):** Juno WER 1.53%, Mira WER 1.42%; Juno 13.8× real-time on one CPU thread, Mira 7.2× real-time; peak RAM 402 MB (Juno) / 601 MB (Mira) [[underdog-woof-a-40-6-mb-cpu-text-to-speech-model-b55589ca]].

> Word error rate is 1.53% for Juno and 1.42% for Mira on Gradium TTS Hard Cases (English). Juno runs 13.8x faster than real time on one CPU thread; Mira runs at 7.2x real time. Peak memory is 402 MB for Juno and 601 MB for Mira. [[underdog-woof-a-40-6-mb-cpu-text-to-speech-model-b55589ca]]

**License:** `underdog-non-commercial-1.0` — free for personal, research, teaching and non-profit use. Commercial use requires a separate license from Conway Research (license@conway.tech); no price disclosed [[underdog-woof-a-40-6-mb-cpu-text-to-speech-model-b55589ca]]. The model is hosted on Hugging Face.

> Primary license: underdog-non-commercial-1.0 - free for personal, research, teaching and non-profit use. Commercial use requires a license from license at conway.tech. [[underdog-woof-a-40-6-mb-cpu-text-to-speech-model-b55589ca]]

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-11-11)_

## Open questions

- [ ] What is the commercial license price from Conway Research, and what are its terms (per-seat, per-call, revenue-share)?
- [ ] Does Underdog Woof appear on any third-party TTS benchmark leaderboard (e.g. Artificial Analysis Controlled Voice TTS, TTS Arena) beyond the Gradium TTS Hard Cases figures in the model card?
- [ ] Will Conway Research release additional voices beyond Juno and Mira, or a multilingual variant?

## See also

- [[audio-tools]]
- [[elevenlabs]]
- [[inworld-realtime-tts-2]]
