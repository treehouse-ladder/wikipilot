---
title: "Inworld Realtime TTS-2"
kind: entity
aliases: ["Realtime TTS-2", "Inworld TTS", "Inworld TTS-2"]
sources:
  - "[[realtime-tts-2-a-new-frontier-voice-model-that-feels-as-real-as-you-68a9e733]]"
  - "[[bringing-personality-to-pixels-inworld-levels-up-game-characters-using-generative-ai-4d8d4bbc]]"
last_updated: 2026-10-25
last_verified: 2026-10-24
freshness_window_days: 30
profile: tool
modality: voice
tasks: ["text-to-speech", "realtime-conversational-tts", "voice-direction", "multilingual"]
vendor: "Inworld"
model_ids: ["realtime-tts-2"]
access: ["api"]
open_weights_license: unknown
hardware_floor: unknown
pricing: unknown
pricing_source: null
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[realtime-tts-2-a-new-frontier-voice-model-that-feels-as-real-as-you-68a9e733]]"
last_release: unknown
arena_rank: ["Artificial Analysis Speech Arena (realtime TTS): #1 (2026-06-11)"]
arena_rank_source: ["[[realtime-tts-2-a-new-frontier-voice-model-that-feels-as-real-as-you-68a9e733]]"]
---

# Inworld Realtime TTS-2

## Summary

Realtime TTS-2 is Inworld's conversational voice model: it conditions on prior turns so tone and pacing carry forward, holds one voice identity across 100+ languages, and takes inline plain-English "Voice Direction" tags (e.g. `[speak sadly, as if something bad just happened]`) passed in the text at inference time rather than a fixed emotion enum [[realtime-tts-2-a-new-frontier-voice-model-that-feels-as-real-as-you-68a9e733]]. Inworld reports it as #1 realtime TTS by real-user votes on the Artificial Analysis Speech Arena with sub-130 ms first-chunk latency; the per-million-character price in the ingested excerpt is garbled ("down to 0"), so `pricing` is `unknown` [[realtime-tts-2-a-new-frontier-voice-model-that-feels-as-real-as-you-68a9e733]].

> #1 realtime TTS by real users on the Artificial Analysis Speech Arena with sub-130ms first-chunk latency

An earlier NVIDIA post (May 2026) already placed Inworld's TTS at #1 on Artificial Analysis with sub-200 ms latency, voice cloning and multilingual support, as part of the Inworld platform used by indie teams and studios such as Ubisoft [[bringing-personality-to-pixels-inworld-levels-up-game-characters-using-generative-ai-4d8d4bbc]].

> Inworld's TTS is ranked #1 on Artificial Analysis, with sub-200ms latency, voice cloning, and multilingual support.

## Disputes

- Entity Summary and quote block claim "sub-130 ms first-chunk latency" citing [[realtime-tts-2-a-new-frontier-voice-model-that-feels-as-real-as-you-68a9e733]]; the re-ingested version of that source (fetched 2026-10-24) states "Sub-200ms median time-to-first-audio for the TTS layer alone" — the sub-130ms figure was one of the claims flagged as no longer on the live page in the 2026-10-24 manual re-ingest log entry. Status: unresolved (confidence: high; sweep: 2026-10-25) — the entity still carries sub-130ms; the other source cited on this page ([[bringing-personality-to-pixels-inworld-levels-up-game-characters-using-generative-ai-4d8d4bbc]], May 2026) already reported sub-200ms, making this a confirmed two-source inconsistency.

> From entity Summary/quote block: "#1 realtime TTS by real users on the Artificial Analysis Speech Arena with sub-130ms first-chunk latency" [[realtime-tts-2-a-new-frontier-voice-model-that-feels-as-real-as-you-68a9e733]]

> From source [[realtime-tts-2-a-new-frontier-voice-model-that-feels-as-real-as-you-68a9e733]] (fetched 2026-10-24): "Sub-200ms median time-to-first-audio for the TTS layer alone."

## Open questions

- [ ] Per-million-character pricing (the figure is unreadable in the ingested excerpt; re-fetch inworld.ai pricing).
- [ ] Commercial-use / licensing terms for generated voices in shipped games.
- [ ] Release date of Realtime TTS-2.
- [ ] Is it reachable via fal / Replicate as well as Inworld's own API?

## See also

- [[generative-media-models]]
- [[audio-tools]]
- [[elevenlabs]]
- [[audio2face]]
