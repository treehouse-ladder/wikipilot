---
title: "Hy-Nomas"
kind: entity
aliases: ["Hy-Nomas", "HunyuanNomas", "tencent/Hy-Nomas"]
sources:
  - "[[tencent-opens-hy-nomas-an-interactive-video-world-model-running-on-one-rtx-4090-7543a82b]]"
last_updated: 2026-10-30
last_verified: 2026-10-30
freshness_window_days: 30
profile: tool
modality: video
tasks: ["interactive-video-generation", "world-model", "text-to-video"]
vendor: "Tencent Hunyuan"
model_ids: ["tencent/Hy-Nomas"]
access: ["open-weights"]
open_weights_license: "Apache-2.0"
hardware_floor: "24 GB VRAM (RTX 4090 with CPU offload, INT8-quantized distilled version)"
pricing: "open-weights, no API pricing (2026-10-30)"
pricing_source: "[[tencent-opens-hy-nomas-an-interactive-video-world-model-running-on-one-rtx-4090-7543a82b]]"
commercial_use: "allowed (Apache-2.0) (2026-10-30)"
commercial_use_source: "[[tencent-opens-hy-nomas-an-interactive-video-world-model-running-on-one-rtx-4090-7543a82b]]"
status: active
status_source: "[[tencent-opens-hy-nomas-an-interactive-video-world-model-running-on-one-rtx-4090-7543a82b]]"
last_release: 2026-10-21
arena_rank: []
arena_rank_source: []
---

## Summary

**Hy-Nomas** is Tencent's Hunyuan team's open-source interactive video world model, released to GitHub and Hugging Face under Apache 2.0 on ~October 21, 2026 [[tencent-opens-hy-nomas-an-interactive-video-world-model-running-on-one-rtx-4090-7543a82b]]. It is an 8B diffusion transformer that supports multi-turn interaction: users describe a scene, then steer it with free-form text instructions and camera trajectories while the model continues generating new segments — without restarting from scratch.

> Tencent released Hy-Nomas under Apache 2.0 in the week of October 21, 2026, with weights on Hugging Face (tencent/Hy-Nomas). The model is an 8B diffusion transformer trained for interactive video world generation. [[tencent-opens-hy-nomas-an-interactive-video-world-model-running-on-one-rtx-4090-7543a82b]]

> During generation, users can issue new free-form text instructions or camera trajectory controls at each segment boundary — multi-turn steering without restarting from scratch. [[tencent-opens-hy-nomas-an-interactive-video-world-model-running-on-one-rtx-4090-7543a82b]]

A distilled INT8-quantized version runs on a single RTX 4090 with CPU offload, generating a 100-second clip at 1280×704 24 FPS with peak GPU memory of 20.53 GiB [[tencent-opens-hy-nomas-an-interactive-video-world-model-running-on-one-rtx-4090-7543a82b]].

> A distilled, INT8-quantized version runs on a single RTX 4090 with CPU offload, generating a 100-second clip at 1280×704, 24 FPS, with peak GPU memory of 20.53 GiB. [[tencent-opens-hy-nomas-an-interactive-video-world-model-running-on-one-rtx-4090-7543a82b]]

The release includes **Hy-Nomas-Bench**, a self-reported benchmark of 280 test cases across multi-turn free-form text, camera navigation, interleaved text+camera control, and spatial memory; the accompanying arXiv paper appeared October 27, 2026. No third-party evaluation is available at launch (see Disputes).

> The release includes Hy-Nomas-Bench, a benchmark of 280 test cases designed to evaluate interaction controllability in video world models. The accompanying arXiv paper appeared October 27, 2026. [[tencent-opens-hy-nomas-an-interactive-video-world-model-running-on-one-rtx-4090-7543a82b]]

## Disputes

- [[tencent-opens-hy-nomas-an-interactive-video-world-model-running-on-one-rtx-4090-7543a82b]] (Tencent) claims Hy-Nomas performance on Hy-Nomas-Bench (280 test cases, four axes); no independent third-party evaluation published at launch. Status: unresolved — all benchmark figures are self-reported by the model authors.

## Open questions

- [ ] Hy-Nomas public API or fal.ai/Replicate endpoint availability; no commercial API announced at launch.
- [ ] Independent third-party arena placement — no Artificial Analysis or arena.ai ranking at launch.
- [ ] Full (non-distilled, non-INT8) hardware floor for the 8B base model.
- [ ] Commercial-use terms for the Hy-Nomas-Bench arXiv paper and the benchmark dataset itself (model weights are Apache-2.0; benchmark dataset license not stated).

## See also

- [[generative-media-models]]
- [[video-tools]]
- [[minimax-h3]]
