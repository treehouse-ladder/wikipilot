---
title: "MiniMax H3"
kind: entity
aliases: ["MiniMax-H3", "Hailuo H3", "MiniMaxAI/MiniMax-H3"]
sources:
  - "[[minimaxai-minimax-h3-hugging-face-1f0e60fd]]"
  - "[[minimax-releases-minimax-h3-an-omni-modal-video-model-that-generates-15-second-2k-clips-with-native-stereo-audio-53db5121]]"
last_updated: 2026-10-25
last_verified: 2026-10-24
freshness_window_days: 30
profile: tool
modality: video
tasks: ["text-to-video", "image-to-video", "video-editing", "first-last-frame", "subject-reference", "motion-reference", "native-stereo-audio"]
vendor: "MiniMax"
model_ids: ["MiniMaxAI/MiniMax-H3"]
access: ["api", "open-weights"]
open_weights_license: "MiniMax H3 Community License Agreement"
hardware_floor: unknown
pricing: unknown
pricing_source: null
commercial_use: "permitted with attribution for organizations below an annual-revenue threshold (figure illegible in source); open weights regionally restricted (2026-08-03)"
commercial_use_source: "[[minimaxai-minimax-h3-hugging-face-1f0e60fd]]"
status: active
status_source: "[[minimaxai-minimax-h3-hugging-face-1f0e60fd]]"
last_release: unknown
arena_rank:
  - "Artificial Analysis Video Editing: #1 (2026-08-03)"
  - "Artificial Analysis Text-to-Video: #2 (2026-08-03)"
  - "Artificial Analysis Image-to-Video: #3 (2026-08-03)"
arena_rank_source:
  - "[[minimaxai-minimax-h3-hugging-face-1f0e60fd]]"
  - "[[minimaxai-minimax-h3-hugging-face-1f0e60fd]]"
  - "[[minimaxai-minimax-h3-hugging-face-1f0e60fd]]"
---

# MiniMax H3

## Summary

MiniMax H3 is an omni-modal video model that generates 15-second 2K clips with native stereo audio from unified text, image, video and audio context, folding text-to-video, image-to-video, first-and-last-frame, subject reference, motion reference and video editing into one pretraining paradigm [[minimax-releases-minimax-h3-an-omni-modal-video-model-that-generates-15-second-2k-clips-with-native-stereo-audio-53db5121]]. MiniMax quotes pricing only relative to "mainstream models" (under a third per second at 2K, under half at 768p), so no absolute `pricing` is recorded [[minimax-releases-minimax-h3-an-omni-modal-video-model-that-generates-15-second-2k-clips-with-native-stereo-audio-53db5121]].

> At 2K, H3's per-second price is less than a third of mainstream models; at 768p, less than half the price of mainstream 720p. Open weights are promised 'in the coming days,' not shipped; the API is the only path today.

The Hugging Face repository (fetched two days later) carries the weights as two task-specific checkpoints totalling 288 GB under the MiniMax H3 Community License, which permits commercial use with attribution for organizations under an annual-revenue threshold whose figure is illegible in the ingested excerpt; open weights are temporarily restricted in some regions. On Artificial Analysis, H3 ranks #1 in Video Editing, #2 in Text-to-Video and #3 in Image-to-Video [[minimaxai-minimax-h3-hugging-face-1f0e60fd]].

> The weights are released under the MiniMax H3 Community License Agreement, which permits commercial use for organizations under 0M annual revenue with attribution, though open weights are temporarily limited in certain regions until the regulatory and compliance framework becomes clearer. On the Artificial Analysis leaderboards H3 ranks #1 in Video Editing, #2 in Text-to-Video, and #3 in Image-to-Video.

## Disputes

- [[minimax-releases-minimax-h3-an-omni-modal-video-model-that-generates-15-second-2k-clips-with-native-stereo-audio-53db5121]] claims open weights were "promised, not shipped" and the API was the only access path; [[minimaxai-minimax-h3-hugging-face-1f0e60fd]] claims the 288 GB weights are published on Hugging Face. Status: resolved-toward-B — the HF card is the later snapshot (2026-08-03 vs 2026-08-01), so `access` lists both `api` and `open-weights`.
- Entity Summary claims "two task-specific checkpoints totalling 288 GB" and cites [[minimaxai-minimax-h3-hugging-face-1f0e60fd]]; current version of that source (fetched 2026-10-24) contains no mention of "288 GB" or any checkpoint size. Status: unresolved (confidence: high; sweep: 2026-10-25)

> From entity: "The Hugging Face repository (fetched two days later) carries the weights as two task-specific checkpoints totalling 288 GB under the MiniMax H3 Community License"

> From source [[minimaxai-minimax-h3-hugging-face-1f0e60fd]]: "MiniMax H3 is released as two task-specific checkpoints. Each checkpoint contains a specialized Omni Transformer Model together with the required processor, tokenizer, text encoder, Visual VAE, and standalone Audio VAE components." (no size specified)

- Entity Summary, quote block, and frontmatter arena_rank claim Artificial Analysis rankings (#1 Video Editing, #2 Text-to-Video, #3 Image-to-Video) citing [[minimaxai-minimax-h3-hugging-face-1f0e60fd]]; current version of that source (fetched 2026-10-24) contains no mention of "Artificial Analysis" or any arena rankings. Status: unresolved (confidence: high; sweep: 2026-10-25)

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
