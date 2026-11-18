---
title: "Qwen-Image-2512"
kind: entity
aliases: ["Qwen Image 2512", "qwen-image-2512", "Qwen-Image", "Qwen Image"]
profile: tool
modality: image
tasks: ["text-to-image"]
vendor: "Alibaba Qwen"
model_ids: ["Qwen/Qwen-Image-2512"]
access: ["open-weights"]
open_weights_license: "Apache-2.0"
hardware_floor: "~24 GB VRAM (Q3-quantized ~23.4 GB); full repo ~57.7 GB"
pricing: "unknown"
pricing_source: null
commercial_use: "allowed (Apache-2.0) (2026-11-18)"
commercial_use_source: "[[qwen-qwen-image-2512-4bc8318c]]"
status: "active"
status_source: "[[qwen-qwen-image-2512-4bc8318c]]"
last_release: 2026-12-01
arena_rank: []
arena_rank_source: []
sources: ["[[qwen-qwen-image-2512-4bc8318c]]"]
last_updated: 2026-11-18
last_verified: 2026-11-18
freshness_window_days: 30
---

# Qwen-Image-2512

## Summary

Qwen-Image-2512 is the December 2026 update of Alibaba's Qwen-Image text-to-image foundation model: a 20-billion-parameter model released under the Apache-2.0 license, making it fully open-weights with commercial use permitted [[qwen-qwen-image-2512-4bc8318c]]. The vendor describes it as the strongest open-source model on AI Arena blind evaluations, though independent arena placement is contested (see Open questions below).

The full model repository weighs approximately 57.7 GB (transformer ~40.9 GB). Community MFlux quantizations are available from Q8 (~36.1 GB) down to Q3 (~23.4 GB), making it self-hostable on a ~24 GB workstation GPU or Apple Silicon device [[qwen-qwen-image-2512-4bc8318c]]. The Apache-2.0 license makes it a candidate for game-asset pipelines requiring fully self-hosted, redistributable image generation.

There is no known hosted API offering (fal, Replicate, etc.) at the time of ingestion, so access is currently open-weights / self-host only. No per-call pricing is available.

> Qwen-Image-2512 is the December update of the Qwen-Image text-to-image foundational model, a 20B-parameter model released under the Apache-2.0 license. The results show that Qwen-Image-2512 is currently the strongest open-source model on AI Arena blind evaluations. [[qwen-qwen-image-2512-4bc8318c]]

## Disputes

## Open questions

- [ ] Qwen-Image-2512 independent AA-Image-T2I v2.1 open-weights placement — vendor claims strongest open-source on AI Arena, but AA open-weights snapshots conflict (readings ~Elo 998-1172) and currently place it below the open-weights board leader [[minimax-h3-image]]; confirm a clean, dated figure [[qwen-qwen-image-2512-4bc8318c]].
- [ ] Qwen-Image-2512 hosted API availability (fal / Replicate) and per-call price, and confirmed minimum-VRAM hardware floor per quantization tier [[qwen-qwen-image-2512-4bc8318c]].

## See also

- [[generative-media-models]]
- [[image-tools]]
- [[minimax-h3-image]]
