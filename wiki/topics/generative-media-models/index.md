---
title: Generative media models
kind: topic
sources: ["[[minimaxai-minimax-h3-hugging-face-1f0e60fd]]", "[[minimax-releases-minimax-h3-an-omni-modal-video-model-that-generates-15-second-2k-clips-with-native-stereo-audio-53db5121]]", "[[realtime-tts-2-a-new-frontier-voice-model-that-feels-as-real-as-you-68a9e733]]", "[[ai-voice-for-games-elevenlabs-31e6ac62]]", "[[gpt-image-2-5-flare-and-sunburst-released-by-openai-cf34266e]]", "[[nano-banana-2-lite-google-deepmind-image-generation-at-0-034-1k-images-3eac9764]]", "[[ideogram-3-0-launches-with-open-weights-model-and-commercial-license-1f773818]]", "[[kling-4-0-and-4-0-flash-video-generation-models-launch-b0391b87]]", "[[seedance-wins-artificial-analysis-image-to-video-with-audio-output-benchmark-1-a7869d54]]", "[[elevenlabs-music-0-15-per-minute-5-minute-cap-studio-games-plan-restriction-9f14fd6d]]", "[[pixellab-sprite-generation-mcp-server-for-claude-code-1195a2d7]]", "[[retro-diffusion-pixel-art-generation-from-0-03-per-image-mcp-server-available-0746b611]]", "[[scenario-mcp-server-for-claude-code-codex-and-cursor-9bf7b8e5]]", "[[flux-3-image-maximum-control-over-every-pixel-37948658]]", "[[flux-3-image-klein-open-weights-5-6b-parameters-155c7b54]]", "[[flux-3-max-text-and-image-to-video-post-trained-by-fal-4991600a]]", "[[introducing-seedance-2-5-78d1ddb7]]", "[[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]", "[[aa-image-t2i-v2-1-leaderboard-top-ai-image-models-634924f7]]", "[[text-to-image-leaderboard-best-ai-image-generators-ba150d9e]]", "[[what-to-know-about-the-sora-discontinuation-4d8dc7c1]]", "[[licensing-ideogram-bdab80bb]]", "[[ideogram-text-to-image-api-on-fal-7cd91f04]]", "[[kling-api-pricing-fba30089]]", "[[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]]", "[[wan-3-0-text-to-video-api-on-fal-581fd1f9]]", "[[aa-video-editing-v1-1-leaderboard-top-ai-video-models-1743cee9]]", "[[seedance-2-5-us-image-to-video-api-on-fal-f520e761]]", "[[shengshu-technology-launches-vidu-q4-preview-a-next-generation-ai-video-model-built-for-lifelike-performances-b956992b]]", "[[tencent-opens-hy-nomas-an-interactive-video-world-model-running-on-one-rtx-4090-7543a82b]]", "[[vidu-q4-preview-aa-video-i2v-debut-38fa453c]]", "[[aa-video-i2v-v2-1-leaderboard-top-ai-video-models-7458c112]]", "[[suno-mcp-beta-fbbc54a2]]", "[[minimax-music-2-6-text-to-audio-api-on-fal-ff196b6a]]", "[[introducing-pika-h3-flex-0a7ab440]]", "[[pika-on-x-meet-pika-h3-flex-96454635]]", "[[runway-dev-plugins-for-coding-agents-35216bb0]]", "[[introducing-images-2-6-295354ff]]", "[[gpt-image-2-6-sunburst-model-e5a487dd]]", "[[minimax-h3-highspeed-video-generation-5b521e7c]]", "[[nano-banana-2-1-model-card-google-deepmind-2783cdec]]", "[[eleven-v4-our-most-expressive-text-to-speech-ai-model-yet-028b20a4]]", "[[can-i-distribute-my-songs-to-spotify-etc-25684551]]", "[[sfx-v3-api-generate-sound-effects-from-multi-part-prompts-6992a7c6]]", "[[elevenlabs-introduces-music-v2-5-its-best-music-model-yet-e742a57d]]"]
last_updated: 2026-11-08
last_verified: 2026-11-08
freshness_window_days: 30
---

# Generative media models

See [purpose](purpose.md) for the topic charter (in-scope / out-of-scope) and
`CLAUDE.md` "Cross-cutting relevance criteria" for the meta-bar.

## Summary

This topic tracks the current lineup of models that generate images, video, music, sound effects and speech — how each is reached (vendor API, fal.ai, Replicate, open weights), what it costs, under what commercial-use terms its output may ship in a game, and where it sits on arena boards with methodology. Every model is an entity page with a machine-readable tool profile (`profile: tool`), and the per-modality comparison pages aggregate those profiles ([[audio-tools]] today; the 3D and rig/motion side of the roster is owned by [[ai-in-game-dev]] via [[3d-tools]] and [[rig-and-motion-tools]]).

**Image.** The current board leader is **OpenAI GPT Image 2.5 Sunburst (max)** — #1 on AA-Image-T2I v2.1 (Elo 1196) and AA-Image-Editing v2.1 (Elo 1199) [[aa-image-t2i-v2-1-leaderboard-top-ai-image-models-634924f7]] and #1 on arena.ai (Elo 1425) [[text-to-image-leaderboard-best-ai-image-generators-ba150d9e]]. OpenAI has since shipped **GPT Image 2.6 (Flare + Sunburst)** as its current API offering on [[gpt-image]] (`gpt-image-2.6-sunburst` at $30/1M output tokens), but 2.6 is not yet ranked on the AA boards, so 2.5 Sunburst remains the measured #1 [[introducing-images-2-6-295354ff]] [[gpt-image-2-6-sunburst-model-e5a487dd]]. A new, distinct image model — **[[nano-banana-2-1]] (Google DeepMind Nano Banana 2.1, on Gemini 3.6 Flash)** — has entered the lineup; it is *not* the already-tracked [[nano-banana]] (Nano Banana 2 Lite = `gemini-3.1-flash-image`, on Gemini 3.1 Flash) [[nano-banana-2-1-model-card-google-deepmind-2783cdec]]. Nano Banana 2.1 sits ~Elo 1176 T2I / ~1152 editing on an Artificial Analysis snapshot — below GPT Image 2.5 Sunburst — but the figure is unconfirmed against the live board [[nano-banana-2-1-model-card-google-deepmind-2783cdec]]. Open-weights image generation is anchored by **FLUX 3 Image Klein** (5.6B params, from $0.009/1K images on the BFL API) [[flux-3-image-klein-open-weights-5-6b-parameters-155c7b54]]; [[flux]] (FLUX 3 Image) and [[ideogram]] (Ideogram 3.0) round out the image roster.

> The text-to-image board has GPT Image 2.5 Sunburst (max) in first, at Elo 1196 across 13,586 comparisons. Sunburst also leads Artificial Analysis's image editing board, at Elo 1199. [[aa-image-t2i-v2-1-leaderboard-top-ai-image-models-634924f7]]

> Nano Banana 2.1 is based on Gemini 3.6 Flash. [[nano-banana-2-1-model-card-google-deepmind-2783cdec]]

