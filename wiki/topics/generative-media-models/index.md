---
title: Generative media models
kind: topic
sources: ["[[minimaxai-minimax-h3-hugging-face-1f0e60fd]]", "[[minimax-releases-minimax-h3-an-omni-modal-video-model-that-generates-15-second-2k-clips-with-native-stereo-audio-53db5121]]", "[[realtime-tts-2-a-new-frontier-voice-model-that-feels-as-real-as-you-68a9e733]]", "[[ai-voice-for-games-elevenlabs-31e6ac62]]", "[[gpt-image-2-5-flare-and-sunburst-released-by-openai-cf34266e]]", "[[nano-banana-2-lite-google-deepmind-image-generation-at-0-034-1k-images-3eac9764]]", "[[ideogram-3-0-launches-with-open-weights-model-and-commercial-license-1f773818]]", "[[kling-4-0-and-4-0-flash-video-generation-models-launch-b0391b87]]", "[[seedance-wins-artificial-analysis-image-to-video-with-audio-output-benchmark-1-a7869d54]]", "[[elevenlabs-music-0-15-per-minute-5-minute-cap-studio-games-plan-restriction-9f14fd6d]]", "[[pixellab-sprite-generation-mcp-server-for-claude-code-1195a2d7]]", "[[retro-diffusion-pixel-art-generation-from-0-03-per-image-mcp-server-available-0746b611]]", "[[scenario-mcp-server-for-claude-code-codex-and-cursor-9bf7b8e5]]", "[[flux-3-image-maximum-control-over-every-pixel-37948658]]", "[[flux-3-image-klein-open-weights-5-6b-parameters-155c7b54]]", "[[flux-3-max-text-and-image-to-video-post-trained-by-fal-4991600a]]", "[[introducing-seedance-2-5-78d1ddb7]]", "[[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]", "[[aa-image-t2i-v2-1-leaderboard-top-ai-image-models-634924f7]]", "[[text-to-image-leaderboard-best-ai-image-generators-ba150d9e]]", "[[what-to-know-about-the-sora-discontinuation-4d8dc7c1]]", "[[licensing-ideogram-bdab80bb]]", "[[ideogram-text-to-image-api-on-fal-7cd91f04]]", "[[kling-api-pricing-fba30089]]"]
last_updated: 2026-10-26
last_verified: 2026-10-26
freshness_window_days: 30
---

# Generative media models

See [purpose](purpose.md) for the topic charter (in-scope / out-of-scope) and
`CLAUDE.md` "Cross-cutting relevance criteria" for the meta-bar.

## Summary

This topic tracks the current lineup of models that generate images, video, music, sound effects and speech — how each is reached (vendor API, fal.ai, Replicate, open weights), what it costs, under what commercial-use terms its output may ship in a game, and where it sits on arena boards with methodology. Every model is an entity page with a machine-readable tool profile (`profile: tool`), and the per-modality comparison pages — [[audio-tools]], [[image-tools]] and [[video-tools]] — aggregate those profiles. The 3D and motion side of the same tool roster is owned by [[ai-in-game-dev]] (see [[3d-tools]] and [[rig-and-motion-tools]]). The dominant caveat across modalities: arena leadership is well-sourced, but game-shipping commercial-use terms are stated for only a few models (see Open questions).

