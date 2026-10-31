---
title: "MiniMax Music"
kind: entity
aliases: ["MiniMax Music 2.6", "Hailuo Music", "fal-ai/minimax-music"]
sources:
  - "[[minimax-music-2-6-text-to-audio-api-on-fal-ff196b6a]]"
last_updated: 2026-10-31
last_verified: 2026-10-31
freshness_window_days: 30
profile: tool
modality: music
tasks: ["text-to-music", "lyrics-to-music", "instrumental-generation"]
vendor: "MiniMax"
model_ids: ["fal:fal-ai/minimax-music/v2.6"]
access: ["fal"]
open_weights_license: unknown
hardware_floor: unknown
pricing: "$0.15 per generated audio (fal, 2026-10-31)"
pricing_source: "[[minimax-music-2-6-text-to-audio-api-on-fal-ff196b6a]]"
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[minimax-music-2-6-text-to-audio-api-on-fal-ff196b6a]]"
last_release: unknown
arena_rank: []
arena_rank_source: []
---

# MiniMax Music

## Summary

MiniMax Music 2.6 generates complete music tracks — singing, backing music, and detailed arrangements — from lyrics and a style description using structure tags such as `[Verse]`, `[Chorus]`, `[Bridge]`, and `[Outro]` [[minimax-music-2-6-text-to-audio-api-on-fal-ff196b6a]]. It also supports `is_instrumental: true` for vocal-free arrangements from the style prompt alone. Audio output is configurable up to 44.1 kHz / 256 kbps as MP3, WAV, or PCM.

**Access caveat:** MiniMax's own Music Generation and Lyrics Generation APIs are **no longer available to new users since 2026-08-20** [[minimax-music-2-6-text-to-audio-api-on-fal-ff196b6a]], making fal the practical route for new users. On fal, pricing is **$0.15 per generated audio**.

> MiniMax Music 2.6 creates complete tracks with singing, backing music, and detailed arrangements from lyrics and a style description. Lyrics use structure tags such as [Verse], [Chorus], [Bridge], and [Outro].

> MiniMax's own docs state that starting August 20, 2026, the paid Music Generation and Lyrics Generation APIs are no longer available to new users, making fal the practical route for new users.

> On fal, MiniMax Music 2.6 is priced at $0.15 per generated audio.

## Open questions

- [ ] Is the `$0.15/generation` price on fal capped by duration, or is it per request regardless of output length?
- [ ] MiniMax's direct API is closed to new users since 2026-08-20 — are there plans to reopen it, or is fal the permanent access path?

## See also

- [[generative-media-models]]
- [[minimax-music-2-6-text-to-audio-api-on-fal-ff196b6a]]

_no contradictions or gaps known yet (last reviewed: 2026-10-31)_
