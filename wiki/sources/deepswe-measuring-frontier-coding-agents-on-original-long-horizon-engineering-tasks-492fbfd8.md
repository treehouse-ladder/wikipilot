---
fetched_at: &id001 2026-07-16
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 492fbfd88787c994950e151bd46568cdccae31b1c0c1dfcdfda2a12e10e63c26
sources: []
title: 'DeepSWE: Measuring Frontier Coding Agents on Original, Long-Horizon Engineering
  Tasks'
topic: agentic-coding
url: https://arxiv.org/abs/2607.07946
---

## Excerpts

> Its tasks are written from scratch across 91 active open-source repositories and five languages and are never contributed back upstream, so their reference solutions stay out of the public record that model training scrapes; and each task is graded by a hand-written verifier that checks the requested functionality and accepts any implementation that provides it.

> When an independent LLM judge re-reviews graded runs, it disagrees with DeepSWE's verifier about an order of magnitude less often than with SWE-Bench Pro's inherited tests (1.4% versus 32.4%).

> Despite being about half the length of SWE-Bench Pro's prompts, DeepSWE's prompts describe tasks whose reference solutions touch 5.5x more code, and the benchmark separates frontier agents across a wider score band than the leaderboards on which they otherwise cluster.