**Video — current leaders.** On the live Artificial Analysis image-to-video boards, [[minimax-h3]] (768p, no audio) leads AA-Video-I2V v1.1 at Elo 1140 (AA-measured $34.12/min), and [[seedance]] 2.0 (720p) leads the separate audio-output I2V board at Elo 1197 (AA-measured $9.07/min) [[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]. MiniMax H3 is the open-weights flagship: an omni-modal model generating 15-second 2K clips with native stereo audio from unified text / image / video / audio context, released as two task-specific checkpoints under the MiniMax H3 Community License (API is the only path today; open weights are regionally restricted) [[minimax-releases-minimax-h3-an-omni-modal-video-model-that-generates-15-second-2k-clips-with-native-stereo-audio-53db5121]] [[minimaxai-minimax-h3-hugging-face-1f0e60fd]].

> MiniMax H3 (768p) currently leads AA-Video-I2V v1.1 with an Elo score of 1140. Its listed API price is $34.12 /min. Seedance 2.0 is listed at $22.45 /min. [[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]

> MiniMax H3 generates 15-second 2K video with native stereo audio from unified text, image, video, and audio context ... Open weights are promised 'in the coming days,' not shipped; the API is the only path today. [[minimax-releases-minimax-h3-an-omni-modal-video-model-that-generates-15-second-2k-clips-with-native-stereo-audio-53db5121]]

> MiniMax H3 is released under the MiniMax H3 Community License Agreement. ... Application form (only for USA/EU/UK/South Korea). [[minimaxai-minimax-h3-hugging-face-1f0e60fd]]

**Video — the rest of the field.** [[seedance]] 2.5 was announced (30-second audio-video clips in one pass, one-take creation, up to 50 reference inputs), though its API launch date and fal/Replicate availability are open [[introducing-seedance-2-5-78d1ddb7]]; Seedance by ByteDance previously took #1 on the AA image-to-video (audio output) benchmark [[seedance-wins-artificial-analysis-image-to-video-with-audio-output-benchmark-1-a7869d54]]. [[flux-3-max]] (BFL post-trained by fal: text-, image-, and keyframes-to-video) is reachable on fal at $0.085/s; fal claims a preliminary joint-#1 image-to-video arena placement (Elo 1139, tied Seedance 2.5) that the live AA board does not corroborate — see Disputes [[flux-3-max-text-and-image-to-video-post-trained-by-fal-4991600a]]. [[kling]] 4.0 and 4.0 Flash (Kuaishou, released Oct 15 2026, via Kling API and Replicate) target cinematic quality vs. speed/cost, but 4.0 API access is "Coming Soon" with preview-only unit rates and no published unit-to-USD conversion [[kling-4-0-and-4-0-flash-video-generation-models-launch-b0391b87]] [[kling-api-pricing-fba30089]]. **First shutdown recorded in the topic:** OpenAI's [[sora]] is discontinued — the web/app experiences closed April 26 2026 and the `sora-2` / `sora-2-pro` API was discontinued September 24 2026, with no recommended replacement and no planned open-weights release [[what-to-know-about-the-sora-discontinuation-4d8dc7c1]].

> Seedance 2.5 is able to generate high-quality, 30-second audio-video clips in a single pass, with multi-round extensions. [[introducing-seedance-2-5-78d1ddb7]]

> Seedance by ByteDance ranks first on the Artificial Analysis Image-to-Video (audio output) benchmark as of October 25, 2026. [[seedance-wins-artificial-analysis-image-to-video-with-audio-output-benchmark-1-a7869d54]]

> FLUX 3 Max is a post-trained video model from fal Research, built with Black Forest Labs on the FLUX 3 foundation model. fal's model listing shows $0.085/s for each variant. [[flux-3-max-text-and-image-to-video-post-trained-by-fal-4991600a]]

> Kling 4.0 and Kling 4.0 Flash are the latest video generation models from Kuaishou. ... Both are available via the Kling API and replicate.com. Last release: October 15, 2026. [[kling-4-0-and-4-0-flash-video-generation-models-launch-b0391b87]]

> The Kling API pricing page lists Kling 4.0 as Coming Soon. Kling 4.0 API access is not yet available, and the prices are for preview purposes only. [[kling-api-pricing-fba30089]]

> The Sora web and app experiences were discontinued on April 26, 2026. The Sora API will be discontinued on September 24, 2026. [[what-to-know-about-the-sora-discontinuation-4d8dc7c1]]

**Image — current leader.** [[gpt-image]] 2.5 Sunburst (OpenAI, quality-first variant; Flare is the speed/cost variant) is the across-the-board leader: #1 on Artificial Analysis AA-Image-T2I v2.1 (Elo 1196, 13,586 comparisons) and #1 on AA-Image-Editing v2.1 (Elo 1199) [[aa-image-t2i-v2-1-leaderboard-top-ai-image-models-634924f7]], and #1 on the arena.ai text-to-image board (Oct 7 2026 snapshot, 6M+ votes, Elo 1425, with Flare second) [[text-to-image-leaderboard-best-ai-image-generators-ba150d9e]]. GPT Image 2.5 is API-only (supports editing / inpainting / outpainting) and its pricing is not yet recorded [[gpt-image-2-5-flare-and-sunburst-released-by-openai-cf34266e]].

> The text-to-image board has GPT Image 2.5 Sunburst (max) in first, at Elo 1196 across 13,586 comparisons. Sunburst also leads Artificial Analysis's image editing board, at Elo 1199. [[aa-image-t2i-v2-1-leaderboard-top-ai-image-models-634924f7]]

> The overall board, dated Oct 7, 2026 and built on 6M+ votes, puts GPT-Image-2.5 Sunburst first at 1425 (+/-7). GPT-Image-2.5 Flare is second (1398). [[text-to-image-leaderboard-best-ai-image-generators-ba150d9e]]

> GPT Image 2.5 Flare and Sunburst are the latest image generation models from OpenAI ... Flare prioritizes speed and cost, Sunburst prioritizes quality. Both support editing, inpainting, and outpainting via the image edit endpoint. [[gpt-image-2-5-flare-and-sunburst-released-by-openai-cf34266e]]

**Image — best-in-segment and value.** [[flux]] (FLUX 3 Image by Black Forest Labs) is the open-weights-adjacent flagship: a unified generate-and-edit endpoint accepting up to ten reference images with bounding-box layout control and output up to 4K, plus a distilled open-weights variant FLUX 3 Image Klein (5.6B params) from $0.009/1K images on the BFL API (full FLUX 3 Image per-call price and Klein's license name are open) [[flux-3-image-maximum-control-over-every-pixel-37948658]] [[flux-3-image-klein-open-weights-5-6b-parameters-155c7b54]]. On price, [[nano-banana]] 2 Lite (Google DeepMind, `gemini-3.1-flash-image`) is the cheapest listed at $0.034/1K images [[nano-banana-2-lite-google-deepmind-image-generation-at-0-034-1k-images-3eac9764]]. [[ideogram]] 3.0 is the clearest commercial-terms story: fal API at $0.03 / $0.06 / $0.09 per image (turbo / balanced / quality), with API image outputs free for any use including commercial, while the Hugging Face open-weights variant is research-only under the Ideogram Non-Commercial Model Agreement (self-serve commercial weights license $300/10k images per month) [[ideogram-text-to-image-api-on-fal-7cd91f04]] [[licensing-ideogram-bdab80bb]].

> FLUX 3 Image generates and edits images through one endpoint, /v1/flux-3-image. ... add up to ten reference images ... Bounding boxes in the prompt place each element. Output goes up to 4K. [[flux-3-image-maximum-control-over-every-pixel-37948658]]

> FLUX 3 Image Klein is an open weights image generation and editing model with 5.6B parameters. ... Pricing starts at $0.009 per 1K image. [[flux-3-image-klein-open-weights-5-6b-parameters-155c7b54]]

> Nano Banana 2 Lite is available via the Gemini API as gemini-3.1-flash-image. Priced at $0.034 per 1K images generated. [[nano-banana-2-lite-google-deepmind-image-generation-at-0-034-1k-images-3eac9764]]

> The fal.ai listing for Ideogram V3 API charges $0.03 with TURBO, $0.06 with BALANCED, and $0.09 with QUALITY per request. [[ideogram-text-to-image-api-on-fal-7cd91f04]]

> Ideogram's pricing FAQ says the company does not claim ownership of your generated images, and you're free to use them for any purpose, including commercial use. ... Open weights are a quantized version ... under the Ideogram Non-Commercial Model Agreement. Under that license, commercial use isn't permitted. [[licensing-ideogram-bdab80bb]]

**Speech.** [[inworld-realtime-tts-2]] targets in-game conversational use with sub-130 ms first-chunk latency, inline plain-language voice direction and one voice identity across 100+ languages, and was #1 realtime TTS on the Artificial Analysis Speech Arena at launch [[realtime-tts-2-a-new-frontier-voice-model-that-feels-as-real-as-you-68a9e733]]; [[elevenlabs]] (Eleven v3) targets multilingual NPC voice with an Unreal Engine integration [[ai-voice-for-games-elevenlabs-31e6ac62]]. Both are speech entities in [[audio-tools]]; pricing and commercial-use terms for both remain open questions.

> #1 realtime TTS by real users on the Artificial Analysis Speech Arena with sub-130ms first-chunk latency [[realtime-tts-2-a-new-frontier-voice-model-that-feels-as-real-as-you-68a9e733]]

> ElevenLabs has released Eleven v3, a text-to-speech model ... designed for easy integration with Unreal Engine. [[ai-voice-for-games-elevenlabs-31e6ac62]]

**Music.** [[eleven-music]] (ElevenLabs Music API) generates music from text prompts at $0.15/min with a 5-minute cap per generation; commercial use is allowed on all paid plans **except** Studio Games on self-serve — a practical restriction for indie game devs to watch [[elevenlabs-music-0-15-per-minute-5-minute-cap-studio-games-plan-restriction-9f14fd6d]]. No competing text-to-music model (Suno, Udio, Lyria, Stable Audio) has a source in the wiki yet (see Open questions).

> ElevenLabs Music generates music from text prompts ... Pricing is $0.15 per minute of generated music, with a 5-minute cap per generation. Commercial use is allowed on all paid plans except Studio Games on self-serve plans. [[elevenlabs-music-0-15-per-minute-5-minute-cap-studio-games-plan-restriction-9f14fd6d]]

**Sprites / game assets.** Three MCP-server sprite generators are tracked, all API-accessible: [[pixellab]] (text-to-sprite, from $0.001/image on pay-as-you-go) [[pixellab-sprite-generation-mcp-server-for-claude-code-1195a2d7]], [[retro-diffusion]] (pixel art, from $0.03/image) [[retro-diffusion-pixel-art-generation-from-0-03-per-image-mcp-server-available-0746b611]], and [[scenario]] (game-ready sprites/assets, MCP server for Claude Code / Codex / Cursor, pricing not stated) [[scenario-mcp-server-for-claude-code-codex-and-cursor-9bf7b8e5]]. All three are directly usable from an agentic coding workflow via their MCP servers.

> PixelLab offers a Claude-compatible MCP server for sprite generation from text prompts. ... Pricing starts from $0.001 per image on pay-as-you-go plans. [[pixellab-sprite-generation-mcp-server-for-claude-code-1195a2d7]]

> Retro Diffusion generates pixel art sprites from text prompts. Pricing starts from $0.03 per image. An MCP server compatible with Claude Code is available. [[retro-diffusion-pixel-art-generation-from-0-03-per-image-mcp-server-available-0746b611]]

> Scenario provides an MCP server for game asset generation compatible with Claude Code, Codex, and Cursor. Scenario generates game-ready sprites and assets. [[scenario-mcp-server-for-claude-code-codex-and-cursor-9bf7b8e5]]

**Recommended best practices (current).** For shippable-in-a-game licensing clarity, [[ideogram]] 3.0's API outputs (free for commercial use) are the safest documented image option today [[licensing-ideogram-bdab80bb]]; [[eleven-music]] is usable commercially on paid plans outside self-serve Studio Games [[elevenlabs-music-0-15-per-minute-5-minute-cap-studio-games-plan-restriction-9f14fd6d]]. For raw arena quality, [[gpt-image]] 2.5 Sunburst leads image [[aa-image-t2i-v2-1-leaderboard-top-ai-image-models-634924f7]], and [[minimax-h3]] / [[seedance]] lead image-to-video [[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]. Treat vendor-reported arena placements (e.g. [[flux-3-max]]'s joint-#1 claim) as provisional until the live Artificial Analysis board corroborates them.

## Recent updates

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

- [[flux-3-max-text-and-image-to-video-post-trained-by-fal-4991600a]] (fal) claims FLUX 3 Max is joint #1 image-to-video on Artificial Analysis's preliminary arena (Elo 1139, tied Seedance 2.5); [[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]] shows the live AA I2V boards led by MiniMax H3 768p (Elo 1140) and Seedance 2.0 720p (audio board, Elo 1197) with FLUX 3 Max not listed as sole #1. Status: unresolved
- Topic Summary claims MiniMax H3 "ranks #1 in Video Editing, #2 in Text-to-Video and #3 in Image-to-Video on the Artificial Analysis boards" citing [[minimaxai-minimax-h3-hugging-face-1f0e60fd]]; current version of that source (fetched 2026-10-24) contains no mention of "Artificial Analysis" or any arena rankings. Status: partially-resolved — [[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]] (2026-10-26) confirms I2V #1; Video Editing #1 and T2V #2 remain uncited. (confidence: high; sweep: 2026-10-25)

> From topic Summary: "On the Artificial Analysis leaderboards H3 ranks #1 in Video Editing, #2 in Text-to-Video, and #3 in Image-to-Video."

> From source [[minimaxai-minimax-h3-hugging-face-1f0e60fd]]: No mention of Artificial Analysis or arena rankings in any excerpt.

## Open questions

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
- [ ] Seedance 2.5 API launch date and fal/Replicate endpoint availability.
- [ ] Which image models (FLUX 3 Image, GPT Image 2.5, Ideogram 3.0) permit game-shipping commercial use under their standard API/self-serve terms?

## See also

- [[audio-tools]]
- [[ai-in-game-dev]]
- [[frontier-models]]
- [[game-music]]
