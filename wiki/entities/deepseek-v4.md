---
title: "DeepSeek V4"
kind: entity
sources: ["[[deepseek-v4-pro-on-hugging-face-a0d5aaf3]]", "[[swe-cycle-benchmarking-code-agents-across-the-complete-issue-resolution-cycle-3256d47f]]", "[[glm-5-everything-you-need-to-know-a53ff5c1]]", "[[deepseek-api-models-and-pricing-8eb12065]]", "[[deepseek-v4-pro-intelligence-and-performance-analysis-artificial-analysis-36762786]]"]
last_updated: "2026-05-22"
last_verified: "2026-05-22"
freshness_window_days: 30
input_cost_per_mtoken: 1.74
output_cost_per_mtoken: 3.48
cost_source: "[[deepseek-api-models-and-pricing-8eb12065]]"
aa_intelligence_index: 52
aa_intelligence_index_source: "[[deepseek-v4-pro-intelligence-and-performance-analysis-artificial-analysis-36762786]]"
gdpval_aa_elo: null
gdpval_aa_elo_source: null
swe_bench_verified: 0.806
swe_bench_verified_source: "[[deepseek-v4-pro-on-hugging-face-a0d5aaf3]]"
cybergym: null
cybergym_source: null
arc_agi_2: null
arc_agi_2_source: null
---

## Summary

DeepSeek V4 was released April 24, 2026 as two models: V4-Pro (1.6T parameter MoE, 49B activated per token) and V4-Flash (284B MoE, 13B activated), both with 1M-token context and both released under the MIT license [[deepseek-v4-pro-on-hugging-face-a0d5aaf3]]. V4-Pro-Max scores 80.6% on SWE-bench Verified and 3,206 Codeforces — surpassing GPT-5.4's 3,168.

> The model weights are licensed under the MIT License. V4-Pro's Codeforces rating of 3,206 surpasses GPT-5.4's 3,168.

DeepSeek V4-Pro list pricing is $1.74 per million input tokens (cache miss) and $3.48 per million output tokens [[deepseek-api-models-and-pricing-8eb12065]]. A 75% promotional discount runs through 2026-05-31 16:00 UTC, bringing effective rates to $0.435/$0.87 per million tokens during the promo window — among the cheapest frontier-tier rates available.

> 1M INPUT TOKENS (CACHE MISS) ... $1.74 ... 1M OUTPUT TOKENS ... $3.48.

DeepSeek V4-Pro (Reasoning, Max Effort) scores 52 on the [[deepseek-v4-pro-intelligence-and-performance-analysis-artificial-analysis-36762786]] Artificial Analysis Intelligence Index v4.0 — placing it as the #2 open-weights reasoning model behind Kimi K2.6 (54) and ahead of GLM-5 (50). AA flags V4-Pro as exceptionally verbose: it generated 190M tokens to evaluate the Intelligence Index, vs. an average of 42M for comparable models — a real cost consideration even at V4-Pro's promotional pricing.

> DeepSeek V4 Pro (Reasoning, Max Effort) scores 52 on the Artificial Analysis Intelligence Index ... When evaluating the Intelligence Index, it generated 190M tokens, which is very verbose in comparison to the average of 42M.

## Disputes

- [[deepseek-v4-pro-on-hugging-face-a0d5aaf3]] claims V4-Pro-Max's 80.6% SWE-bench Verified is a frontier-leading score, but OpenAI has stopped reporting SWE-bench Verified after finding contamination across all frontier models. On SWE-bench Pro (the contamination-controlled successor) DeepSeek V4-Pro's ranking is not yet published. Status: unresolved.
- [[swe-cycle-benchmarking-code-agents-across-the-complete-issue-resolution-cycle-3256d47f]] claims that even on isolated tasks, traditional deterministic pass/fail script evaluation (the methodology behind SWE-bench Verified) "produces severe misjudgments and false signals" and proposes SWE-Judge (LLM-based, human-validated) as a corrective — raising the question of whether V4-Pro-Max's 80.6% SWE-bench Verified score [[deepseek-v4-pro-on-hugging-face-a0d5aaf3]] is reliably measuring what it claims to measure. Status: unresolved.

## Open questions

- [ ] Has DeepSeek R2 (the reasoning-model sibling to V4) actually been released as of 2026-05-20?
- [ ] What is DeepSeek V4-Pro's SWE-bench Pro score?
- [ ] Does DeepSeek V4 include DeepSeek Sparse Attention (now documented in GLM-5 [[glm-5-everything-you-need-to-know-a53ff5c1]]), or is that a technique Z.AI integrated independently?

## See also

- [[frontier-models]]
- [[claude-opus-4.7]]
- [[gpt-5.5]]
- [[glm-5]]
