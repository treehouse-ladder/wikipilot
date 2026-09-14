---
fetched_at: &id001 2026-09-14
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: b771098d5cbe5b1ce3fe923920dc2e9e2aac2b33c0094cc010e7022304031b78
sources: []
title: Programmable World Model
topic: ai-in-game-dev
url: https://arxiv.org/abs/2609.10540
---

## Excerpts

> An agent translates natural-language instructions into executable programs that specify entity states and state-transition rules, enabling direct control over individual entities and their interactions. A lightweight engine executes these programs to update and maintain an explicit, persistent global world state, including off-screen entities and non-visual attributes.

> To connect world state with visual generation, we introduce state-augmented 3D oriented bounding boxes (OBBs) as an intermediate representation, which together with the target camera trajectory, is deterministically compiled into pixel-aligned spatiotemporal conditioning signals for a pretrained video model serving as the generative renderer.

> This design allows users to create playable games with predefined mechanics, direct control over individual entities, and persistent world state. The method achieves 94% Count Accuracy and 98% State Accuracy, substantially outperforming existing interactive video world models while supporting coherent long-horizon generation.