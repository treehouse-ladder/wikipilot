---
fetched_at: &id001 2026-06-12
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: e823a3200754a840040e2e28fb8cf05ae094a24f51a1be2cc4eb1337ada0321c
sources: []
title: 'HDSL: A Hierarchical Domain-Specific Language for Structured 3D Indoor Scene
  Generation and Localized Editing with LLM Agents'
topic: ai-in-game-dev
url: https://arxiv.org/abs/2606.09738
---

## Excerpts

> HDSL (Hierarchical Descriptive Scene Language) is an XML/CSS-style domain-specific language for structured 3D indoor scenes. HDSL represents rooms, regions, objects, and support surfaces as a tree with local coordinates, making complex scenes easier to plan recursively and easier to retrieve for editing.

> Existing LLM-based systems often rely on scene graphs or global constraint lists, which are compact but underspecify local geometry and make instruction-based edits difficult to localize.

> The pipeline uses LLM agents to generate HDSL subtrees with bounded verification, grounds non-virtual nodes through multimodal asset retrieval, and applies force-directed layout optimization to repair boundary and collision errors.