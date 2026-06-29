---
fetched_at: &id001 2026-06-29
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 61ac650cc3ded55901647da3783f72e3ebcd9a8ae0d076f8570bec5666fd227e
sources: []
title: LLM Agents Can See Code Repositories
topic: agentic-coding
url: https://arxiv.org/abs/2606.14061
---

## Excerpts

> Human developers see code repositories, where folder hierarchies, file dependencies, and syntax highlighting convey critical semantics, while modern coding agents rely almost entirely on text.

> Experiments across four modern multimodal models reveal that while a vision-only context representation degrades performance and inflates token costs, integrating visualized context graphs as a supplementary modality can help agents grasp the repository more efficiently.

> The repository is provided as both image and text: the image is split into patches, encoded by a ViT into visual tokens, projected into the LLM embedding space, and concatenated with text tokens, preserving spatial topology for dependency reasoning.