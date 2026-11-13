---
title: "Gemini 4 Hydrogen"
kind: entity
aliases: ["Hydrogen", "gemini-4-hydrogen", "Gemini 4 Hydrogen (High)"]
sources:
  - "[[gemini-4-hydrogen-model-card-google-deepmind-441ce58c]]"
  - "[[introducing-gemini-4-hydrogen-for-agentic-workflows-d7c21c50]]"
  - "[[gemini-4-hydrogen-xhigh-intelligence-performance-price-analysis-38ea2af2]]"
last_updated: 2026-11-13
last_verified: 2026-11-13
freshness_window_days: 14
input_cost_per_mtoken: 1.50
output_cost_per_mtoken: 7.50
cost_source: "[[introducing-gemini-4-hydrogen-for-agentic-workflows-d7c21c50]]"
aa_intelligence_index: 51
aa_intelligence_index_source: "[[gemini-4-hydrogen-xhigh-intelligence-performance-price-analysis-38ea2af2]]"
gdpval_aa_elo: null
gdpval_aa_elo_source: null
swe_bench_verified: null
swe_bench_verified_source: null
cybergym: null
cybergym_source: null
arc_agi_2: null
arc_agi_2_source: null
---

# Gemini 4 Hydrogen

## Summary

**Gemini 4 Hydrogen** is Google DeepMind's fast, low-cost agentic tier of the Gemini 4 family, released 2026-11-12, and the **successor to Gemini 3.8 Flash** in Google's model fleet [[introducing-gemini-4-hydrogen-for-agentic-workflows-d7c21c50]]. It is priced at **$1.50 per million input tokens and $7.50 per million output tokens**, with a **1M-token context window**, and supports four thinking effort levels: low, medium, high (default), and xhigh (new as of this release) [[introducing-gemini-4-hydrogen-for-agentic-workflows-d7c21c50]].

> Gemini 4 Hydrogen was released November 12, 2026. The most intelligent model available on Google is Gemini 4 Carbon (high) with an Intelligence Index score of 60. [[gemini-4-hydrogen-xhigh-intelligence-performance-price-analysis-38ea2af2]]

On the **Artificial Analysis Intelligence Index v5**, Hydrogen scores **51 at high (default)** — the value stored in `aa_intelligence_index` — with effort-level scores: **low 27 / medium 41 / high 51 / xhigh 54** [[gemini-4-hydrogen-xhigh-intelligence-performance-price-analysis-38ea2af2]]. At high effort the per-task cost is approximately $1.87; at medium ~$0.80; at low ~$0.29 [[gemini-4-hydrogen-xhigh-intelligence-performance-price-analysis-38ea2af2]].

> Gemini 4 Hydrogen effort levels score 54 (xhigh), 51 (high), 41 (medium), and 27 (low) on the Artificial Analysis Intelligence Index; the high variant costs about $1.87 per task, medium $0.80, and low $0.29. [[gemini-4-hydrogen-xhigh-intelligence-performance-price-analysis-38ea2af2]]

The model card notes that Gemini 4 Hydrogen "did not show a material capability increase over Gemini 4 Argon," positioning it as an efficiency-optimized sibling rather than a capability upgrade [[gemini-4-hydrogen-model-card-google-deepmind-441ce58c]]. Available via Gemini API, Google AI Studio, and Android Studio [[introducing-gemini-4-hydrogen-for-agentic-workflows-d7c21c50]].

> Gemini 4 Hydrogen is a fast, low-cost tier of the Gemini 4 family, built for agentic workflows. [[introducing-gemini-4-hydrogen-for-agentic-workflows-d7c21c50]]

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-11-13)_

## Open questions

- [ ] GDPval-AA Elo, SWE-Bench Verified, CyberGym, ARC-AGI-2 scores — not in ingested sources.
- [ ] Exact architecture details (parameter count, MoE vs dense) — not stated in ingested sources.
- [ ] Cached input pricing — not stated in ingested sources.

## See also

- [[frontier-models]]
- [[gemini-4-argon]]
- [[gemini-4-carbon]]
- [[benchmark-leaders]]
- [[cost-comparison]]
