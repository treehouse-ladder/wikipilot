---
title: "ElevenLabs Music"
kind: entity
aliases: ["ElevenLabs music generation", "elevenlabs music API"]
sources:
  - "[[elevenlabs-music-0-15-per-minute-5-minute-cap-studio-games-plan-restriction-9f14fd6d]]"
  - "[[elevenlabs-introduces-music-v2-5-its-best-music-model-yet-e742a57d]]"
last_updated: 2026-11-08
last_verified: 2026-11-08
freshness_window_days: 30
profile: tool
modality: music
tasks: ["text-to-music"]
vendor: "ElevenLabs"
model_ids: ["music_v2_5", "music_v2"]
access: ["api"]
open_weights_license: unknown
hardware_floor: unknown
pricing: "$0.15/min, 5-min cap per generation (2026-10-25)"
pricing_source: "[[elevenlabs-music-0-15-per-minute-5-minute-cap-studio-games-plan-restriction-9f14fd6d]]"
commercial_use: "allowed on all paid plans except Studio Games self-serve (2026-10-25)"
commercial_use_source: "[[elevenlabs-music-0-15-per-minute-5-minute-cap-studio-games-plan-restriction-9f14fd6d]]"
status: active
status_source: "[[elevenlabs-music-0-15-per-minute-5-minute-cap-studio-games-plan-restriction-9f14fd6d]]"
last_release: 2026-11-08
arena_rank: []
arena_rank_source: []
---

# ElevenLabs Music

## Summary

ElevenLabs Music generates music from text prompts via the ElevenLabs API, priced at $0.15 per minute of generated audio with a 5-minute cap per generation [[elevenlabs-music-0-15-per-minute-5-minute-cap-studio-games-plan-restriction-9f14fd6d]]. Commercial use is allowed on all paid ElevenLabs plans **except** the Studio Games plan on self-serve tiers — a meaningful restriction for indie game developers who may be on that plan.

> ElevenLabs Music generates music from text prompts via the music generation API. Pricing is $0.15 per minute of generated music, with a 5-minute cap per generation. Commercial use is allowed on all paid plans except Studio Games on self-serve plans.

**Music v2.5** (`music_v2_5`) is now the default model in ElevenMusic, replacing Music v2 as the default. In a blind test across 47,885 pairs, v2.5 was preferred the majority of the time — with the largest gap in vocal-led and acoustic-heavy genres [[elevenlabs-introduces-music-v2-5-its-best-music-model-yet-e742a57d]]. Music v2 (`music_v2`) remains available. The older `music_v1` model is deprecated and will be removed January 31, 2027 — migrate to `music_v2_5` for continued service [[elevenlabs-introduces-music-v2-5-its-best-music-model-yet-e742a57d]].

> ElevenLabs introduces Music v2.5, its best performing music model yet. Music v2.5 is now the default for prompted and reference generation in ElevenMusic. [[elevenlabs-introduces-music-v2-5-its-best-music-model-yet-e742a57d]]

> The music_v1 model is deprecated and will be removed on January 31, 2027. Please migrate to music_v2_5 for continued service. [[elevenlabs-introduces-music-v2-5-its-best-music-model-yet-e742a57d]]

This is a distinct entity from [[elevenlabs]] (which covers ElevenLabs' voice/TTS models under `modality: voice`).

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-25)_

## Open questions

- [x] Model id(s) for the music generation endpoint — resolved: `music_v2_5` (default, 2026-11-08) and `music_v2` [[elevenlabs-introduces-music-v2-5-its-best-music-model-yet-e742a57d]].
- [ ] Arena placement (any music generation benchmark).
- [ ] Whether the Studio Games restriction applies to enterprise plan customers as well.

## See also

- [[audio-tools]]
- [[elevenlabs]]
- [[generative-media-models]]
- [[game-music]]
