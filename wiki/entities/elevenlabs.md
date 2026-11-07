---
title: "ElevenLabs"
kind: entity
aliases: ["Eleven Labs", "Eleven v3", "elevenlabs.io"]
sources:
  - "[[ai-voice-for-games-elevenlabs-31e6ac62]]"
  - "[[eleven-v4-our-most-expressive-text-to-speech-ai-model-yet-028b20a4]]"
last_updated: 2026-11-07
last_verified: 2026-11-07
freshness_window_days: 30
profile: tool
modality: voice
tasks: ["text-to-speech", "multilingual", "npc-voice"]
vendor: "ElevenLabs"
model_ids: ["eleven-v3", "eleven-v4", "eleven-v4-turbo"]
access: ["api"]
open_weights_license: unknown
hardware_floor: unknown
pricing: "credit-based: 1 credit/char; free 10k credits/mo, paid from $6/mo for 30k credits; Eleven v4 API ~$0.08/min, v4 Turbo ~$0.04/min (per-minute figures conflict across pages) (2026-11-07)"
pricing_source: "[[eleven-v4-our-most-expressive-text-to-speech-ai-model-yet-028b20a4]]"
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[ai-voice-for-games-elevenlabs-31e6ac62]]"
last_release: 2026-09-28
arena_rank: []
arena_rank_source: []
---

# ElevenLabs

## Summary

ElevenLabs sells multilingual AI voice generation for game worlds, NPCs and interactive content; its current model is Eleven v3, pitched on human-like emotion, timing and nuance, and the product is designed for integration with Unreal Engine [[ai-voice-for-games-elevenlabs-31e6ac62]].

> ElevenLabs has released Eleven v3, a text-to-speech model that performs text with human-like emotion, timing, and nuance. The AI voice technology is designed for easy integration with Unreal Engine.

The single ingested source is the vendor's gaming use-case page [[ai-voice-for-games-elevenlabs-31e6ac62]]. It does not name an API, pricing, plan-based commercial terms or any arena placement, so those fields are `unknown` — the first roster sweep should cite elevenlabs.io pricing/docs to fill them.

**Eleven v4 + v4 Turbo (launched 2026-09-28) are now ElevenLabs' current flagship TTS, superseding Eleven v3.** Eleven v4 is "our latest and most advanced Text to Speech model, and the first in a new generation of models"; the real-time variant Eleven v4 Turbo returns first audio at ~100 ms median latency (median time to first speech ~150 ms) and supports 90+ languages [[eleven-v4-our-most-expressive-text-to-speech-ai-model-yet-028b20a4]]. Both are available in ElevenAgents, ElevenCreative and via the ElevenAPI, billed at one credit per character — free tier 10,000 credits/mo, paid from $6/mo for 30,000 credits; one API page lists ~$0.04/min for v4 Turbo and ~$0.08/min for v4 (per-minute figures conflict across ElevenLabs pages) [[eleven-v4-our-most-expressive-text-to-speech-ai-model-yet-028b20a4]]. The v4 Turbo ~100 ms latency makes ElevenLabs a direct competitor to [[inworld-realtime-tts-2]] for in-game conversational NPC voice.

> Eleven v4 is our latest and most advanced Text to Speech model, and the first in a new generation of models. [[eleven-v4-our-most-expressive-text-to-speech-ai-model-yet-028b20a4]]

> Eleven v4 and v4 Turbo are available now in ElevenAgents, ElevenCreative, and via the ElevenAPI. [[eleven-v4-our-most-expressive-text-to-speech-ai-model-yet-028b20a4]]

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-24)_

## Open questions

- [ ] Reconcile Eleven v4 / v4 Turbo per-minute API rates (~$0.08 / ~$0.04 per min) with the credit-based pricing model ($6/mo per 30k credits, 1 credit/char) — ElevenLabs pages conflict [[eleven-v4-our-most-expressive-text-to-speech-ai-model-yet-028b20a4]].
- [ ] Update `model_ids` frontmatter to add `eleven-v4` and `eleven-v4-turbo`, and `access` to include `api` (confirmed by the Eleven v4 launch blog) [[eleven-v4-our-most-expressive-text-to-speech-ai-model-yet-028b20a4]].
- [ ] Access path on record (API / SDK / Unreal plugin) — not stated in the ingested page, so `access` is `["unknown"]`.
- [ ] Pricing per plan and per-character cost.
- [ ] Commercial-use terms for generated voices by plan tier.
- [ ] Artificial Analysis Speech Arena placement relative to [[inworld-realtime-tts-2]].
- [ ] Eleven v3 release date.

## See also

- [[generative-media-models]]
- [[audio-tools]]
- [[inworld-realtime-tts-2]]
- [[eleven-music]]
