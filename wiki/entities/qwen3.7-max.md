---
title: "Qwen3.7 Max"
kind: entity
sources: ["[[qwen3-max-thinking-benchmarks-and-analysis-26760cd0]]", "[[qwen3-7-max-intelligence-performance-price-analysis-61bdb800]]", "[[qwen3-7-plus-intelligence-performance-price-analysis-ce790755]]", "[[qwen3-8-max-intelligence-performance-price-analysis-0ad85146]]"]
last_updated: "2026-08-04"
last_verified: "2026-05-26"
freshness_window_days: 30
input_cost_per_mtoken: 2.50
output_cost_per_mtoken: 7.50
cost_source: "[[qwen3-7-max-intelligence-performance-price-analysis-61bdb800]]"
aa_intelligence_index: 57
aa_intelligence_index_source: "[[qwen3-7-max-intelligence-performance-price-analysis-61bdb800]]"
gdpval_aa_elo: null
gdpval_aa_elo_source: null
swe_bench_verified: null
swe_bench_verified_source: null
cybergym: null
cybergym_source: null
arc_agi_2: null
arc_agi_2_source: null
---

## Summary

Qwen3.7 Max is Alibaba's frontier open-weights model. It scored 57 on the Artificial Analysis Intelligence Index on its May 19, 2026 release, becoming the current open-weights leader [[qwen3-max-thinking-benchmarks-and-analysis-26760cd0]].

> Qwen3.7 Max scored 57 on the AA Intelligence Index at its May 19, 2026 release.

Stub entity page seeded for `[frontier_models].roster` resolution. The daily `topic-researcher` roster sweep populates remaining benchmark frontmatter as it confirms values against current sources.

Benchmark and pricing detail confirmed 2026-05-26: Qwen3.7 Max is a **closed-weights, API-only** model (not open-weights) [[qwen3-7-max-intelligence-performance-price-analysis-61bdb800]]. On Alibaba Cloud DashScope it is priced at $2.50 input / $7.50 output per Mtoken. It scores 92.4 on GPQA Diamond (ahead of Claude Opus 4.6 Max 91.3, behind GPT-5.5 93.6), 60.6 on SWE-Pro, and 69.7 on Terminal-Bench 2.0, putting it ahead of DeepSeek V4-Pro and Claude Opus 4.6 on agentic coding [[qwen3-7-max-intelligence-performance-price-analysis-61bdb800]].

**Superseded 2026-08-04**: Alibaba shipped **Qwen3.8 Max** as its new flagship, scoring **53 on AA Intelligence Index v4.1** (a 2.4T-total / ~95B-active MoE with 1M context and text/image/video input at $2/$6 per Mtoken), superseding Qwen3.7 Max as the per-lab flagship [[qwen3-8-max-intelligence-performance-price-analysis-0ad85146]].

The sibling **Qwen3.7 Plus** multimodal variant (text/image/video input, text output) was placed at **AA Intelligence Index v4.1 = 39** on 2026-06-27, well below Max's 57 (v4.0) — trading reasoning headroom for vision capability [[qwen3-7-plus-intelligence-performance-price-analysis-ce790755]].

> Qwen 3.7 Max and Qwen 3.7 Plus are both closed-weights, API-only. On Alibaba Cloud DashScope pricing is $2.50 per million input tokens and $7.50 per million output tokens.

> Qwen3.7-Max scores 92.4 on GPQA Diamond, 60.6% on SWE-Pro, 69.7 on Terminal-Bench 2.0.

> Qwen3.7 Max scored 57 on the Artificial Analysis Intelligence Index.

> Qwen3.7 Plus achieves a score of 39 on the Artificial Analysis Intelligence Index, which is a composite benchmark that evaluates models across reasoning, knowledge, mathematics, and coding. This score places it well above average among comparable models (averaging 16). Qwen3.7 Plus is multimodal and can process text, image, and video input and generate text output.

## Disputes

- This entity page's earlier description implied Qwen3.7 Max was an open-weights model, but [[qwen3-7-max-intelligence-performance-price-analysis-61bdb800]] confirms Qwen3.7 Max (and Qwen3.7 Plus) are closed-weights, API-only. Status: resolved-toward-B — Qwen3.7 Max is closed-weights.
- [[qwen3-max-thinking-benchmarks-and-analysis-26760cd0]] claims Qwen3.7 Max "scored 57 on the AA Intelligence Index at its May 19, 2026 release, becoming the current open-weights leader"; [[qwen3-7-max-intelligence-performance-price-analysis-61bdb800]] confirms Qwen3.7 Max is closed-weights, API-only, not open-weights. Status: unresolved (confidence: high; sweep: 2026-07-05) — the "open-weights leader" claim is factually incorrect; Qwen3.7 Max is a closed-weights model and therefore not a candidate for open-weights leadership.

## Open questions

- [ ] GDPval-AA Elo, SWE-bench Verified, Cybench, ARC-AGI-2 for Qwen3.7 Max — pending researcher sweep.

## See also

- [[frontier-models]]
- [[glm-5]]
- [[kimi-k2.6]]
