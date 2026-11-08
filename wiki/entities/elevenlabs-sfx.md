---
title: "ElevenLabs SFX"
kind: entity
aliases: ["ElevenLabs Sound Effects", "ElevenLabs SFX v3", "eleven_text_to_sound_v3"]
sources:
  - "[[sfx-v3-api-generate-sound-effects-from-multi-part-prompts-6992a7c6]]"
last_updated: 2026-11-08
last_verified: 2026-11-08
freshness_window_days: 30
profile: tool
modality: sfx
tasks: ["text-to-sfx"]
vendor: "ElevenLabs"
model_ids: ["eleven_text_to_sound_v3"]
access: ["api"]
open_weights_license: unknown
hardware_floor: unknown
pricing: "40 credits/second when duration specified; duration 0.5–30s (2026-11-08)"
pricing_source: "[[sfx-v3-api-generate-sound-effects-from-multi-part-prompts-6992a7c6]]"
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[sfx-v3-api-generate-sound-effects-from-multi-part-prompts-6992a7c6]]"
last_release: 2026-11-08
arena_rank: []
arena_rank_source: []
---

# ElevenLabs SFX

## Summary

ElevenLabs SFX v3 (`eleven_text_to_sound_v3`) is ElevenLabs' sound-effect generation model, available in ElevenCreative and the ElevenLabs API [[sfx-v3-api-generate-sound-effects-from-multi-part-prompts-6992a7c6]]. It follows multi-part prompts — listing events in the order they should occur — more closely than its predecessor. Pricing is 40 credits per second when a duration is specified, with duration ranging from 0.5 to 30 seconds.

> The API model ID is eleven_text_to_sound_v3. Pricing is 40 credits per second when a duration is specified; duration ranges from 0.5 to 30 seconds, with prompt_influence defaulting to 0.3. [[sfx-v3-api-generate-sound-effects-from-multi-part-prompts-6992a7c6]]

> The eleven_text_to_sound_v2 model is deprecated and will be removed on March 1, 2027. Its replacement is eleven_text_to_sound_v3. [[sfx-v3-api-generate-sound-effects-from-multi-part-prompts-6992a7c6]]

This is a distinct entity from [[elevenlabs]] (voice/TTS), [[eleven-music]] (music generation), and from the parent company entity [[elevenlabs]].

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-11-08)_

## Open questions

- [ ] Commercial-use terms: no ingested source states whether SFX v3 output can be shipped in a commercial game product.
- [ ] Credit-to-USD conversion: pricing stated in ElevenLabs credits; exact dollar cost per second of SFX output not stated.
- [ ] Arena placement: no benchmark board has ranked ElevenLabs SFX v3 yet.

## See also

- [[audio-tools]]
- [[elevenlabs]]
- [[eleven-music]]
- [[generative-media-models]]