**Video.** Text-to-video and video-editing are led by **[[wan-3]] (Wan 3.0, Alibaba)** — #1 on AA-Video-T2V v2.1 (with audio, Elo 1174) and #1 on AA-Video-Editing v1.1 (Elo 1198), available on fal at $0.05–$0.20/s by resolution [[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]] [[aa-video-editing-v1-1-leaderboard-top-ai-video-models-1743cee9]] [[wan-3-0-text-to-video-api-on-fal-581fd1f9]]. Image-to-video is led by **[[seedance]] (Dreamina Seedance 2.5)** — #1 on the updated AA-Video-I2V v2.1 board (Elo 1152) as of 2026-10-31, reachable on fal under `bytedance/seedance-2.5/us` (~$0.47/s at 720p) [[aa-video-i2v-v2-1-leaderboard-top-ai-video-models-7458c112]] [[seedance-2-5-us-image-to-video-api-on-fal-f520e761]]. The open-weights video leader is **[[minimax-h3]] (MiniMax H3 768p)** — #1 among open weights on both AA-Video-T2V v2.1 (Elo 1158, #3 overall) and AA-Video-I2V v2.1 (Elo 1129, #4 overall), under the MiniMax H3 Community License [[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]] [[aa-video-i2v-v2-1-leaderboard-top-ai-video-models-7458c112]]; [[pika-h3-flex]] (open-weights LoRA adapters on the H3 base) is #1 open-weights / #7 overall on DesignArena's separate t2v board (Elo 1293) [[pika-on-x-meet-pika-h3-flex-96454635]]. [[flux-3-max]] (BFL/fal, $0.085/s), [[kling]] (Kling 4.0), [[vidu-q4-preview]] (4K, commercial API) and the open-weights interactive world model [[hy-nomas]] extend the roster; [[sora]] is shut down (API discontinued 2026-09-24).

> Wan 3.0 currently leads AA-Video-T2V v2.1 with an Elo score of 1174. [[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]]

> Dreamina Seedance 2.5 currently leads AA-Video-I2V v2.1 with an Elo score of 1152. [[aa-video-i2v-v2-1-leaderboard-top-ai-video-models-7458c112]]

**Speech / TTS.** Two models now compete head-to-head for in-game conversational NPC voice. **[[inworld-realtime-tts-2]]** targets realtime use with sub-130 ms first-chunk latency, inline plain-language voice direction and one voice identity across 100+ languages, and was #1 realtime TTS on the Artificial Analysis Speech Arena at launch [[realtime-tts-2-a-new-frontier-voice-model-that-feels-as-real-as-you-68a9e733]]. **[[elevenlabs]]**'s flagship is now **Eleven v4 + v4 Turbo** (launched 2026-09-28, superseding Eleven v3) — the v4 Turbo real-time variant returns first audio at ~100 ms median latency across 90+ languages, making it a direct NPC-voice competitor to Inworld [[eleven-v4-our-most-expressive-text-to-speech-ai-model-yet-028b20a4]]. Both are speech entities in [[audio-tools]].

> Eleven v4 is our latest and most advanced Text to Speech model, and the first in a new generation of models. [[eleven-v4-our-most-expressive-text-to-speech-ai-model-yet-028b20a4]]

**Music / SFX.** **[[suno]]** music is now confirmed game-shippable: songs made while subscribed to a Pro or Premier plan are granted commercial-use rights and can be distributed to Spotify/Apple Music via any distributor (Pro 20 downloads/mo, Premier 60/mo; free-plan songs cannot be monetized and there is no retroactive license) [[can-i-distribute-my-songs-to-spotify-etc-25684551]]. Other music options: [[eleven-music]] (ElevenLabs Music, $0.15/min with a 5-min cap, commercial on all paid plans *except* Studio Games on self-serve) — its default model is now **Music v2.5** (`music_v2_5`), preferred a majority of the time over v2 in a 47,885-pair blind test (largest gains on vocal-led and acoustic-heavy genres), with `music_v2` still available [[elevenlabs-introduces-music-v2-5-its-best-music-model-yet-e742a57d]] [[elevenlabs-music-0-15-per-minute-5-minute-cap-studio-games-plan-restriction-9f14fd6d]] — and [[minimax-music]] (MiniMax Music 2.6, $0.15/generated audio on fal) [[minimax-music-2-6-text-to-audio-api-on-fal-ff196b6a]]. For sound effects, **[[elevenlabs-sfx]] (ElevenLabs SFX v3, `eleven_text_to_sound_v3`)** is the first `modality: sfx` entity on this topic: now the default model in ElevenCreative Sound Effects/Studio/Flows and available to every workspace via API, it improves multi-part prompt following and is priced at 40 credits/second when a duration (0.5–30 s) is specified [[sfx-v3-api-generate-sound-effects-from-multi-part-prompts-6992a7c6]].

> Songs made while subscribed (to a Pro or Premier plan) are granted commercial use rights. This allows you to distribute songs to Spotify, Apple Music, etc, using the distributor of your choice. [[can-i-distribute-my-songs-to-spotify-etc-25684551]]

> ElevenLabs introduces Music v2.5, its best performing music model yet. Music v2.5 is now the default for prompted and reference generation in ElevenMusic. [[elevenlabs-introduces-music-v2-5-its-best-music-model-yet-e742a57d]]

> Introducing SFX v3 in ElevenCreative and ElevenAPI. SFX v3 is now available to every workspace. In ElevenCreative, SFX v3 is the default model in Sound Effects, Studio and Flows. [[sfx-v3-api-generate-sound-effects-from-multi-part-prompts-6992a7c6]]

**3D / sprites.** Sprite/pixel-art generation is covered by MCP-server tools [[pixellab]] (from $0.001/image) [[pixellab-sprite-generation-mcp-server-for-claude-code-1195a2d7]], [[retro-diffusion]] (pixel art, from $0.03/image) and [[scenario]] (game-ready sprites, MCP for Claude Code/Codex/Cursor); the 3D and rig/motion side of the asset roster is owned by [[ai-in-game-dev]] (see [[3d-tools]] and [[rig-and-motion-tools]]).

**Best practices for game-dev asset pipelines.** Favor models that drop into an agentic workflow: Suno, Runway Dev, PixelLab, Retro Diffusion and Scenario all expose MCP servers compatible with Claude Code / Codex. For commercially shippable assets, the cleanest documented licenses today are [[suno]] music on a Pro/Premier plan, Ideogram's commercial API outputs, and FLUX 3 Image Klein open weights — always confirm per-model commercial-use terms before shipping.

**Key open caveats.** Nano Banana 2.1's exact Gemini model id, per-image pricing and AA Elo remain unconfirmed [[nano-banana-2-1-model-card-google-deepmind-2783cdec]]; Eleven v4 / v4 Turbo per-minute pricing conflicts across ElevenLabs pages and commercial-use terms by plan tier are unstated [[eleven-v4-our-most-expressive-text-to-speech-ai-model-yet-028b20a4]]; several image models' (GPT Image 2.x, Nano Banana) game-shipping commercial terms are unstated; the reported ByteDance Seedance 1.5 Pro retirement (2026-11-11) is still unconfirmed by a primary source; and two ElevenLabs legacy models are on deprecation countdowns — `music_v1` is removed January 31, 2027 and `eleven_text_to_sound_v2` is removed March 1, 2027, so pipelines should migrate to `music_v2_5` / `eleven_text_to_sound_v3` [[elevenlabs-introduces-music-v2-5-its-best-music-model-yet-e742a57d]] [[sfx-v3-api-generate-sound-effects-from-multi-part-prompts-6992a7c6]].

