---
title: "Pika H3 Flex"
kind: entity
aliases: ["Pika-H3-Flex", "Pika-Labs/Pika-H3-Flex"]
sources:
  - "[[introducing-pika-h3-flex-0a7ab440]]"
  - "[[pika-on-x-meet-pika-h3-flex-96454635]]"
last_updated: 2026-11-04
last_verified: 2026-11-04
freshness_window_days: 30
profile: tool
modality: video
tasks: ["text-to-video", "image-to-video", "first-last-frame", "subject-reference", "native-stereo-audio"]
vendor: "Pika Labs"
model_ids: ["Pika-Labs/Pika-H3-Flex"]
access: ["api", "open-weights"]
open_weights_license: "MiniMax H3 Community License Agreement"
hardware_floor: "80 GB VRAM (single H100 80GB tested; large requests may need CPU offloading)"
pricing: "unknown (open weights free on Hugging Face; hosted 4K upscaling and audio stem separation behind Pika API subscription, pricing not stated in sources)"
pricing_source: null
commercial_use: "permitted with attribution for organizations below an annual-revenue threshold (MiniMax H3 Community License applies to LoRA adapters); hosted API commercial terms unknown"
commercial_use_source: null
status: active
status_source: "[[introducing-pika-h3-flex-0a7ab440]]"
last_release: 2026-10-29
arena_rank:
  - "DesignArena Text-to-Video: #1 open-weights, #7 overall, Elo 1293 (2026-10-29)"
arena_rank_source:
  - "[[pika-on-x-meet-pika-h3-flex-96454635]]"
---

# Pika H3 Flex

## Summary

Pika H3 Flex is an open-weights video generation model released by Pika Labs on October 29, 2026 (open weights on Hugging Face + GitHub; Pika consumer app integration on November 2) [[introducing-pika-h3-flex-0a7ab440]]. It is a post-trained derivative of [[minimax-h3]] — LoRA adapters built on MiniMax's 33B base that cut sampling from 50 steps to 6, enabling faster-than-realtime generation: a 15-second clip with synchronized audio in as little as 7 seconds [[pika-on-x-meet-pika-h3-flex-96454635]].

> Meet Pika H3 Flex, debuting today as the #1 open weight model on DesignArena's t2v board. It's built for professional iteration, with exportable audio stems, resolutions up to 4k, and faster-than-realtime generation. It can produce a 15-second clip with soundtrack in as little as 7 sec. [[pika-on-x-meet-pika-h3-flex-96454635]]

> Everything we put into this model was designed to give creators the flexibility and speed to explore with precision. In that spirit, we're making Pika H3 Flex open source from day 1. You can find the code on GitHub, the weights on @huggingface, and start playing with it in @ComfyUI. [[pika-on-x-meet-pika-h3-flex-96454635]]

Native output is 480p or 768p at 24 fps, running 5–15 seconds, across eleven aspect ratios from 21:9 down to 9:21. The model supports up to 12 reference inputs (9 images, 3 videos, 3 audio clips). Upscaling to 1080p, 2K, and 4K plus audio stem separation are available only via the hosted Pika API (subscription, pricing undisclosed in ingested sources) [[introducing-pika-h3-flex-0a7ab440]]. The open release consists of LoRA adapters (not full 33B weights) plus inference code on GitHub and ComfyUI nodes; Pika tested on single NVIDIA H100 80GB GPUs.

At launch, Pika H3 Flex ranked **#7 overall and #1 among open-weights models** on DesignArena's text-to-video board (Elo 1293) [[pika-on-x-meet-pika-h3-flex-96454635]]. The adapters are distributed under the MiniMax H3 Community License Agreement; example code uses Apache 2.0.

## Disputes

- Multiple sources disagree on the license: emergent.sh states "MiniMax H3 Community License Agreement"; maverickframe.com says adapters are under the same license while example code is Apache 2.0; screenweaver.ai reports the Hugging Face card lists the license as "other" with no named license in the press release. Status: unresolved. The Hugging Face model card (Pika-Labs/Pika-H3-Flex) is the authoritative source but could not be fetched.

## Open questions

- [ ] Confirm the actual license on the Hugging Face model card (Pika-Labs/Pika-H3-Flex) — sources conflict between MiniMax H3 Community License and "other" [[introducing-pika-h3-flex-0a7ab440]]
- [ ] Pika hosted API pricing for 4K upscaling and audio stem separation — not stated in any ingested source.
- [ ] Commercial-use terms for the hosted API (game-dev shipping rights) — not stated.
- [ ] Placement on Artificial Analysis AA-Video-T2V v2.1 board — search results do not confirm an AA entry for Pika H3 Flex [[pika-on-x-meet-pika-h3-flex-96454635]].
- [ ] Multi-GPU requirement for full 33B MiniMax H3 base (LoRA adapters run on H100 80GB, but whether a local deployment of the full model is practical on consumer hardware is undocumented in sources).

## See also

- [[minimax-h3]]
- [[generative-media-models]]
- [[video-tools]]
