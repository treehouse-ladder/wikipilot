---
title: "DeepSeek V4"
kind: entity
sources: ["[[deepseek-v4-pro-on-hugging-face-a0d5aaf3]]", "[[swe-cycle-benchmarking-code-agents-across-the-complete-issue-resolution-cycle-3256d47f]]", "[[glm-5-everything-you-need-to-know-a53ff5c1]]", "[[deepseek-api-models-and-pricing-8eb12065]]", "[[deepseek-v4-pro-intelligence-and-performance-analysis-artificial-analysis-36762786]]", "[[deepseek-r2-explained-92-7-aime-32b-open-weight-d990eab3]]", "[[glm-5-1-intelligence-performance-price-analysis-fb6f086c]]", "[[deepseek-is-back-among-the-leading-open-weights-models-with-v4-pro-and-v4-flash-d16dda28]]", "[[itbench-aa-frontier-models-score-below-50-on-the-first-benchmark-for-agentic-enterprise-it-tasks-c6a7b34a]]", "[[deepseek-v4-flash-0731-scores-50-on-the-artificial-analysis-intelligence-index-10-points-above-previous-deepseek-v4-flash-108621d0]]", "[[deepseek-upgrades-deepseek-v4-flash-0731-with-major-agentic-and-coding-gains-159beea4]]", "[[deepseek-ai-deepseek-v4-flash-0731-a1a747f4]]", "[[deepseek-v4-pro-ga-release-fe54be56]]"]
last_updated: 2026-08-14
last_verified: 2026-08-14
freshness_window_days: 30
input_cost_per_mtoken: 1.74
output_cost_per_mtoken: 3.48
cost_source: "[[deepseek-api-models-and-pricing-8eb12065]]"
aa_intelligence_index: 53
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

DeepSeek's reasoning-model sibling, DeepSeek R2, shipped in April 2026 as a 32B dense transformer under the MIT license — answering the long-standing open question of whether R2 had released [[deepseek-r2-explained-92-7-aime-32b-open-weight-d990eab3]]. Unlike V4-Pro's 1.6T MoE, R2 is small enough to fit on a single 24GB consumer GPU (RTX 4090 / A6000), scores 92.7% on AIME 2025, and undercuts Western frontier reasoning APIs by ~70% on token cost [[deepseek-r2-explained-92-7-aime-32b-open-weight-d990eab3]].

> Where R1 (January 2025) was a 671-billion-parameter Mixture-of-Experts behemoth, R2 ships as a 32B dense transformer released under MIT license, small enough to fit on a single RTX 4090 or A6000.

> DeepSeek R2 ... scores 92.7% on AIME 2025 ... and undercuts Western frontier reasoning APIs by roughly 70% on token cost.

Artificial Analysis published a dedicated launch analysis confirming the V4 family positioning [[deepseek-is-back-among-the-leading-open-weights-models-with-v4-pro-and-v4-flash-d16dda28]]: DeepSeek V4 Pro (Reasoning, Max Effort) sits at #2 among open-weights reasoning models at AA Intelligence Index 52, behind Kimi K2.6 (54); DeepSeek V4 Flash (Reasoning, Max Effort) lands at 47 on the same axis. Both models are hybrid thinking/non-thinking. The three-way open-weights top of the leaderboard now reads Kimi K2.6 (54), MiMo-V2.5-Pro (54), DeepSeek V4 Pro (52). On ITBench-AA SRE — the new agentic enterprise IT benchmark — DeepSeek V4 Pro (Reasoning, Max Effort) scores 38%, the #2 open-weights position behind GLM-5.1 (40%) [[itbench-aa-frontier-models-score-below-50-on-the-first-benchmark-for-agentic-enterprise-it-tasks-c6a7b34a]].

> The top open weights models on Artificial Analysis are: 1. Kimi K2.6 (54), 2. MiMo-V2.5-Pro (54), 3. DeepSeek V4 Pro (Reasoning, Max Effort) (52).

> GLM-5.1 (Reasoning) leads open weights models at 40%, with DeepSeek V4 Pro (Reasoning, Max Effort) at 38%, and Gemma 4 31B (Reasoning) at 37%.

**DeepSeek-V4-Flash-0731 (official release, July 31, 2026)** supersedes the preview and achieves a major agentic performance leap via re-post-training on the same architecture [[deepseek-ai-deepseek-v4-flash-0731-a1a747f4]]. Terminal-Bench 2.1 jumps from 61.8 (preview) to **82.7** and DeepSWE from 7.3 to **54.4**, while the AA Intelligence Index moves from 40 to **50** — 10 points, placing it above the prior open-weights cluster (GLM-5.2 = 51 is close; Kimi K3 = 57 remains well ahead) [[deepseek-v4-flash-0731-scores-50-on-the-artificial-analysis-intelligence-index-10-points-above-previous-deepseek-v4-flash-108621d0]]. The V4-Flash-0731 pricing is **$0.14/MTok cache-miss input, $0.0028/MTok cache-hit input, $0.28/MTok output**; the cache-hit pricing makes it exceptionally cheap for agentic loops with shared system prompts [[deepseek-upgrades-deepseek-v4-flash-0731-with-major-agentic-and-coding-gains-159beea4]]. MIT-licensed, ungated, ships with the DSpark speculative decoding module.

> DeepSeek-V4-Flash-0731 is the official release of DeepSeek-V4-Flash, superseding the preview version, with substantially enhanced agentic capabilities. DeepSeek-V4-Flash-0731 outperforms DeepSeek-V4-Pro (Preview) on benchmarks listed below despite its far smaller activated parameter count, and is broadly competitive with the strongest proprietary models available. [[deepseek-ai-deepseek-v4-flash-0731-a1a747f4]]