## Recent updates

### Updates 2026-11-08

**ElevenLabs ships SFX v3 and Music v2.5; `music_v1` enters deprecation countdown.** ElevenLabs launched two model updates on the same day, covering both its sound-effects and music modalities. **SFX v3** (`eleven_text_to_sound_v3`) is now the default model in Sound Effects, Studio and Flows on ElevenCreative, and is available to all workspaces via API; it improves multi-part prompt following (events are listed in sequence order) over SFX v2 — pricing is 40 credits/second when a duration is specified (0.5–30 s, `prompt_influence` defaults to 0.3) [[sfx-v3-api-generate-sound-effects-from-multi-part-prompts-6992a7c6]]. This warrants a **new entity page [[elevenlabs-sfx]]** — the first `modality: sfx` entity tracked on this topic. `eleven_text_to_sound_v2` is deprecated and will be removed March 1, 2027 [[sfx-v3-api-generate-sound-effects-from-multi-part-prompts-6992a7c6]]. Separately, **Music v2.5** (`music_v2_5`) is now the default music model in ElevenMusic — ElevenLabs ran a blind test across 47,885 pairs and v2.5 was preferred a majority of the time, with the largest gain in vocal-led and acoustic-heavy genres; `music_v2` remains available; `music_v1` is deprecated with removal on January 31, 2027 [[elevenlabs-introduces-music-v2-5-its-best-music-model-yet-e742a57d]]. The [[eleven-music]] entity page has been updated with `model_ids: ["music_v2_5", "music_v2"]` and the open question on model identifiers is now resolved.

> Introducing SFX v3 in ElevenCreative and ElevenAPI. SFX v3 is now available to every workspace. In ElevenCreative, SFX v3 is the default model in Sound Effects, Studio and Flows. [[sfx-v3-api-generate-sound-effects-from-multi-part-prompts-6992a7c6]]

> ElevenLabs introduces Music v2.5, its best performing music model yet. Music v2.5 is now the default for prompted and reference generation in ElevenMusic. [[elevenlabs-introduces-music-v2-5-its-best-music-model-yet-e742a57d]]

### Updates 2026-11-07

**New image model: [[nano-banana-2-1]] (Google DeepMind, Nano Banana 2.1 on Gemini 3.6 Flash).** Google DeepMind published a model card for Nano Banana 2.1, a text-to-image + image-editing model "based on Gemini 3.6 Flash" that "outperforms previous Nano Banana models to deliver better visual design, mask-based editing, subject consistency, and more natural-looking images" [[nano-banana-2-1-model-card-google-deepmind-2783cdec]]. It is distinct from the already-tracked [[nano-banana]] (Nano Banana 2 Lite = `gemini-3.1-flash-image`, on Gemini 3.1 Flash); the DeepMind model-cards index lists Nano Banana 2.1 as updated 2026-10-06 [[nano-banana-2-1-model-card-google-deepmind-2783cdec]]. An Artificial Analysis snapshot places it at ~Elo 1176 on AA-Image-T2I v2.1 and ~Elo 1152 on AA-Image-Editing v2.1 — below the current image leader GPT Image 2.5 Sunburst (Elo 1196) — but the leaderboard captures conflict and the figure needs confirmation against the live board [[nano-banana-2-1-model-card-google-deepmind-2783cdec]]. Pricing, the exact Gemini API model id, and commercial-use terms are not stated.

> Nano Banana 2.1 is based on Gemini 3.6 Flash. [[nano-banana-2-1-model-card-google-deepmind-2783cdec]]

> It outperforms previous Nano Banana models to deliver better visual design, mask-based editing, subject consistency, and more natural-looking images. [[nano-banana-2-1-model-card-google-deepmind-2783cdec]]

**[[elevenlabs]] flagship moves to Eleven v4 + v4 Turbo (launched 2026-09-28).** ElevenLabs' current TTS flagship is Eleven v4, "our latest and most advanced Text to Speech model, and the first in a new generation of models"; the real-time variant Eleven v4 Turbo returns first audio at ~100 ms median latency (median time to first speech ~150 ms) and supports 90+ languages [[eleven-v4-our-most-expressive-text-to-speech-ai-model-yet-028b20a4]]. Both are available in ElevenAgents, ElevenCreative and via the ElevenAPI, billed at one credit per character — free tier 10,000 credits/mo, paid from $6/mo for 30,000 credits; one API page lists ~$0.04/min for v4 Turbo and ~$0.08/min for v4 (per-minute figures conflict across ElevenLabs pages) [[eleven-v4-our-most-expressive-text-to-speech-ai-model-yet-028b20a4]]. The v4 Turbo ~100 ms latency makes ElevenLabs a direct competitor to [[inworld-realtime-tts-2]] for in-game conversational NPC voice.

> Eleven v4 is our latest and most advanced Text to Speech model, and the first in a new generation of models. [[eleven-v4-our-most-expressive-text-to-speech-ai-model-yet-028b20a4]]

> Eleven v4 and v4 Turbo are available now in ElevenAgents, ElevenCreative, and via the ElevenAPI. [[eleven-v4-our-most-expressive-text-to-speech-ai-model-yet-028b20a4]]

**[[suno]] commercial-use terms confirmed — paid plans grant commercial rights.** Suno's rights page states songs made while subscribed to a Pro or Premier plan "are granted commercial use rights ... to distribute songs to Spotify, Apple Music, etc, using the distributor of your choice"; any song downloaded as a paying subscriber carries commercial rights for commercial or personal use [[can-i-distribute-my-songs-to-spotify-etc-25684551]]. Free-plan songs cannot be monetized and there is no retroactive license (subscribing after creating a song does not license that song); free users get only a limited number of trial downloads for personal, non-commercial use. Under the updated downloads policy, Pro includes 20 downloads/month and Premier 60 downloads/month, both with commercial use rights [[can-i-distribute-my-songs-to-spotify-etc-25684551]]. For an indie game dev this means Suno-generated music is shippable commercially on a non-enterprise paid plan, subject to the per-month download limits.

> Songs made while subscribed (to a Pro or Premier plan) are granted commercial use rights. This allows you to distribute songs to Spotify, Apple Music, etc, using the distributor of your choice. [[can-i-distribute-my-songs-to-spotify-etc-25684551]]

> For any song that you download from the platform as a paying subscriber, you have the commercial rights to the music and can use it for commercial or personal use. [[can-i-distribute-my-songs-to-spotify-etc-25684551]]

**Roster sweep.** Re-confirmed [[suno]] (commercial_use) and [[elevenlabs]] (pricing, status) against vendor pages today. The reported ByteDance Seedance 1.5 Pro retirement (2026-11-11) is still sourced only to a third-party aggregator, not a primary notice — remains unconfirmed.

### Updates 2026-11-06

