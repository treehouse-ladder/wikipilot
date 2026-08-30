---
title: 'Same Model, Different Harness: Different Coding-Agent Results'
kind: source
url: https://arxiv.org/abs/2608.26218
sha256: 22e9439185d06c73c647b1c69338fb52a9f66e266f103adbe5735802323a6c71
fetched_at: 2026-08-29
topic: agentic-coding
image_count: 0
sources: []
last_updated: 2026-08-29
last_verified: 2026-08-29
freshness_window_days: 365
---

## Excerpts

> We test two harness configurations on three benchmarks (SWE-bench Verified, SWE-bench Pro, and RE-Bench). Under tight context, mechanically shortening older tool results raises the mean fail-to-pass fraction — the same model, differently harnessed, produces substantially different benchmark outcomes.

> Our principal finding is that harness decisions — specifically how a coding agent manages context and truncates prior tool output — matter as much as model choice on established coding-agent benchmarks. A configuration that aggressively shortens stale tool results outperforms an otherwise-identical configuration that retains them, at no additional inference cost.

> This has immediate practical implications for benchmark interpretation: when a lab reports an improved SWE-bench score, the score reflects model × harness jointly. Without harness disclosure, score comparisons across labs are not apples-to-apples.
