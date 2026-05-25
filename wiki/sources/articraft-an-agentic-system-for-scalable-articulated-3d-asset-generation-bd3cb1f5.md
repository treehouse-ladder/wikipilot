---
fetched_at: 2026-05-25
freshness_window_days: 365
image_count: 0
kind: source
last_updated: 2026-05-25
last_verified: 2026-05-25
sha256: bd3cb1f57d490f9d0f0b447409c525c3021fdc914e93d6029dae5611f508207c
sources: []
title: 'Articraft: An Agentic System for Scalable Articulated 3D Asset Generation'
topic: ai-in-game-dev
url: https://arxiv.org/abs/2605.15187
---

## Excerpts

> We reduce the problem of generating an articulated 3D asset to that of writing a program that builds it. We then introduce a new agentic system, Articraft, that writes such programs automatically.

> the LLM writing code against a domain-specific SDK for defining parts, composing geometry, specifying joints, and writing tests to validate the resulting assets, while the harness exposes a restricted workspace and interface to the LLM, validates the resulting assets, and returns structured feedback.

> Using Articraft, researchers built Articraft-10K, a curated dataset of over 10K articulated assets spanning 245 categories, with utility for training models of articulated assets and downstream applications such as robotics simulation and virtual reality.

> SDK support for revolute, prismatic, continuous, and fixed joints with explicit origins, axes, and motion limits. The compiled URDF preserves kinematic structure, so the output is not only visual geometry but also a structured representation of how parts move.

> This produces higher-quality assets than both state-of-the-art articulated-asset generators and general-purpose coding agents.