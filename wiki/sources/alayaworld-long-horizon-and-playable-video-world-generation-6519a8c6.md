---
fetched_at: &id001 2026-07-24
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 6519a8c697c866422866d153afd2c630fe208b31157d966d7c1af21142eeb818
sources: []
title: 'AlayaWorld: Long-Horizon and Playable Video World Generation'
topic: ai-in-game-dev
url: https://arxiv.org/abs/2607.06291
---

## Excerpts

> AlayaWorld is a full-stack open-source framework for building interactive generative worlds. These models autoregressively synthesize future observations conditioned on the current world state and user interactions, enabling playable worlds to be generated online.

> AlayaWorld enables open-ended real-time interaction, allowing users to freely navigate and perform diverse actions such as combat, spell casting, and monster summoning. The model generates consistent video sequences from a scene while responding to camera instructions, text prompts, and player interactions, maintaining coherence across durations that typically cause other video generation models to drift or reset.

> AlayaWorld is an interactive world model built on top of the LTX-2.3. Built on a 15B video diffusion transformer, AlayaWorld generates short latent chunks autoregressively under camera trajectories and switchable text prompts. Runtime performance is achieved through DMD (Distribution Matching Distillation) distillation, which compresses the diffusion sampling process from the 50-100 steps typical of high-quality video generation down to four denoising steps per chunk.

> AlayaLab released AlayaWorld as an open source model under an Apache 2.0 license. Trained on both gameplay recordings and real-world videos, they can capture diverse visual appearances and physical dynamics, opening new opportunities for interactive applications beyond gaming, including embodied intelligence.