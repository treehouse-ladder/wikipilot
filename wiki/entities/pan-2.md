---
title: "PAN 2"
kind: entity
profile: tool
modality: video
tasks: ["text-to-video", "image-to-video", "world-model", "action-simulation"]
vendor: "MBZUAI"
model_ids: ["IFM/PAN2"]
access: ["open-weights"]
open_weights_license: "Apache-2.0"
hardware_floor: unknown
pricing: "open-weights, self-hosted (2026-11-28)"
pricing_source: "[[pan-2-a-general-purpose-interactable-video-world-model-mbzuai-ifm-9676145e]]"
commercial_use: "allowed under Apache-2.0 (2026-11-28)"
commercial_use_source: "[[pan-2-a-general-purpose-interactable-video-world-model-mbzuai-ifm-9676145e]]"
status: active
status_source: "[[pan-2-a-general-purpose-interactable-video-world-model-mbzuai-ifm-9676145e]]"
last_release: unknown
arena_rank: []
arena_rank_source: []
sources: ["[[pan-2-a-general-purpose-interactable-video-world-model-mbzuai-ifm-9676145e]]"]
last_updated: 2026-11-28
last_verified: 2026-11-28
freshness_window_days: 30
---

# PAN 2

## Summary

PAN 2 is a general-purpose video world model from MBZUAI's Institute of Foundation Models (IFM), designed for **simulative reasoning** in agentic pipelines: given an optional starting image and an action description in text, it simulates the resulting world state as a video of up to 20 seconds [[pan-2-a-general-purpose-interactable-video-world-model-mbzuai-ifm-9676145e]].

**Architecture.** A 29B-parameter MMDiT backbone trained from scratch on hundreds of millions of action-annotated videos, a frozen Qwen3.5-9B text encoder, and the frozen Wan 2.2 VAE decoder. Output resolution is 704×1248 at 24 fps in BF16. The single `IFM/PAN2` checkpoint serves both text-to-video (t2v) and image-to-video (i2v) tasks [[pan-2-a-general-purpose-interactable-video-world-model-mbzuai-ifm-9676145e]].

> PAN 2 is a general-purpose world model: it simulates how the world will change in response to actions. Given a current observation (an optional image plus text) and actions described in text, it simulates the outcome as a video of up to 20 seconds. [[pan-2-a-general-purpose-interactable-video-world-model-mbzuai-ifm-9676145e]]

**Agentic use case.** A planning agent can run PAN 2 as a forward model — simulate N candidate action sequences, evaluate the simulated outcomes, and commit only to the best-rated plan. The model card includes a **Conceptual Reasoner** skill for Claude Code / Codex agents: a system prompt carrying the caption policy and a token-budget validator (soft limit 1,480; hard capacity 1,536 tokens per caption) [[pan-2-a-general-purpose-interactable-video-world-model-mbzuai-ifm-9676145e]].

> PAN 2 Conceptual Reasoner skill: a Codex / Claude Code agent skill carrying the caption policy (system_prompt.md), the fixed negative prompt, and a validator for the text-encoder token budget (soft limit 1,480, hard capacity 1,536 tokens per caption). [[pan-2-a-general-purpose-interactable-video-world-model-mbzuai-ifm-9676145e]]

> The 29B-parameter MMDiT, the perceptual reasoning backbone, trained from scratch on hundreds of millions of videos annotated in the same format, predicts the perceptual detail that the description leaves open: the video latents that realize the state, conditioned on it and on the VAE latent of the starting image. [[pan-2-a-general-purpose-interactable-video-world-model-mbzuai-ifm-9676145e]]

**Safety.** MBZUAI strongly recommends running PAN 2 behind `pan2-guardrail`: Qwen3Guard-Gen-4B screens the request before generation; the Q16 frame classifier checks the generated video after [[pan-2-a-general-purpose-interactable-video-world-model-mbzuai-ifm-9676145e]].

> We strongly recommend running PAN 2 behind pan2-guardrail, which screens the request with Qwen3Guard-Gen-4B before generation and the generated video with the Q16 frame classifier after it. [[pan-2-a-general-purpose-interactable-video-world-model-mbzuai-ifm-9676145e]]

**Known limitation.** Long plans fail often: about two in three simulated plans contain at least one step that is not carried out [[pan-2-a-general-purpose-interactable-video-world-model-mbzuai-ifm-9676145e]].

> Long plans fail often. About two in three simulated plans contain at least one step that is not carried out. The quantitative study covers open-loop plans designed to succeed; how faithfully PAN 2 simulates plans that should fail is not yet measured. [[pan-2-a-general-purpose-interactable-video-world-model-mbzuai-ifm-9676145e]]

## Disputes

## Open questions

- [ ] Hardware floor (minimum VRAM) for running PAN 2 — not stated in the source; the 29B MMDiT backbone alone is substantial [[pan-2-a-general-purpose-interactable-video-world-model-mbzuai-ifm-9676145e]].
- [ ] Whether the guardrail models (`pan2-guardrail`, Qwen3Guard-Gen-4B, Q16 frame classifier) are separately open-weights and what their hardware requirements are [[pan-2-a-general-purpose-interactable-video-world-model-mbzuai-ifm-9676145e]].
- [ ] Arena placement on any standard video generation benchmark (AA-Video-T2V, AA-Video-I2V) — not evaluated in ingested sources.
- [ ] How faithfully PAN 2 simulates plans that *should* fail — explicitly marked as not yet measured [[pan-2-a-general-purpose-interactable-video-world-model-mbzuai-ifm-9676145e]].

## See also

- [[generative-media-models]] — topic index (video and tool roster)
- [[wan-3]] — current AA-Video-T2V leader
- [[seedance]] — current AA-Video-I2V leader
- [[minimax-h3]] — current open-weights video leader
