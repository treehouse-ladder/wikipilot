---
fetched_at: &id001 2026-10-18
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 00d52fc8d595b78821b44d40fdf3624d6c2592572d3d7238e15defe7c3254ce4
sources: []
title: Artificial Analysis Decision Index v1.0
topic: frontier-models
url: https://artificialanalysis.ai/articles/artificial-analysis-decision-index
---

## Excerpts

> The Decision Index benchmarks decision models, which choose from a fixed set of options and attach a probability to each in a single call. These models are built for speed and low cost rather than long reasoning chains.

> The index has four equally weighted evaluations, each at 25%: AA-Omniscience-Decision (knowledge and hallucination), HLE-MultiChoice (reasoning), When2Call (tool calling), and WildGuardTest (classification, scored by average F1).

> The tool-calling slot is When2Call, NVIDIA's test. Each item offers four candidate replies, and the model must pick whether to answer directly, call a tool, ask for more information, or say it cannot answer. The reply order is shuffled per task.