Quiet run — no new in-scope sources ingested for generative-media-models today. Swept image generators (FLUX 3, GPT Image 2.6, Ideogram 3, Nano Banana), video models (Kling, Seedance, Pika, Wan, MiniMax H3), and audio/3D tools (Suno, ElevenLabs Music, Tripo, Meshy, Rodin). No new material published since the GPT Image 2.6 update on 2026-11-05 met the ingestion bar. ByteDance Seedance 1.5 Pro retirement (expected 2026-11-11) remains unconfirmed by a primary source; track on the next run.

_Note: the wikipilot-qmd index was unreachable this run (CONNECT_TIMEOUT); conceptual-dedupe was done via a direct read of the topic index._

### Updates 2026-11-05

**OpenAI ships GPT Image 2.6 (Flare + Sunburst), released November 4, 2026.** OpenAI released its Images 2.6 generation, with `gpt-image-2.6-flare` and `gpt-image-2.6-sunburst` available in the API and Images 2.6 live in ChatGPT and Codex [[introducing-images-2-6-295354ff]]. Sunburst is the quality-first variant, adding higher-quality generation and greater image consistency across edits at medium/high quality [[introducing-images-2-6-295354ff]]. The developer model page prices `gpt-image-2.6-sunburst` at $30 per 1M output tokens [[gpt-image-2-6-sunburst-model-e5a487dd]]. This supersedes GPT Image 2.5 (Flare/Sunburst) as OpenAI's current image offering on [[gpt-image]]; the 2.6 model is not yet listed on the Artificial Analysis image boards, where GPT Image 2.5 Sunburst (max) remains #1 on AA-Image-T2I v2.1 and AA-Image-Editing v2.1 [[aa-image-t2i-v2-1-leaderboard-top-ai-image-models-634924f7]].

> GPT-Image-2.6 Sunburst and GPT-Image-2.6 Flare are available in the API. Images 2.6 is available in ChatGPT and Codex. [[introducing-images-2-6-295354ff]]

> Price: $30 per 1M output tokens. [[gpt-image-2-6-sunburst-model-e5a487dd]]

**MiniMax H3 vendor/host pricing surfaces on Replicate.** Replicate now hosts [[minimax-h3]] at three 768p tiers — H3 Lite $0.04/s, H3 Highspeed $0.06/s, H3 $0.08/s — with H3 Lite and Highspeed 50% off through year-end; a 10-second Highspeed clip costs $0.60 [[minimax-h3-highspeed-video-generation-5b521e7c]]. This is the first concrete per-second host price for H3 in the wiki, alongside the prior AA-measured $34.12/min.

> MiniMax H3 Lite is $0.04 per second, H3 Highspeed is $0.06 per second, and H3 is $0.08 per second, all at 768P. A 10-second Highspeed video costs $0.60. [[minimax-h3-highspeed-video-generation-5b521e7c]]

### Updates 2026-11-04

**New entity: [[pika-h3-flex]] (Pika Labs).** Pika Labs released Pika H3 Flex on October 29, 2026 — open-weights LoRA adapters built on the [[minimax-h3]] 33B base that cut sampling from 50 steps to 6, enabling faster-than-realtime generation: a 15-second clip with synchronized audio in as little as 7 seconds [[pika-on-x-meet-pika-h3-flex-96454635]]. At launch it debuted **#7 overall and #1 among open-weights models** on DesignArena's text-to-video board (Elo 1293 as of 2026-10-29) [[pika-on-x-meet-pika-h3-flex-96454635]]. Open weights are on Hugging Face (`Pika-Labs/Pika-H3-Flex`) with inference code on GitHub and ComfyUI nodes; Pika tested on a single NVIDIA H100 80GB. The LoRA adapters are distributed under the MiniMax H3 Community License Agreement (see Disputes on [[pika-h3-flex]] for the license conflict). Hosted 4K upscaling and audio stem separation are available only via the Pika API (subscription, pricing unknown) [[introducing-pika-h3-flex-0a7ab440]].

> Meet Pika H3 Flex, debuting today as the #1 open weight model on DesignArena's t2v board. It's built for professional iteration, with exportable audio stems, resolutions up to 4k, and faster-than-realtime generation. It can produce a 15-second clip with soundtrack in as little as 7 sec. [[pika-on-x-meet-pika-h3-flex-96454635]]

> Everything we put into this model was designed to give creators the flexibility and speed to explore with precision. In that spirit, we're making Pika H3 Flex open source from day 1. You can find the code on GitHub, the weights on @huggingface, and start playing with it in @ComfyUI. [[pika-on-x-meet-pika-h3-flex-96454635]]

**Runway Dev — MCP plugins for coding agents (November 2, 2026).** Runway announced Dev plugins connecting coding agents (Claude Code, etc.) to the Runway Dev API via MCP, enabling generative video API calls from within agentic coding workflows [[runway-dev-plugins-for-coding-agents-35216bb0]].

> Runway announced Dev plugins for coding agents on November 2, 2026. The plugins connect your coding agent to your Runway Dev account through the Runway Dev MCP and add Runway's skills for building with the generative media API. [[runway-dev-plugins-for-coding-agents-35216bb0]]

### Updates 2026-11-01

Quiet run — no new sources ingested for generative-media-models today. Swept allowlisted outlets (Artificial Analysis, Replicate, fal.ai, Hugging Face, Meshy blog, Tripo AI blog) and found no material published since 2026-10-31 meeting the topic's charter scope. Tool-profile roster sweep skipped due to qmd MCP connection failure.

_no contradictions or gaps known yet (last reviewed: 2026-11-01)_

### Updates 2026-10-31

**AA-Video-I2V v2.1 leaderboard update: Seedance 2.5 #1 (Elo 1152), MiniMax H3 768p #4 overall / #1 open-weights.** The Artificial Analysis Image-to-Video (audio output) v2.1 leaderboard now shows **Dreamina Seedance 2.5 at #1 (Elo 1152)**, Utopai X at #2 (1144, no API), Dreamina Seedance 2.0 at #3 (1135), and **MiniMax H3 768p at #4 (Elo 1129) — first among open-weights models** [[aa-video-i2v-v2-1-leaderboard-top-ai-video-models-7458c112]]. Hyperflow H3 rounds out the top five at 1123. On the silent variant (AA-Video-I2V-Silent v2.1), Seedance 2.5 again leads at 1129, followed by MiniMax H3 Max (1125). Entity updates: [[seedance]] arena_rank updated with v2.1 data; [[minimax-h3]] arena_rank updated to reflect v2.1 I2V placement (#4, Elo 1129 vs prior #1 Elo 1140 on v1.1).

> Dreamina Seedance 2.5 currently leads AA-Video-I2V v2.1 with an Elo score of 1152.

> Among open-weights models, MiniMax H3 (768p) is first at Elo 1129, followed by LTX-2.5 Fast (917) and LTX-2.5 Pro (909).

**Two new audio-tool entities added: [[suno]] and [[minimax-music]].** Suno launched an MCP (beta) server at `https://api.suno.com/mcp` that connects to Claude, Claude Code, and other MCP clients via HTTP transport with no API key — available on all plans including Free, using plan credits [[suno-mcp-beta-fbbc54a2]]. MiniMax Music 2.6 is available on fal at **$0.15/generated audio**, with MiniMax's own direct API closed to new users since 2026-08-20 [[minimax-music-2-6-text-to-audio-api-on-fal-ff196b6a]]. Both entities are filed under `modality: music`.

