---
title: "MiniMax H3"
kind: entity
aliases: ["MiniMax-H3", "Hailuo H3", "MiniMaxAI/MiniMax-H3"]
sources:
  - "[[minimaxai-minimax-h3-hugging-face-1f0e60fd]]"
  - "[[minimax-releases-minimax-h3-an-omni-modal-video-model-that-generates-15-second-2k-clips-with-native-stereo-audio-53db5121]]"
  - "[[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]"
  - "[[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]]"
  - "[[aa-video-i2v-v2-1-leaderboard-top-ai-video-models-7458c112]]"
last_updated: 2026-10-31
last_verified: 2026-10-31
freshness_window_days: 30
profile: tool
modality: video
tasks: ["text-to-video", "image-to-video", "video-editing", "first-last-frame", "subject-reference", "motion-reference", "native-stereo-audio"]
vendor: "MiniMax"
model_ids: ["MiniMaxAI/MiniMax-H3"]
access: ["api", "open-weights"]
open_weights_license: "MiniMax H3 Community License Agreement"
hardware_floor: unknown
pricing: "AA-measured $34.12/min (768p image-to-video, AA-Video-I2V v1.1) (2026-10-26)"
pricing_source: "[[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]"
commercial_use: "permitted with attribution for organizations below an annual-revenue threshold (figure illegible in source); open weights regionally restricted (2026-08-03)"
commercial_use_source: "[[minimaxai-minimax-h3-hugging-face-1f0e60fd]]"
status: active
status_source: "[[minimaxai-minimax-h3-hugging-face-1f0e60fd]]"
last_release: unknown
arena_rank:
  - "Artificial Analysis Image-to-Video v2.1 (audio output, 768p): #4 overall, #1 open-weights, Elo 1129 (2026-10-31)"
  - "Artificial Analysis Image-to-Video v1.1 (768p): #1, Elo 1140 (2026-10-28)"
  - "Artificial Analysis Text-to-Video (AA-Video-T2V v2.1, open weights): #1, Elo 1158 (2026-10-28)"
arena_rank_source:
  - "[[aa-video-i2v-v2-1-leaderboard-top-ai-video-models-7458c112]]"
  - "[[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]"
  - "[[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]]"
---

# MiniMax H3

## Summary

MiniMax H3 is an omni-modal video model that generates 15-second 2K clips with native stereo audio from unified text, image, video and audio context, folding text-to-video, image-to-video, first-and-last-frame, subject reference, motion reference and video editing into one pretraining paradigm [[minimax-releases-minimax-h3-an-omni-modal-video-model-that-generates-15-second-2k-clips-with-native-stereo-audio-53db5121]]. MiniMax quotes pricing only relative to "mainstream models" (under a third per second at 2K, under half at 768p), so no absolute `pricing` is recorded [[minimax-releases-minimax-h3-an-omni-modal-video-model-that-generates-15-second-2k-clips-with-native-stereo-audio-53db5121]].

> At 2K, H3's per-second price is less than a third of mainstream models; at 768p, less than half the price of mainstream 720p. Open weights are promised 'in the coming days,' not shipped; the API is the only path today.

The Hugging Face repository (fetched two days later) carries the weights as two task-specific checkpoints totalling 288 GB under the MiniMax H3 Community License, which permits commercial use with attribution for organizations under an annual-revenue threshold whose figure is illegible in the ingested excerpt; open weights are temporarily restricted in some regions. On Artificial Analysis, H3 ranks #1 in Video Editing, #2 in Text-to-Video and #3 in Image-to-Video [[minimaxai-minimax-h3-hugging-face-1f0e60fd]].

> The weights are released under the MiniMax H3 Community License Agreement, which permits commercial use for organizations under 0M annual revenue with attribution, though open weights are temporarily limited in certain regions until the regulatory and compliance framework becomes clearer. On the Artificial Analysis leaderboards H3 ranks #1 in Video Editing, #2 in Text-to-Video, and #3 in Image-to-Video.

The Artificial Analysis AA-Video-I2V v1.1 leaderboard (October 2026) shows MiniMax H3 768p at #1 with Elo 1140, and lists its API price at $34.12/min [[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]. On the AA-Video-T2V v2.1 board (October 28, 2026), MiniMax H3 768p sits at #3 overall (Elo 1158) and #1 among open-weights models [[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]].

> MiniMax H3 (768p) currently leads among open weights models on AA-Video-T2V v2.1 with an Elo score of 1158. [[aa-video-t2v-v2-1-leaderboard-top-ai-video-models-050f7208]]

> MiniMax H3 (768p) currently leads AA-Video-I2V v1.1 with an Elo score of 1140. Its listed API price is $34.12 /min. [[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]]

## Disputes

- [[minimax-releases-minimax-h3-an-omni-modal-video-model-that-generates-15-second-2k-clips-with-native-stereo-audio-53db5121]] claims open weights were "promised, not shipped" and the API was the only access path; [[minimaxai-minimax-h3-hugging-face-1f0e60fd]] claims the 288 GB weights are published on Hugging Face. Status: resolved-toward-B — the HF card is the later snapshot (2026-08-03 vs 2026-08-01), so `access` lists both `api` and `open-weights`.
- Entity Summary claims "two task-specific checkpoints totalling 288 GB" and cites [[minimaxai-minimax-h3-hugging-face-1f0e60fd]]; current version of that source (fetched 2026-10-24) contains no mention of "288 GB" or any checkpoint size. Status: unresolved (confidence: high; sweep: 2026-10-25)

> From entity: "The Hugging Face repository (fetched two days later) carries the weights as two task-specific checkpoints totalling 288 GB under the MiniMax H3 Community License"

> From source [[minimaxai-minimax-h3-hugging-face-1f0e60fd]]: "MiniMax H3 is released as two task-specific checkpoints. Each checkpoint contains a specialized Omni Transformer Model together with the required processor, tokenizer, text encoder, Visual VAE, and standalone Audio VAE components." (no size specified)

- Entity Summary, quote block, and frontmatter arena_rank claim Artificial Analysis rankings (#1 Video Editing, #2 Text-to-Video, #3 Image-to-Video) citing [[minimaxai-minimax-h3-hugging-face-1f0e60fd]]; current version of that source (fetched 2026-10-24) contains no mention of "Artificial Analysis" or any arena rankings. Status: partially-resolved — [[aa-video-i2v-v1-1-leaderboard-top-ai-video-models-d50415cf]] (2026-10-26) confirms H3 768p #1 on the I2V board (Elo 1140); #1 Video Editing and #2 T2V remain uncited.

> From entity quote block: "On the Artificial Analysis leaderboards H3 ranks #1 in Video Editing, #2 in Text-to-Video, and #3 in Image-to-Video."

> From source [[minimaxai-minimax-h3-hugging-face-1f0e60fd]]: No mention of Artificial Analysis or arena rankings in any excerpt.

## Open questions

- [ ] The Community License revenue threshold (the figure is garbled as "0M" in the ingested excerpt) — re-fetch the licence text.
- [ ] Absolute API pricing per second at 768p and 2K.
- [ ] VRAM / multi-GPU floor for the 288 GB checkpoints.
- [ ] Release date (`last_release` is `unknown`; the announcement coverage is dated 2026-08-01).
- [ ] fal / Replicate endpoint ids.

## See also

- [[generative-media-models]]
- [[frontier-models]]
- [[minimax-m3]]
