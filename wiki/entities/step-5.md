---
title: "Step 5 Preview"
kind: entity
aliases: ["StepFun Step 5", "Step5 Preview", "step-5-preview"]
sources: ["[[stepfun-launches-step-5-preview-600b-sparse-moe-1m-context-weights-open-oct-15-3397b6e7]]", "[[stepfun-launches-step-5-preview-a-600b-total-27b-active-moe-model-with-1m-context-for-long-horizon-agentic-work-f4fd772d]]"]
last_updated: 2026-09-22
last_verified: 2026-09-22
freshness_window_days: 30
input_cost_per_mtoken: 1.00
output_cost_per_mtoken: 2.70
cost_source: "[[stepfun-launches-step-5-preview-600b-sparse-moe-1m-context-weights-open-oct-15-3397b6e7]]"
aa_intelligence_index: 44
aa_intelligence_index_source: "[[stepfun-launches-step-5-preview-600b-sparse-moe-1m-context-weights-open-oct-15-3397b6e7]]"
gdpval_aa_elo: null
gdpval_aa_elo_source: null
swe_bench_verified: null
swe_bench_verified_source: null
cybergym: null
cybergym_source: null
arc_agi_2: null
arc_agi_2_source: null
---

# Step 5 Preview

## Summary

Step 5 Preview is StepFun's latest frontier model, launched 2026-09-20, a **600B-parameter sparse Mixture-of-Experts** model with **27B active parameters** (4.5% active-to-total ratio) and a **1M-token context window** supporting text, image, and video inputs [[stepfun-launches-step-5-preview-600b-sparse-moe-1m-context-weights-open-oct-15-3397b6e7]]. On the **Artificial Analysis Intelligence Index**, it scores approximately **44**, placing it among the top open-weight models [[stepfun-launches-step-5-preview-600b-sparse-moe-1m-context-weights-open-oct-15-3397b6e7]]. On **DeepSWE v1.1** (High reasoning), it scores **67.7%** — above Kimi K3 Max (67.5%) and GLM-5.3 Max (66.9%), but below GPT-6 Astra Max (74.1%) and Claude Opus 5 Max (74.0%) [[stepfun-launches-step-5-preview-a-600b-total-27b-active-moe-model-with-1m-context-for-long-horizon-agentic-work-f4fd772d]]. On **StepCodeBench**, it scores **49.0% avg@4**, with particular strength in bug repair, feature modification, and refactoring [[stepfun-launches-step-5-preview-a-600b-total-27b-active-moe-model-with-1m-context-for-long-horizon-agentic-work-f4fd772d]]. Architecture uses a **92-layer narrow-deep Transformer** layout with **Sparse GQA** and block-wise token merging for 1M-context efficiency [[stepfun-launches-step-5-preview-a-600b-total-27b-active-moe-model-with-1m-context-for-long-horizon-agentic-work-f4fd772d]]. API is live now at **$1.00/$2.70 per Mtoken** ($0.05 on cache hit); **model weights open October 15** [[stepfun-launches-step-5-preview-600b-sparse-moe-1m-context-weights-open-oct-15-3397b6e7]].

> Step 5 Preview is a 600B-parameter sparse Mixture-of-Experts model with 27B active parameters, a 1M-token context window, and native support for text, image, and video inputs. [[stepfun-launches-step-5-preview-600b-sparse-moe-1m-context-weights-open-oct-15-3397b6e7]]

> StepFun reports a 67.7 score for Step 5 Preview at High reasoning on DeepSWE v1.1, compared to Kimi K3 Max at 67.5, GLM-5.3 Max at 66.9, GPT-6 Astra Max at 74.1 and Claude Opus 5 Max at 74.0. [[stepfun-launches-step-5-preview-a-600b-total-27b-active-moe-model-with-1m-context-for-long-horizon-agentic-work-f4fd772d]]

> On Artificial Analysis, Step 5 Preview scores about 44 on the intelligence index, which StepFun positions among the top open-weight models in that ranking. [[stepfun-launches-step-5-preview-600b-sparse-moe-1m-context-weights-open-oct-15-3397b6e7]]

## Disputes

_none_

## Open questions

- [ ] Full AA Intelligence Index placement (AA-Briefcase, Terminal-Bench, GDPval-AA Elo) not yet reported.
- [ ] Weights open Oct 15 — confirm at that date whether the release happens as announced.

## See also

- [[frontier-models]]
- [[kimi-k3]]
- [[claude-opus-5]]
- [[gpt-6-astra]]
- [[benchmark-leaders]]
- [[cost-comparison]]