> Suno MCP (beta) connects Suno to Claude, ChatGPT, Claude Code and other MCP clients.

> MiniMax's own docs state that starting August 20, 2026, the paid Music Generation and Lyrics Generation APIs are no longer available to new users, making fal the practical route for new users.

### Updates 2026-10-30

Two new in-scope video tools added this run — [[vidu-q4-preview]] (Shengshu, commercial API) and [[hy-nomas]] (Tencent Hunyuan, open-weights). Neither changes the current v1.1 leaderboard standings, so the Summary is left untouched; both extend the tool-entity roster.

**[[vidu-q4-preview]] (Shengshu Technology) — 4K, 15-image reference, commercial API launch (October 2026).** Shengshu Technology launched Vidu Q4 Preview at `platform.vidu.com` (API model ID: `viduq4-preview`) [[shengshu-technology-launches-vidu-q4-preview-a-next-generation-ai-video-model-built-for-lifelike-performances-b956992b]]. The model supports up to 15 reference images and 3 reference audio clips per generation, synchronized audio-video output, and clips up to 16 seconds at 2K or 4K resolution. Pricing is $0.045/s at 540p, scaling to $0.39/s at 4K; a 30% introductory discount on image-to-video and reference-to-video runs through November 30, 2026 [[shengshu-technology-launches-vidu-q4-preview-a-next-generation-ai-video-model-built-for-lifelike-performances-b956992b]]. An aggregator source reports Vidu Q4 Preview debuted at **#3 on AA-Video-I2V v1.0 with Elo 1,179** [[vidu-q4-preview-aa-video-i2v-debut-38fa453c]]; this is on the v1.0 board version, which is not directly comparable to the v1.1 standings (MiniMax H3 at Elo 1140) the wiki currently tracks — the v1.1 or v2.1 standing remains an open question.

> Pricing starts at $0.045 per second of video at 540p and scales with resolution, up to $0.39 per second at 4K. Image-to-video and reference-to-video generation is available at a 30% discount through November 30. [[shengshu-technology-launches-vidu-q4-preview-a-next-generation-ai-video-model-built-for-lifelike-performances-b956992b]]

> Vidu Q4 Preview supports up to 3 reference audio clips, 15 reference images, and 2K and 4K output. [[shengshu-technology-launches-vidu-q4-preview-a-next-generation-ai-video-model-built-for-lifelike-performances-b956992b]]

> Vidu Q4 Preview entered the Artificial Analysis AA-Video-I2V v1.0 leaderboard at number three with an Elo score of 1,179 on its debut, making it among the highest-ranked commercial image-to-video models on its launch day. [[vidu-q4-preview-aa-video-i2v-debut-38fa453c]]

**[[hy-nomas]] (Tencent Hunyuan) — open-source interactive world model, Apache 2.0, single-RTX-4090 footprint (October 21, 2026).** Tencent's Hunyuan team released Hy-Nomas, an interactive autoregressive video world model, to GitHub and Hugging Face under Apache 2.0 on ~October 21, 2026 [[tencent-opens-hy-nomas-an-interactive-video-world-model-running-on-one-rtx-4090-7543a82b]]. Rather than a single generation, the model supports multi-turn interaction: users describe a scene, then steer it with free-form text instructions and camera trajectories while the model continues generating. It runs on a single NVIDIA RTX 4090 [[tencent-opens-hy-nomas-an-interactive-video-world-model-running-on-one-rtx-4090-7543a82b]]. The companion Hy-Nomas-Bench covers 280 test cases across multi-turn free-form text, camera navigation, interleaved text+camera control, and spatial memory — all self-reported (see Disputes) [[tencent-opens-hy-nomas-an-interactive-video-world-model-running-on-one-rtx-4090-7543a82b]].

> Tencent's Hunyuan team released Hy-Nomas, an open-source interactive world model, on October 21, 2026. Users give a text description of a scene, then steer it with text instructions and camera moves while it keeps generating video. [[tencent-opens-hy-nomas-an-interactive-video-world-model-running-on-one-rtx-4090-7543a82b]]

> Hy-Nomas is an open-source interactive video world model under Apache 2.0, and runs on a single RTX 4090. [[tencent-opens-hy-nomas-an-interactive-video-world-model-running-on-one-rtx-4090-7543a82b]]

### Updates 2026-10-28

**Video — new leader and new entity.** [[wan-3]] (Alibaba Wan 3.0) added as a video tool entity. It now leads the Artificial Analysis text-to-video board (AA-Video-T2V v2.1, with audio) at Elo 1174, ahead of Utopai X, MiniMax H3 (768p), HeyGen Video 1 and Dreamina Seedance 2.5 [[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]], and also leads the Artificial Analysis video-editing board (AA-Video-Editing v1.1) at Elo 1198 [[aa-video-editing-v1-1-leaderboard-top-ai-video-models-1743cee9]]. On fal it is priced per second by resolution: $0.05/s (480p), $0.10/s (720p), $0.20/s (1080p); the Wan 3.0 Prime tier runs $0.068/$0.14/$0.28 per second [[wan-3-0-text-to-video-api-on-fal-581fd1f9]].

> Wan 3.0 currently leads AA-Video-T2V v2.1 with an Elo score of 1174. [[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]]

> Wan 3.0 leads AA-Video-Editing v1.1 at Elo 1198, ahead of Dreamina Seedance 2.5 at 1155 and Hyperflow H3 at 1153. [[aa-video-editing-v1-1-leaderboard-top-ai-video-models-1743cee9]]

> Wan 3.0 on fal is priced at $0.05 per second at 480p, $0.10 per second at 720p, and $0.20 per second at 1080p. [[wan-3-0-text-to-video-api-on-fal-581fd1f9]]

**Image-to-video board unchanged at the top.** [[minimax-h3]] (768p) re-confirmed #1 on AA-Video-I2V v1.1 at Elo 1140; on the text-to-video board the same model sits at #3 overall and #1 among open-weights models (Elo 1158) [[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]].

> MiniMax H3 (768p) currently leads among open weights models on AA-Video-T2V v2.1 with an Elo score of 1158. [[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]]

**Seedance 2.5 now live on fal.** [[seedance]]: Seedance 2.5 is reachable on fal under `bytedance/seedance-2.5/us`, billed by output tokens — roughly $0.2205/s (480p), $0.4730/s (720p) and $1.164/s (1080p), at $0.0214 per 1,000 tokens for 480p/720p, with no subscription or minimum [[seedance-2-5-us-image-to-video-api-on-fal-f520e761]]. This answers the prior open question on Seedance 2.5's fal availability.

> For 480p, your request will cost roughly $0.2205 per second of generated video, for 720p, you will be charged roughly $0.4730 per second of generated video, and for 1080p, roughly $1.164 per second of generated video. [[seedance-2-5-us-image-to-video-api-on-fal-f520e761]]

### Updates 2026-10-26

**Image models — new entities.** [[flux]] (FLUX 3 Image by Black Forest Labs) added: a unified generate-and-edit API endpoint (`/v1/flux-3-image`) accepting up to ten reference images with bounding-box layout control, outputting up to 4K [[flux-3-image-maximum-control-over-every-pixel-37948658]]; open-weights distilled variant FLUX 3 Image Klein (5.6B params, `flux-3-image-klein`) starts at $0.009/1K images on the BFL API [[flux-3-image-klein-open-weights-5-6b-parameters-155c7b54]].

