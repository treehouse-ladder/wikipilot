---
title: "GLM-5"
kind: entity
sources: ["[[glm-5-everything-you-need-to-know-a53ff5c1]]", "[[z-ai-developer-document-pricing-667e8002]]"]
last_updated: "2026-05-22"
last_verified: "2026-05-22"
freshness_window_days: 30
input_cost_per_mtoken: 1.00
output_cost_per_mtoken: 3.20
cost_source: "[[z-ai-developer-document-pricing-667e8002]]"
aa_intelligence_index: 50
aa_intelligence_index_source: "[[glm-5-everything-you-need-to-know-a53ff5c1]]"
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

GLM-5 is Z.AI's frontier open-weights model released on February 11, 2026 [[glm-5-everything-you-need-to-know-a53ff5c1]]. It scores 50 on the Artificial Analysis Intelligence Index, up 8 points from GLM-4.7's 42, and was the leading open-weights model at the time of its February release (later overtaken by Moonshot's Kimi K2.6 at 54 in April and Qwen3.7 Max at 57 in May). GLM-5 is Z.AI's first new architecture since GLM-4.5, scaling to 744B total parameters with 40B active parameters in a mixture-of-experts (MoE) configuration. It is the first model documented to integrate DeepSeek Sparse Attention.

GLM-5 achieves the highest Artificial Analysis Agentic Index score among open-weights models with a score of 63, ranking third overall, driven by strong performance in GDPval-AA [[glm-5-everything-you-need-to-know-a53ff5c1]]. The model has a context window of 200K tokens and supports text input and output only. GLM-5 is released under the MIT license, which allows commercial use.

> GLM-5 is the new leading open weights model, leading the Artificial Analysis Intelligence Index amongst open weights models.

> GLM-5 is Z.AI's first new architecture since GLM-4.5, scaling to 744B total / 40B active parameters, and integrates DeepSeek Sparse Attention.

> GLM-5 achieves the highest Artificial Analysis Agentic Index score among open weights models with a score of 63, ranking third overall, driven by strong performance in GDPval-AA.

Z.AI's hosted GLM-5 API is priced at $1.00 per million input tokens and $3.20 per million output tokens; cached input drops to $0.20/M, with cached input storage free for a limited time [[z-ai-developer-document-pricing-667e8002]].

> GLM-5 ... Input $1 ... Cached Input $0.2 ... Output $3.2.

## Disputes

- [[glm-5-everything-you-need-to-know-a53ff5c1]] claims GLM-5 (AA Index 50, released Feb 11 2026) is the leading open-weights model, but [[kimi-k26-the-new-leading-open-weights-model-0bea9ccd]] and [[qwen3-max-thinking-benchmarks-and-analysis-26760cd0]] report later open-weights leaders: Moonshot's Kimi K2.6 at AA Index 54 (released Apr 20) and Qwen3.7 Max at 57 (released May 19). Status: resolved-toward-B — GLM-5 was the open-weights leader at its February release but has since been overtaken; the 'new leading open weights model' framing is time-bound to early 2026.

## Open questions

- [ ] How much of GLM-5's agentic-index lead (63) among open-weights models is attributable to DeepSeek Sparse Attention vs. its 28.5T-token pretraining scale-up?
- [ ] Does the sparse-attention integration measurably help long-horizon agentic loops?
- [ ] What is GLM-5's performance on contamination-resistant benchmarks like SWE-bench Pro?

## See also

- [[frontier-models]]
- [[deepseek-v4]]
- [[claude-opus-4.7]]
