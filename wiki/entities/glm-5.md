---
title: "GLM-5"
kind: entity
sources: ["[[glm-5-everything-you-need-to-know-a53ff5c1]]", "[[z-ai-developer-document-pricing-667e8002]]", "[[z-ai-introduces-glm-5-1-an-open-weight-754b-agentic-model-that-achieves-sota-on-swe-bench-pro-and-sustains-8-hour-autonomous-execution-27ebed2a]]", "[[mimo-v2-5-pro-intelligence-performance-price-analysis-51e3baae]]", "[[qwen3-7-max-intelligence-performance-price-analysis-61bdb800]]"]
last_updated: 2026-05-26
last_verified: 2026-05-25
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

GLM-5 is Z.AI's frontier open-weights model released on February 11, 2026 [[glm-5-everything-you-need-to-know-a53ff5c1]]. It scores 50 on the Artificial Analysis Intelligence Index, up 8 points from GLM-4.7's 42, and was the leading open-weights model at the time of its February release (later overtaken by Moonshot's Kimi K2.6 at 54 in April and co-leaders Kimi K2.6 / Xiaomi MiMo-V2.5-Pro at 54 in May; Qwen3.7 Max scores 57 but is closed-weights API-only). GLM-5 is Z.AI's first new architecture since GLM-4.5, scaling to 744B total parameters with 40B active parameters in a mixture-of-experts (MoE) configuration. It is the first model documented to integrate DeepSeek Sparse Attention.

GLM-5 achieves the highest Artificial Analysis Agentic Index score among open-weights models with a score of 63, ranking third overall, driven by strong performance in GDPval-AA [[glm-5-everything-you-need-to-know-a53ff5c1]]. The model has a context window of 200K tokens and supports text input and output only. GLM-5 is released under the MIT license, which allows commercial use.

> GLM-5 is the new leading open weights model, leading the Artificial Analysis Intelligence Index amongst open weights models.

> GLM-5 is Z.AI's first new architecture since GLM-4.5, scaling to 744B total / 40B active parameters, and integrates DeepSeek Sparse Attention.

> GLM-5 achieves the highest Artificial Analysis Agentic Index score among open weights models with a score of 63, ranking third overall, driven by strong performance in GDPval-AA.

Z.AI's hosted GLM-5 API is priced at $1.00 per million input tokens and $3.20 per million output tokens; cached input drops to $0.20/M, with cached input storage free for a limited time [[z-ai-developer-document-pricing-667e8002]].

> GLM-5 ... Input $1 ... Cached Input $0.2 ... Output $3.2.

Z.AI released GLM-5.1 as the successor to GLM-5 in April 2026, a 754B-parameter MoE + DSA model trained with asynchronous reinforcement learning, designed explicitly for long-horizon autonomous agentic execution [[z-ai-introduces-glm-5-1-an-open-weight-754b-agentic-model-that-achieves-sota-on-swe-bench-pro-and-sustains-8-hour-autonomous-execution-27ebed2a]]. GLM-5.1 is released under the MIT license with a 200K context window and 128K max output tokens. The headline claim is a vendor-reported state-of-the-art score of 58.4 on SWE-Bench Pro, ahead of GPT-5.4, Claude Opus 4.6, and Gemini 3.1 Pro (pending independent verification), and is engineered to sustain a single complex task for up to 8 hours across hundreds of rounds and thousands of tool calls without human intervention [[z-ai-introduces-glm-5-1-an-open-weight-754b-agentic-model-that-achieves-sota-on-swe-bench-pro-and-sustains-8-hour-autonomous-execution-27ebed2a]].

> GLM-5.1 sets a new state-of-the-art on SWE-Bench Pro with a score of 58.4, outperforming GPT-5.4, Claude Opus 4.6, and Gemini 3.1 Pro, making it one of the strongest publicly benchmarked models for software engineering tasks.

> The model is built for long-horizon autonomous execution, capable of working on a single complex task for up to 8 hours — running experiments, revising strategies, and iterating across hundreds of rounds and thousands of tool calls without human intervention.

## Disputes

- [[glm-5-everything-you-need-to-know-a53ff5c1]] claims GLM-5 (AA Index 50, released Feb 11 2026) is the leading open-weights model, but [[kimi-k26-the-new-leading-open-weights-model-0bea9ccd]] reports a later open-weights leader: Moonshot's Kimi K2.6 at AA Index 54 (released Apr 20), co-tied with Xiaomi's MiMo-V2.5-Pro at 54 (released Apr 22) [[mimo-v2-5-pro-intelligence-performance-price-analysis-51e3baae]]. Qwen3.7 Max scores 57 but is closed-weights API-only [[qwen3-7-max-intelligence-performance-price-analysis-61bdb800]]. Status: resolved-toward-B — GLM-5 was the open-weights leader at its February release but has since been overtaken by the Kimi K2.6 / MiMo-V2.5-Pro co-leadership at 54; the 'new leading open weights model' framing is time-bound to early 2026.

## Open questions

- [ ] How much of GLM-5's agentic-index lead (63) among open-weights models is attributable to DeepSeek Sparse Attention vs. its 28.5T-token pretraining scale-up?
- [ ] Does the sparse-attention integration measurably help long-horizon agentic loops?
- [ ] What is GLM-5's performance on contamination-resistant benchmarks like SWE-bench Pro?
- [ ] What is GLM-5.1's hosted API pricing, and does it maintain GLM-5's $1.00/$3.20 pricing or shift to reflect the 754B parameter scale-up [[z-ai-introduces-glm-5-1-an-open-weight-754b-agentic-model-that-achieves-sota-on-swe-bench-pro-and-sustains-8-hour-autonomous-execution-27ebed2a]]?
- [ ] Does GLM-5.1's 8-hour autonomous-execution claim translate into measurably higher completion rates on long-horizon benchmarks like SWE-Chain or Terminal-Bench compared to GLM-5 [[z-ai-introduces-glm-5-1-an-open-weight-754b-agentic-model-that-achieves-sota-on-swe-bench-pro-and-sustains-8-hour-autonomous-execution-27ebed2a]]?

## See also

- [[frontier-models]]
- [[deepseek-v4]]
- [[claude-opus-4.7]]
