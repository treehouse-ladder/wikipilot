---
title: Generative media models
kind: topic
sources: ["[[minimaxai-minimax-h3-hugging-face-1f0e60fd]]", "[[minimax-releases-minimax-h3-an-omni-modal-video-model-that-generates-15-second-2k-clips-with-native-stereo-audio-53db5121]]", "[[realtime-tts-2-a-new-frontier-voice-model-that-feels-as-real-as-you-68a9e733]]", "[[ai-voice-for-games-elevenlabs-31e6ac62]]"]
last_updated: 2026-10-24
last_verified: 2026-10-24
freshness_window_days: 30
---

# Generative media models

See [purpose](purpose.md) for the topic charter (in-scope / out-of-scope) and
`CLAUDE.md` "Cross-cutting relevance criteria" for the meta-bar.

## Summary

This topic tracks the current lineup of models that generate images, video, music, sound effects and speech — how each is reached (vendor API, fal.ai, Replicate, open weights), what it costs, under what commercial-use terms its output may ship in a game, and where it sits on arena boards with methodology. Every model is an entity page with a machine-readable tool profile (`profile: tool`) — currently [[minimax-h3]], [[inworld-realtime-tts-2]] and [[elevenlabs]] — and the per-modality comparison pages ([[audio-tools]] today) aggregate those profiles. The topic was created on 2026-10-24 and seeded only from sources already in the wiki, so coverage of image, music and SFX models is empty until the first daily run.

**Video.** The only video model with a source in the wiki is MiniMax H3, an omni-modal model that generates 15-second 2K clips with native stereo audio from unified text / image / video / audio context, released as two open-weight checkpoints under the MiniMax H3 Community License and ranked #1 Video Editing, #2 Text-to-Video and #3 Image-to-Video on the Artificial Analysis boards at the time of the model card [[minimaxai-minimax-h3-hugging-face-1f0e60fd]] [[minimax-releases-minimax-h3-an-omni-modal-video-model-that-generates-15-second-2k-clips-with-native-stereo-audio-53db5121]]. Its absolute per-second price is not recorded (the launch coverage gives only relative figures).

> On the Artificial Analysis leaderboards H3 ranks #1 in Video Editing, #2 in Text-to-Video, and #3 in Image-to-Video.

> At 2K, H3's per-second price is less than a third of mainstream models; at 768p, less than half the price of mainstream 720p.

**Speech.** Inworld's Realtime TTS-2 targets in-game conversational use with sub-130 ms first-chunk latency, inline plain-language voice direction and one voice identity across 100+ languages, and was #1 realtime TTS on the Artificial Analysis Speech Arena at launch [[realtime-tts-2-a-new-frontier-voice-model-that-feels-as-real-as-you-68a9e733]]; ElevenLabs (Eleven v3) targets multilingual NPC voice with an Unreal Engine integration [[ai-voice-for-games-elevenlabs-31e6ac62]]. Both are speech entities in [[audio-tools]]; their pricing and commercial-use terms are open questions.

> #1 realtime TTS by real users on the Artificial Analysis Speech Arena with sub-130ms first-chunk latency

> ElevenLabs has released Eleven v3, a text-to-speech model that performs text with human-like emotion, timing, and nuance. The AI voice technology is designed for easy integration with Unreal Engine.

**Image, music, SFX, sprites.** No sources yet. The researcher's first runs should seed the `image-tools` and `video-tools` comparison pages once at least two tool entities per modality exist; the 3D and motion side of the same tool roster is owned by [[ai-in-game-dev]] (see [[3d-tools]] and [[rig-and-motion-tools]]).

## Recent updates

### Updates 2026-10-24

Topic created. Seeded three speech/video tool entities ([[minimax-h3]], [[inworld-realtime-tts-2]], [[elevenlabs]]) from sources previously ingested under `ai-in-game-dev`, and the `audio-tools` comparison page. No new sources ingested.

## Disputes

_(none yet)_

## Open questions

- [ ] What is the current #1 on the arena.ai text-to-image board, and does Artificial Analysis' image arena agree?
- [ ] Which text-to-music models (Suno, Udio, Lyria, Stable Audio) permit shipping output in a commercial game on a non-enterprise plan, as of this month?
- [ ] What are the per-second prices for MiniMax H3 on the MiniMax API vs fal.ai, and does the open-weight license permit commercial game use?
- [ ] Which sprite / pixel-art generators (PixelLab, Retro Diffusion, Scenario) expose a public API, and at what price?

## See also

- [[audio-tools]]
- [[ai-in-game-dev]]
- [[frontier-models]]
- [[game-music]]