> DeepSeek V4 Flash 0731 scores 50 on the Artificial Analysis Intelligence Index, 10 points above the previous DeepSeek V4 Flash. DeepSeek-V4-Flash-0731 outperforms DeepSeek-V4-Pro (Preview) on the published benchmarks despite its far smaller activated parameter count. [[deepseek-v4-flash-0731-scores-50-on-the-artificial-analysis-intelligence-index-10-points-above-previous-deepseek-v4-flash-108621d0]]

DeepSeek shipped the GA build **DeepSeek-V4-Pro-0813** on 2026-08-13, superseding the April preview [[deepseek-v4-pro-ga-release-fe54be56]]. It is a **1.57T-total / 48B-active MoE** built on the V4-Pro preview structure with a **DSpark speculative-decoding module** attached; the GA build "greatly enhances agent capabilities" especially in production, and V4-Pro/V4-Flash thinking now expose three effort levels (low/high/max) [[deepseek-v4-pro-ga-release-fe54be56]]. Artificial Analysis re-places the 0813 build at **53 on the Intelligence Index v4.1.1** (up from the preview's 52 on v4.0) [[deepseek-v4-pro-intelligence-and-performance-analysis-artificial-analysis-36762786]]. New API pricing takes effect 16:00 UTC 2026-08-16; the specific rates were not published in the GA note, so the current cost fields are pending re-verification [[deepseek-v4-pro-ga-release-fe54be56]].

> Compared with the preview version, the GA version greatly enhances agent capabilities, with particularly significant performance improvements in production environments. [[deepseek-v4-pro-ga-release-fe54be56]]

## Disputes

- [[deepseek-v4-pro-on-hugging-face-a0d5aaf3]] claims V4-Pro-Max's 80.6% SWE-bench Verified is a frontier-leading score, but OpenAI has stopped reporting SWE-bench Verified after finding contamination across all frontier models. On SWE-bench Pro (the contamination-controlled successor) DeepSeek V4-Pro's ranking is not yet published. Status: unresolved.
- [[swe-cycle-benchmarking-code-agents-across-the-complete-issue-resolution-cycle-3256d47f]] claims that even on isolated tasks, traditional deterministic pass/fail script evaluation (the methodology behind SWE-bench Verified) "produces severe misjudgments and false signals" and proposes SWE-Judge (LLM-based, human-validated) as a corrective — raising the question of whether V4-Pro-Max's 80.6% SWE-bench Verified score [[deepseek-v4-pro-on-hugging-face-a0d5aaf3]] is reliably measuring what it claims to measure. Status: unresolved.
- [[deepseek-is-back-among-the-leading-open-weights-models-with-v4-pro-and-v4-flash-d16dda28]] places DeepSeek V4 Pro (Reasoning, Max Effort) at AA Intelligence Index score 52 (May 2026, v4.0); [[glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index-ef3ea3a0]] reports DeepSeek V4 Pro (max) at 44 on AA Intelligence Index v4.1 (the June 2026 agentic-reweighted version). The frontmatter records `aa_intelligence_index: 52` without specifying which index version it reflects. Status: unresolved — the two scores reflect different index versions (v4.0 vs v4.1); the frontmatter should clarify which version it tracks (confidence: high; sweep: 2026-07-12).

## Open questions

- [ ] What is the 0813 build's contamination-resistant coding (SWE-bench Pro) placement, and is the 52→53 move capability or index-version (v4.0→v4.1.1) artifact? [[deepseek-v4-pro-ga-release-fe54be56]]
- [ ] DeepSeek's new API pricing effective 2026-08-16 16:00 UTC — per-Mtoken rates unpublished in the GA note; cost fields may move. [[deepseek-v4-pro-ga-release-fe54be56]]
- [ ] Now that DeepSeek R2 has shipped as a 32B dense model [[deepseek-r2-explained-92-7-aime-32b-open-weight-d990eab3]], does it share V4's architecture lineage or DeepSeek Sparse Attention, and where does it land on the AA Intelligence Index relative to V4-Pro?
- [ ] What is DeepSeek V4-Pro's SWE-bench Pro score?
- [ ] Does DeepSeek V4 include DeepSeek Sparse Attention (now documented in GLM-5 [[glm-5-everything-you-need-to-know-a53ff5c1]]), or is that a technique Z.AI integrated independently?
- [ ] GLM-5.1 now ranks #2 on GDPval-AA among open-weights models (1535 Elo) per [[glm-5-1-intelligence-performance-price-analysis-fb6f086c]], implying DeepSeek V4-Pro leads at #1 — what is V4-Pro's actual GDPval-AA Elo score, and does it hold the open-weights #1 spot consistently across the April-May 2026 time window?
- [ ] On ITBench-AA SRE, DeepSeek V4 Pro at 38% is behind GLM-5.1 at 40% [[itbench-aa-frontier-models-score-below-50-on-the-first-benchmark-for-agentic-enterprise-it-tasks-c6a7b34a]] — is this a methodology-driven inversion (K8s-incident-RCA-specific) or does GLM-5.1 genuinely outpace V4 Pro on long-horizon agentic infrastructure tasks?
- [ ] V4-Flash-0731's DeepSWE score (54.4) is compared to Kimi K3's 67.4 in the same source's comparison set — does this gap reflect a meaningful capability difference, or do the two benchmark runs use different harnesses? [[deepseek-upgrades-deepseek-v4-flash-0731-with-major-agentic-and-coding-gains-159beea4]]

## See also

- [[frontier-models]]
- [[claude-opus-4.7]]
- [[gpt-5.5]]
- [[glm-5]]
