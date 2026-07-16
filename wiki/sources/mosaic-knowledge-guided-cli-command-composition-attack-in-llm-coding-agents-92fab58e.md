---
fetched_at: &id001 2026-07-16
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 92fab58e59598c2d13e9ee36ddfd54d4c38c86f3c66cabae1b6a5566ef83b350
sources: []
title: 'MOSAIC: Knowledge-Guided CLI Command Composition Attack in LLM Coding Agents'
topic: agentic-coding
url: https://arxiv.org/abs/2607.02857
---

## Excerpts

> Individually benign commands can form a dangerous producer-consumer state relation across the command trace, exposing what we call CLI command-composition risk (CCR). Following Unix design, these commands cooperate through shared operating-system state where one command may write state that a later command reads.

> MOSAIC is a knowledge-guided framework that distills validated command-state behaviors from CVEs, advisories, and researcher PoCs into reusable summaries, composes them into exploit paths, and instantiates them as realistic developer workflows for blackbox agent evaluation.

> Across five real-world CLI coding agents and five backend LLMs over 2,525 trials, MOSAIC achieves a 96.59% attack success rate under benign developer tasks.