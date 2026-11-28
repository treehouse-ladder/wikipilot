---
fetched_at: &id001 2026-11-28
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 9676145effb986088e621649f6782701088a13fcc7cf36f7429fe4a5351f6077
sources: []
title: PAN 2 — a general-purpose interactable video world model (MBZUAI IFM)
topic: generative-media-models
url: https://huggingface.co/IFM/PAN2
---

## Excerpts

> PAN 2 is a general-purpose world model: it simulates how the world will change in response to actions. Given a current observation (an optional image plus text) and actions described in text, it simulates the outcome as a video of up to 20 seconds. This supports simulative reasoning: an agent can imagine the outcomes of its candidate actions before choosing among them, by simulating each plan with PAN 2 and acting on the one whose simulated outcome is best.

> The 29B-parameter MMDiT, the perceptual reasoning backbone, trained from scratch on hundreds of millions of videos annotated in the same format, predicts the perceptual detail that the description leaves open: the video latents that realize the state, conditioned on it and on the VAE latent of the starting image. The Wan 2.2 VAE decoder renders the predicted latents as the next observation, so every prediction can be seen and checked against real footage.

> PAN 2's latent diffusion model is released as a single checkpoint that serves both tasks. The frozen text encoder (Qwen3.5-9B) and VAE (Wan 2.2) are downloaded from their own repositories.

> PAN 2 diffusion backbone (IFM/PAN2) | Text-to-video (t2v), Image-to-video (i2v) | Structured world-state caption; optional first frame | Video via the VAE decoder, 704x1248 at 24 fps, up to 20 s | BF16

> PAN 2 is developed by the Institute of Foundation Models (IFM) at MBZUAI. Its own code and weights are released under the Apache License, Version 2.0.

> PAN 2 is intended for research and development in world modeling and simulative reasoning, including simulating the outcomes of actions for agents and robotics, studying physical and causal reasoning in video, and generating video for evaluation, education, and creative work.

> PAN 2 Conceptual Reasoner skill: a Codex / Claude Code agent skill carrying the caption policy (system_prompt.md), the fixed negative prompt, and a validator for the text-encoder token budget (soft limit 1,480, hard capacity 1,536 tokens per caption).

> Long plans fail often. About two in three simulated plans contain at least one step that is not carried out. The quantitative study covers open-loop plans designed to succeed; how faithfully PAN 2 simulates plans that should fail is not yet measured.

> We strongly recommend running PAN 2 behind pan2-guardrail, which screens the request with Qwen3Guard-Gen-4B before generation and the generated video with the Q16 frame classifier after it. Use both guards.