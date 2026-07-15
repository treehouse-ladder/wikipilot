---
fetched_at: &id001 2026-07-15
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 855a6af75157f73e60daf0d0899e185a97445d7b934bef454a0ff69a5719ee7d
sources: []
title: 'Rigel3D: Rig-aware Latents for Animation-Ready 3D Asset Generation'
topic: ai-in-game-dev
url: https://arxiv.org/abs/2605.13129
---

## Excerpts

> Recent 3D generative models can synthesize high-quality assets, but their outputs are typically static: they lack the skeletal rigs, joint hierarchies, and skinning weights required for animation. This limits their use in games, film, simulation, virtual agents, and embodied AI, where assets must not only look plausible but also move plausibly.

> Unlike post-hoc auto-rigging methods that attach rigs to completed shapes, the method jointly models geometry and rig structure through coupled surface and skeleton structured latent representations. A rig-aware autoencoder decodes these representations into mesh geometry, skeleton topology, joint coordinates, and skinning weights, while a two-stage latent generative model synthesizes both surface and skeleton representations for image-conditioned generation.

> The method introduces an open-vocabulary joint labeling module that embeds generated joints into a shared vision-language space, enabling correspondence to arbitrary retargeting templates. Experiments on large-scale rigged asset datasets demonstrate that the method generates diverse, high-quality animation-ready assets and outperforms existing rigging baselines across multiple metrics.