> FLUX 3 Image generates and edits images through one endpoint, /v1/flux-3-image. Send a prompt to generate, or add up to ten reference images to edit, restyle, or combine them. Bounding boxes in the prompt place each element. Output goes up to 4K. [[flux-3-image-maximum-control-over-every-pixel-37948658]]

> BFL API: the distilled model is available as flux-3-image-klein ... Pricing starts at $0.009 per 1K image. FLUX 3 Image Klein is an open weights image generation and editing model with 5.6B parameters. [[flux-3-image-klein-open-weights-5-6b-parameters-155c7b54]]

**Image leaderboards.** GPT Image 2.5 Sunburst confirmed as #1 on Artificial Analysis AA-Image-T2I v2.1 (Elo 1196, 13,586 comparisons) and AA-Image-Editing v2.1 (Elo 1199) [[aa-image-t2i-v2-1-leaderboard-top-ai-image-models-634924f7]]; also #1 on arena.ai (Oct 7 2026 snapshot, 6M+ votes, Elo 1425) [[text-to-image-leaderboard-best-ai-image-generators-ba150d9e]].

> The text-to-image board has GPT Image 2.5 Sunburst (max) in first, at Elo 1196 across 13,586 comparisons. Sunburst also leads Artificial Analysis's image editing board, at Elo 1199. [[aa-image-t2i-v2-1-leaderboard-top-ai-image-models-634924f7]]

**Video models — new entity.** [[flux-3-max]] (FLUX 3 Max by BFL/fal) added: text-to-video, image-to-video, and keyframes-to-video on fal at $0.085/s; fal claims preliminary joint-#1 image-to-video on Artificial Analysis (Elo 1139, tied Seedance 2.5) — see Disputes [[flux-3-max-text-and-image-to-video-post-trained-by-fal-4991600a]].

> FLUX 3 Max is a post-trained video model from fal Research, built with Black Forest Labs on the FLUX 3 foundation model. fal's model listing shows $0.085/s for each variant. [[flux-3-max-text-and-image-to-video-post-trained-by-fal-4991600a]]

**Video leaderboards.** MiniMax H3 768p confirmed #1 on AA-Video-I2V v1.1 (Elo 1140, $34.12/min) [[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]; Seedance 2.0 720p #1 on the AA audio-output I2V board (Elo 1197, $9.07/min) [[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]. Seedance 2.5 announced — 30-second audio-video clips, one-take creation, up to 50 reference inputs [[introducing-seedance-2-5-78d1ddb7]].

