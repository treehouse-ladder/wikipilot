---
title: Generative media models
kind: topic
sources: ["[[minimaxai-minimax-h3-hugging-face-1f0e60fd]]", "[[minimax-releases-minimax-h3-an-omni-modal-video-model-that-generates-15-second-2k-clips-with-native-stereo-audio-53db5121]]", "[[realtime-tts-2-a-new-frontier-voice-model-that-feels-as-real-as-you-68a9e733]]", "[[ai-voice-for-games-elevenlabs-31e6ac62]]", "[[gpt-image-2-5-flare-and-sunburst-released-by-openai-cf34266e]]", "[[nano-banana-2-lite-google-deepmind-image-generation-at-0-034-1k-images-3eac9764]]", "[[ideogram-3-0-launches-with-open-weights-model-and-commercial-license-1f773818]]", "[[kling-4-0-and-4-0-flash-video-generation-models-launch-b0391b87]]", "[[seedance-wins-artificial-analysis-image-to-video-with-audio-output-benchmark-1-a7869d54]]", "[[elevenlabs-music-0-15-per-minute-5-minute-cap-studio-games-plan-restriction-9f14fd6d]]", "[[pixellab-sprite-generation-mcp-server-for-claude-code-1195a2d7]]", "[[retro-diffusion-pixel-art-generation-from-0-03-per-image-mcp-server-available-0746b611]]", "[[scenario-mcp-server-for-claude-code-codex-and-cursor-9bf7b8e5]]", "[[flux-3-image-maximum-control-over-every-pixel-37948658]]", "[[flux-3-image-klein-open-weights-5-6b-parameters-155c7b54]]", "[[flux-3-max-text-and-image-to-video-post-trained-by-fal-4991600a]]", "[[introducing-seedance-2-5-78d1ddb7]]", "[[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]", "[[aa-image-t2i-v2-1-leaderboard-top-ai-image-models-634924f7]]", "[[text-to-image-leaderboard-best-ai-image-generators-ba150d9e]]", "[[what-to-know-about-the-sora-discontinuation-4d8dc7c1]]", "[[licensing-ideogram-bdab80bb]]", "[[ideogram-text-to-image-api-on-fal-7cd91f04]]", "[[kling-api-pricing-fba30089]]", "[[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]]", "[[wan-3-0-text-to-video-api-on-fal-581fd1f9]]", "[[aa-video-editing-v1-1-leaderboard-top-ai-video-models-1743cee9]]", "[[seedance-2-5-us-image-to-video-api-on-fal-f520e761]]", "[[shengshu-technology-launches-vidu-q4-preview-a-next-generation-ai-video-model-built-for-lifelike-performances-b956992b]]", "[[tencent-opens-hy-nomas-an-interactive-video-world-model-running-on-one-rtx-4090-7543a82b]]", "[[vidu-q4-preview-aa-video-i2v-debut-38fa453c]]"]
last_updated: 2026-10-30
last_verified: 2026-10-30
freshness_window_days: 30
---

# Generative media models

See [purpose](purpose.md) for the topic charter (in-scope / out-of-scope) and
`CLAUDE.md` "Cross-cutting relevance criteria" for the meta-bar.

## Summary

This topic tracks the current lineup of models that generate images, video, music, sound effects and speech — how each is reached (vendor API, fal.ai, Replicate, open weights), what it costs, under what commercial-use terms its output may ship in a game, and where it sits on arena boards with methodology. Every model is an entity page with a machine-readable tool profile (`profile: tool`) — currently [[minimax-h3]], [[inworld-realtime-tts-2]] and [[elevenlabs]] — and the per-modality comparison pages ([[audio-tools]] today) aggregate those profiles. The topic was created on 2026-10-24 and seeded only from sources already in the wiki, so coverage of image, music and SFX models is empty until the first daily run.

**Video.** As of 2026-10-28 the video-board leaders are: **[[wan-3]] (Wan 3.0, Alibaba)** at #1 on both the Artificial Analysis text-to-video board (AA-Video-T2V v2.1, with audio, Elo 1174) [[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]] and the video-editing board (AA-Video-Editing v1.1, Elo 1198) [[aa-video-editing-v1-1-leaderboard-top-ai-video-models-1743cee9]], available on fal at $0.05–$0.20/s by resolution [[wan-3-0-text-to-video-api-on-fal-581fd1f9]]; and **[[minimax-h3]] (768p)** as #1 image-to-video (AA-Video-I2V v1.1, Elo 1140, $34.12/min AA-measured) and #1 open-weights text-to-video (Elo 1158, #3 overall) [[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]]. [[seedance]] (Seedance 2.5) is now live on fal under `bytedance/seedance-2.5/us` (~$0.47/s at 720p) [[seedance-2-5-us-image-to-video-api-on-fal-f520e761]]; Seedance 2.0 720p remains #1 on the AA I2V audio-output board (Elo 1197) [[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]. MiniMax H3 retains open-weight checkpoints under the MiniMax H3 Community License [[minimaxai-minimax-h3-hugging-face-1f0e60fd]]. [[flux-3-max]] (BFL/fal, $0.085/s) covers text-to-video, image-to-video and keyframes-to-video on fal [[flux-3-max-text-and-image-to-video-post-trained-by-fal-4991600a]]; [[kling]] (Kling 4.0, API + Replicate, API preview pricing for 4.0) and [[sora]] (shutdown Sep 24, 2026) round out the video entity roster.

> Wan 3.0 currently leads AA-Video-T2V v2.1 with an Elo score of 1174. [[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]]

> MiniMax H3 (768p) currently leads among open weights models on AA-Video-T2V v2.1 with an Elo score of 1158. [[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]]

**Speech.** Inworld's Realtime TTS-2 targets in-game conversational use with sub-130 ms first-chunk latency, inline plain-language voice direction and one voice identity across 100+ languages, and was #1 realtime TTS on the Artificial Analysis Speech Arena at launch [[realtime-tts-2-a-new-frontier-voice-model-that-feels-as-real-as-you-68a9e733]]; ElevenLabs (Eleven v3) targets multilingual NPC voice with an Unreal Engine integration [[ai-voice-for-games-elevenlabs-31e6ac62]]. Both are speech entities in [[audio-tools]]; their pricing and commercial-use terms are open questions.

> #1 realtime TTS by real users on the Artificial Analysis Speech Arena with sub-130ms first-chunk latency

> ElevenLabs has released Eleven v3, a text-to-speech model that performs text with human-like emotion, timing, and nuance. The AI voice technology is designed for easy integration with Unreal Engine.

**Image, music, SFX, sprites.** No sources yet. The researcher's first runs should seed the `image-tools` and `video-tools` comparison pages once at least two tool entities per modality exist; the 3D and motion side of the same tool roster is owned by [[ai-in-game-dev]] (see [[3d-tools]] and [[rig-and-motion-tools]]).

## Recent updates

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

> From topic Summary: "On the Artificial Analysis leaderboards H3 ranks #1 in Video Editing, #2 in Text-to-Video, and #3 in Image-to-Video."

> From source [[minimaxai-minimax-h3-hugging-face-1f0e60fd]]: No mention of Artificial Analysis or arena rankings in any excerpt.

## Open questions

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

## See also

- [[audio-tools]]
- [[ai-in-game-dev]]
- [[frontier-models]]
- [[game-music]]
- [[wan-3]]