> MiniMax H3 (768p) currently leads AA-Video-I2V v1.1 with an Elo score of 1140. Its listed API price is $34.12 /min. Seedance 2.0 is listed at $22.45 /min. [[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]

**Sora discontinued.** [[sora]] entity added with `status: shutdown`; the Sora web/app experiences closed April 26, 2026 and the API (`sora-2`, `sora-2-pro`) was discontinued September 24, 2026 with no recommended replacement; OpenAI has no plan for an open-weights release [[what-to-know-about-the-sora-discontinuation-4d8dc7c1]].

> The Sora web and app experiences were discontinued on April 26, 2026. The Sora API will be discontinued on September 24, 2026. [[what-to-know-about-the-sora-discontinuation-4d8dc7c1]]

**Ideogram pricing + licensing confirmed.** Ideogram 3.0 API on fal: $0.03/$0.06/$0.09 per image (turbo/balanced/quality) [[ideogram-text-to-image-api-on-fal-7cd91f04]]; commercial API outputs may be used freely including commercially; open-weights non-commercial only; self-serve weights license $300/10k images/mo [[licensing-ideogram-bdab80bb]].

> The fal.ai listing for Ideogram V3 API charges $0.03 with TURBO, $0.06 with BALANCED, and $0.09 with QUALITY per request. [[ideogram-text-to-image-api-on-fal-7cd91f04]]

**Kling 4.0 API preview pricing.** Kling API pricing page shows Kling 4.0 as "Coming Soon" with preview-only rates (720p 1.0 unit/s, 1080p 1.5 unit/s without video input) [[kling-api-pricing-fba30089]]; unit-to-USD conversion unknown.

> The Kling API pricing page lists Kling 4.0 as Coming Soon. Kling 4.0 API access is not yet available, and the prices are for preview purposes only. [[kling-api-pricing-fba30089]]

### Updates 2026-10-25

**Image models.** Three new image-generation entities added: [[gpt-image]] (OpenAI GPT Image 2.5 Flare + Sunburst — API, speed/quality variants, supports editing/inpainting/outpainting [[gpt-image-2-5-flare-and-sunburst-released-by-openai-cf34266e]]), [[nano-banana]] (Google DeepMind Nano Banana 2 Lite at $0.034/1K images via `gemini-3.1-flash-image` [[nano-banana-2-lite-google-deepmind-image-generation-at-0-034-1k-images-3eac9764]]), and [[ideogram]] (Ideogram 3.0 with commercial API on fal.ai and a research-only open-weights variant on Hugging Face [[ideogram-3-0-launches-with-open-weights-model-and-commercial-license-1f773818]]).

> GPT Image 2.5 Flare and Sunburst are the latest image generation models from OpenAI, available in the API as gpt-image-2.5-flare and gpt-image-2.5-sunburst. Flare prioritizes speed and cost, Sunburst prioritizes quality. Both support editing, inpainting, and outpainting via the image edit endpoint.

> Nano Banana 2 Lite is available via the Gemini API as gemini-3.1-flash-image. Priced at $0.034 per 1K images generated. Supports image generation and editing. Built on the Gemini 3.1 Flash architecture.

**Video models.** Two new video-generation entities added: [[kling]] (Kling 4.0 + 4.0 Flash by Kuaishou, cinematic quality vs. speed/cost variants, API and Replicate, released Oct 15 2026 [[kling-4-0-and-4-0-flash-video-generation-models-launch-b0391b87]]) and [[seedance]] (ByteDance Seedance, #1 Artificial Analysis Image-to-Video with audio output benchmark as of Oct 25 2026 [[seedance-wins-artificial-analysis-image-to-video-with-audio-output-benchmark-1-a7869d54]]).

> Seedance by ByteDance ranks first on the Artificial Analysis Image-to-Video (audio output) benchmark as of October 25, 2026. Available via the Seedance API. Supports image-to-video and text-to-video with synchronized audio output.

**Music.** [[eleven-music]] entity added: ElevenLabs Music API at $0.15/min with a 5-min cap per generation; commercial use allowed on all paid plans **except** Studio Games on self-serve — a practical restriction for indie game devs [[elevenlabs-music-0-15-per-minute-5-minute-cap-studio-games-plan-restriction-9f14fd6d]].

> ElevenLabs Music generates music from text prompts via the music generation API. Pricing is $0.15 per minute of generated music, with a 5-minute cap per generation. Commercial use is allowed on all paid plans except Studio Games on self-serve plans.

**Sprites.** Three new sprite/game-asset entities added: [[pixellab]] (Claude-compatible MCP server, from $0.001/image [[pixellab-sprite-generation-mcp-server-for-claude-code-1195a2d7]]), [[retro-diffusion]] (pixel art, from $0.03/image, MCP server [[retro-diffusion-pixel-art-generation-from-0-03-per-image-mcp-server-available-0746b611]]), and [[scenario]] (game-ready sprites via MCP server compatible with Claude Code, Codex, and Cursor [[scenario-mcp-server-for-claude-code-codex-and-cursor-9bf7b8e5]]). Enables seeding of the `image-tools` and sprite-tools roster.

### Updates 2026-10-24

Topic created. Seeded three speech/video tool entities ([[minimax-h3]], [[inworld-realtime-tts-2]], [[elevenlabs]]) from sources previously ingested under `ai-in-game-dev`, and the `audio-tools` comparison page. No new sources ingested.

## Disputes

- [[tencent-opens-hy-nomas-an-interactive-video-world-model-running-on-one-rtx-4090-7543a82b]] (Tencent) reports Hy-Nomas performance on Hy-Nomas-Bench (280 test cases, four axes); no independent third-party evaluation of the benchmarks published at launch. Status: unresolved — all benchmark claims are self-reported by the model authors.
- [[flux-3-max-text-and-image-to-video-post-trained-by-fal-4991600a]] (fal) claims FLUX 3 Max is joint #1 image-to-video on Artificial Analysis's preliminary arena (Elo 1139, tied Seedance 2.5); [[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]] shows the live AA I2V boards led by MiniMax H3 768p (Elo 1140) and Seedance 2.0 720p (audio board, Elo 1197) with FLUX 3 Max not listed as sole #1. Status: unresolved
- Topic Summary claims MiniMax H3 "ranks #1 in Video Editing, #2 in Text-to-Video and #3 in Image-to-Video on the Artificial Analysis boards" citing [[minimaxai-minimax-h3-hugging-face-1f0e60fd]]; current version of that source (fetched 2026-10-24) contains no mention of "Artificial Analysis" or any arena rankings. Status: partially-resolved — [[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]] (2026-10-26) confirms I2V #1; [[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]] (2026-10-28) places H3 #3 overall / #1 open-weights on T2V (not #2 overall); Video Editing #1 now confirmed by [[aa-video-editing-v1-1-leaderboard-top-ai-video-models-1743cee9]] (Wan 3.0 is #1, H3/Hyperflow H3 not explicitly ranked but the prior claim of H3 #1 is superseded). (confidence: high; sweep: 2026-10-25)
- [[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]] shows MiniMax H3 (768p) at #3 overall on the text-to-video board (behind Wan 3.0 and Utopai X); the topic Summary's carried-forward claim that H3 is "#2 in Text-to-Video" is therefore superseded on the live board. Status: resolved-toward-aa-video-t2v — H3 is #3 overall / #1 open-weights on AA-Video-T2V v2.1 as of 2026-10-28.
- Topic Summary (as of 2026-10-28, citing v1.1 board data) claims MiniMax H3 (768p) is #1 image-to-video (AA-Video-I2V v1.1, Elo 1140); [[aa-video-i2v-v2-1-leaderboard-top-ai-video-models-7458c112]] (2026-10-31) shows that on the updated v2.1 board, Dreamina Seedance 2.5 is #1 (Elo 1152) and MiniMax H3 768p is #4 overall (Elo 1129, #1 among open-weights). Status: unresolved — the Summary has not been regenerated to reflect the current v2.1 board version and standings. (confidence: high; sweep: 2026-11-01)

> From topic Summary: "and **[[minimax-h3]] (768p)** as #1 image-to-video (AA-Video-I2V v1.1, Elo 1140, $34.12/min AA-measured)"

> From 2026-10-31 log entry: "The Artificial Analysis Image-to-Video (audio output) v2.1 leaderboard now shows **Dreamina Seedance 2.5 at #1 (Elo 1152)**, Utopai X at #2 (1144, no API), Dreamina Seedance 2.0 at #3 (1135), and **MiniMax H3 768p at #4 (Elo 1129) — first among open-weights models**"

> From topic Summary: "On the Artificial Analysis leaderboards H3 ranks #1 in Video Editing, #2 in Text-to-Video, and #3 in Image-to-Video."

> From source [[minimaxai-minimax-h3-hugging-face-1f0e60fd]]: No mention of Artificial Analysis or arena rankings in any excerpt.

- Topic Summary (line 31) claims "Image, music, SFX, sprites. No sources yet"; Recent updates 2026-10-25 and 2026-10-26 show image/sprite/music entities added ([[gpt-image]], [[nano-banana]], [[ideogram]], [[flux]], [[pixellab]], [[retro-diffusion]], [[scenario]], [[eleven-music]]). Status: unresolved (confidence: high; sweep: 2026-11-01)

> From topic Summary (line 31): "**Image, music, SFX, sprites.** No sources yet. The researcher's first runs should seed the `image-tools` and `video-tools` comparison pages once at least two tool entities per modality exist..."

> From Recent updates 2026-10-25: "**Image models.** Three new image-generation entities added: [[gpt-image]] (OpenAI GPT Image 2.5 Flare + Sunburst — API, speed/quality variants, supports editing/inpainting/outpainting [[gpt-image-2-5-flare-and-sunburst-released-by-openai-cf34266e]]), [[nano-banana]] (Google DeepMind Nano Banana 2 Lite at $0.034/1K images via `gemini-3.1-flash-image` [[nano-banana-2-lite-google-deepmind-image-generation-at-0-034-1k-images-3eac9764]]), and [[ideogram]] (Ideogram 3.0 with commercial API on fal.ai and a research-only open-weights variant on Hugging Face [[ideogram-3-0-launches-with-open-weights-model-and-commercial-license-1f773818]])."

> From Recent updates 2026-10-25: "**Sprites.** Three new sprite/game-asset entities added: [[pixellab]] (Claude-compatible MCP server, from $0.001/image [[pixellab-sprite-generation-mcp-server-for-claude-code-1195a2d7]]), [[retro-diffusion]] (pixel art, from $0.03/image, MCP server [[retro-diffusion-pixel-art-generation-from-0-03-per-image-mcp-server-available-0746b611]]), and [[scenario]] (game-ready sprites via MCP server compatible with Claude Code, Codex, and Cursor [[scenario-mcp-server-for-claude-code-codex-and-cursor-9bf7b8e5]])."

## Open questions

- [ ] Nano Banana 2.1 exact Gemini API model id (`gemini-3.6-flash-image`?), per-image pricing, and commercial-use terms for game assets — not stated in the DeepMind model card [[nano-banana-2-1-model-card-google-deepmind-2783cdec]].
- [ ] Confirm Nano Banana 2.1 Artificial Analysis AA-Image-T2I / AA-Image-Editing Elo against a dated live snapshot — captures currently conflict (~1176 T2I, ~1152 editing) [[nano-banana-2-1-model-card-google-deepmind-2783cdec]].
- [ ] Reconcile Eleven v4 / v4 Turbo per-minute API pricing (~$0.08/min v4, ~$0.04/min v4 Turbo) with the credit model ($6/mo per 30k credits, 1 credit/char) — ElevenLabs pages conflict [[eleven-v4-our-most-expressive-text-to-speech-ai-model-yet-028b20a4]].
- [ ] Eleven v4 / v4 Turbo commercial-use terms by plan tier for shipping NPC voice in a commercial game — not stated in the launch blog [[eleven-v4-our-most-expressive-text-to-speech-ai-model-yet-028b20a4]].
- [ ] Suno credit-to-song cost rate on paid plans (credits per generated song), and whether MiniMax Music / Udio / Lyria offer comparably documented commercial-use terms for game use [[can-i-distribute-my-songs-to-spotify-etc-25684551]].
- [ ] Vidu Q4 Preview v1.1/v2.1 arena placement — debuted #3 on AA-Video-I2V v1.0 (Elo 1,179) [[vidu-q4-preview-aa-video-i2v-debut-38fa453c]], but v1.0 Elos are not comparable to the v1.1 standings the wiki tracks; confirm v1.1 or v2.1 placement once available. Commercial-use terms for game production not stated in ingested sources.
- [ ] Hy-Nomas public API or fal/Replicate endpoint availability; hardware floor confirmed as single RTX 4090 but not stated for 8B size.
- [ ] What is the current #1 on the arena.ai text-to-image board, and does Artificial Analysis' image arena agree?
- [ ] Which text-to-music models (Suno, Udio, Lyria, Stable Audio) permit shipping output in a commercial game on a non-enterprise plan, as of this month?
- [ ] What are the per-second prices for MiniMax H3 on the MiniMax API vs fal.ai, and does the open-weight license permit commercial game use?
- [ ] Which sprite / pixel-art generators (PixelLab, Retro Diffusion, Scenario) expose a public API, and at what price? (Partially answered 2026-10-25: all three have APIs; PixelLab from $0.001/img, Retro Diffusion from $0.03/img, Scenario pricing unknown.)
- [ ] Commercial-use terms for new image models (GPT Image 2.5, Nano Banana, Ideogram 3.0) — none stated in ingested sources.
- [ ] Commercial-use terms for ElevenLabs Music on the Studio Games enterprise plan (only self-serve restriction confirmed).
- [ ] Video pricing for Kling 4.0 / Seedance — Kling 4.0 has preview rates but "unit" is undefined (USD/unit unknown); Seedance 2.0 pricing is AA-measured ($9.07–$22.45/min) rather than vendor-listed.
- [ ] Full (non-Klein) FLUX 3 Image per-call price on the BFL API; Klein open-weights license name (SPDX or vendor name) and hardware floor.
- [ ] FLUX 3 Max commercial-use terms for game video; primary dated release announcement (reported 2026-10-19, unconfirmed).
- [ ] Does any third-party aggregator (fal, Replicate) still serve a Sora-2 endpoint after the 2026-09-24 OpenAI API shutdown?
- [x] Seedance 2.5 API launch date and fal/Replicate endpoint availability — **resolved 2026-10-28**: `bytedance/seedance-2.5/us` live on fal [[seedance-2-5-us-image-to-video-api-on-fal-f520e761]].
- [ ] What is Seedance 2.5's own placement on the AA-Video-I2V / T2V boards (it appears in the T2V top-5 but with no clean standalone Elo in the ingested snapshot)?
- [ ] Does FLUX 3 Max's live AA image-to-video placement match its vendor-reported joint-#1 claim? The AA I2V board snapshot lists it near Elo 1138, below MiniMax H3 (1140) — needs a clean dedicated citation.
- [ ] Is Wan 3.0 available as open weights, and under what license and hardware floor? One aggregator noted no official Alibaba model card; fal lists API-only pricing.
- [ ] Which image models (FLUX 3 Image, GPT Image 2.5, Ideogram 3.0) permit game-shipping commercial use under their standard API/self-serve terms?
- [ ] Has Meshy's pricing changed after the $400M Series B at $1.5B valuation (2026-10-10)? The Meshy pricing page was swept on 2026-11-01 but no changes were found; re-check on the next run.
- [ ] Does Tripo AI's P2.0 native-quad-mesh generation reduce the downstream retopology burden to zero for production pipelines, or does it still require manual cleanup for game-engine compliance?
- [ ] Utopai X holds #2 on AA-Video-T2V v2.1 (Elo 1161) but has no API — does Utopai plan a public API/fal/Replicate release, and does access status change before the next roster sweep?
- [ ] Does DesignArena's T2V methodology match Artificial Analysis' (arena-style human evaluation vs. automated?) — [[pika-h3-flex]] is #7 on DesignArena and #1 open-weights, but the boards are not directly comparable; confirm whether Pika H3 Flex appears on the AA-Video-T2V board [[pika-on-x-meet-pika-h3-flex-96454635]].
- [ ] Pika API subscription pricing for hosted 4K upscaling and audio stem separation — not stated in any ingested source [[introducing-pika-h3-flex-0a7ab440]].
- [ ] Commercial-use terms for game developers shipping video generated via the Pika API (hosted) or the Pika H3 Flex open-weights LoRA adapters — not stated in any ingested source [[introducing-pika-h3-flex-0a7ab440]].
- [ ] Does Runway Dev MCP expose video generation endpoints on par with the full Runway API, or is it limited to metadata and job management? [[runway-dev-plugins-for-coding-agents-35216bb0]]
- [ ] What are GPT Image 2.6's commercial-use / licensing terms for shipping generated assets in a commercial game? Not stated in the ingested OpenAI announcement or model docs.
- [ ] GPT Image 2.6 arena placement — not yet on the Artificial Analysis AA-Image-T2I / AA-Image-Editing boards as of 2026-11-05 (GPT Image 2.5 Sunburst still #1); confirm 2.6's Elo once ranked.
- [x] Is Nano Banana 2.1 (Gemini 3.6 Flash, DeepMind model card dated 2026-10-06, AA image-editing Elo ~1151) a distinct model from the tracked Nano Banana 2 Lite (gemini-3.1-flash-image)? Decide whether [[nano-banana]] should be updated or split into a 2.1 entity. **resolved 2026-11-07**: split into [[nano-banana-2-1]] entity; [[nano-banana]] updated to note the split.
- [ ] ByteDance reportedly retires Seedance 1.5 Pro on 2026-11-11 (surfaced in an aggregator search, not confirmed by a primary ByteDance / fal / Replicate deprecation notice) — confirm the date, scope, and migration path.
- [ ] AA-Video-I2V v2.1 Elo drift: a 2026-11-05 board read showed Seedance 2.5 at ~1159 (vs recorded 1152 on 2026-10-31) and Wan 3.0 at #9 (~1112); confirm against a dated AA snapshot before updating [[seedance]] / [[wan-3]] arena_rank.
- [ ] FLUX 3 Max fal launch promo — 75% off until 2026-11-07 (720p $0.0425/s discounted; list $0.17/s at 720p, $0.29/s at 1080p) — conflicts with the recorded $0.085/s and with a fal 'until Dec 31' claim; reconcile [[flux-3-max]] pricing on the next sweep (a fresh dated source is needed since the existing fal source page is immutable).

## See also

- [[audio-tools]]
- [[ai-in-game-dev]]
- [[frontier-models]]
- [[game-music]]
- [[wan-3]]
