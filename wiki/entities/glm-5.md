---
title: "GLM-5"
kind: entity
sources: ["[[glm-5-everything-you-need-to-know-a53ff5c1]]", "[[z-ai-developer-document-pricing-667e8002]]", "[[z-ai-introduces-glm-5-1-an-open-weight-754b-agentic-model-that-achieves-sota-on-swe-bench-pro-and-sustains-8-hour-autonomous-execution-27ebed2a]]", "[[mimo-v2-5-pro-intelligence-performance-price-analysis-51e3baae]]", "[[qwen3-7-max-intelligence-performance-price-analysis-61bdb800]]", "[[glm-5-1-intelligence-performance-price-analysis-fb6f086c]]", "[[glm-5-from-vibe-coding-to-agentic-engineering-43553238]]", "[[zhipu-ai-open-sources-glm-5-2-with-1-million-token-context-cbc95c1c]]", "[[artificial-analysis-intelligence-index-v4-1-a-shift-toward-agentic-workloads-e0bce552]]", "[[glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index-ef3ea3a0]]", "[[glm-5-2-built-for-long-horizon-tasks-9e3636b0]]", "[[glm-5-3-overview-7e6c3dd9]]", "[[z-ai-delays-glm-5-3-weights-after-cybergym-score-tops-mythos-bca697d6]]", "[[glm-5-3-max-intelligence-performance-price-analysis-26ed0788]]", "[[glm-5-3-flash-intelligence-performance-price-analysis-b02205ef]]"]
last_updated: 2026-08-27
last_verified: 2026-08-20
freshness_window_days: 30
input_cost_per_mtoken: 1.40
output_cost_per_mtoken: 4.40
cost_source: "[[glm-5-3-max-intelligence-performance-price-analysis-26ed0788]]"
aa_intelligence_index: 60
aa_intelligence_index_source: "[[glm-5-3-max-intelligence-performance-price-analysis-26ed0788]]"
gdpval_aa_elo: 1524
gdpval_aa_elo_source: "[[glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index-ef3ea3a0]]"
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

GLM-5.1's vendor SWE-Bench Pro SOTA claim now has an independent counterpoint: on artificialanalysis.ai, GLM-5.1 (Reasoning) scores 51 on the AA Intelligence Index — the first open-weights model to cross 50 on v4.0 — ranks #2 among open weights on GDPval-AA (1535 Elo, behind DeepSeek V4-Pro), and edges Kimi K2.6 on Code Arena WebDev (1534 vs 1529), priced at $1.40/$4.40 per Mtoken [[glm-5-1-intelligence-performance-price-analysis-fb6f086c]]. The independent aggregate score (51) confirms GLM-5.1 as a leading open-weights agentic model but sits well below the closed-frontier leaders (GPT-5.5 at 60), so the vendor's 'beats GPT-5.4 / Opus 4.6 / Gemini 3.1 Pro' framing is a coding-axis (SWE-Bench Pro) claim, not an aggregate-leaderboard one.

> GLM-5.1 (Reasoning) achieves a score of 51 on the Artificial Analysis Intelligence Index ... This score places it well above average among comparable models (averaging 30).

The GLM-5 line now also has a primary technical report (arXiv 2602.15763), which frames GLM-5 as a transition from 'vibe coding' to 'agentic engineering' on ARC capabilities, confirms DSA (DeepSeek Sparse Attention) as the cost-reduction mechanism, and details a new asynchronous agent-RL infrastructure that decouples generation from training to learn from long-horizon interactions [[glm-5-from-vibe-coding-to-agentic-engineering-43553238]].

> GLM-5 ... adopts DSA to significantly reduce training and inference costs while maintaining long-context fidelity.

Z.AI released **GLM-5.2** on June 13, 2026, the latest model in the GLM-5 line, available immediately on the GLM Coding Plan tiers with the standalone API, Z.ai chatbot, and MIT open weights confirmed for the following week [[zhipu-ai-open-sources-glm-5-2-with-1-million-token-context-cbc95c1c]]. GLM-5.2 retains GLM-5's 744B-total / 40B-active MoE architecture but extends the context window to a usable 1M tokens (vs 200K on GLM-5/5.1) and adds a dual thinking-effort system (High / Max, no Auto/Low tier), with max output capped at 131,072 tokens; Z.AI recommends Max as the coding default [[zhipu-ai-open-sources-glm-5-2-with-1-million-token-context-cbc95c1c]]. The MIT open-weights release carries no regional usage restrictions.

> GLM-5.2 will be released as open-source software under the MIT license, with a 1 million token context window — among the largest available from any open-source LLM — and will carry no regional usage restrictions.

> Maximum output is capped at 131,072 tokens. Zhipu's own guidance is that Max should be the default for coding work.

**GLM-5.2 now holds the open-weights #1 position on AA Intelligence Index v4.1 at 51**, ahead of MiniMax-M3 (44), DeepSeek V4-Pro (44), and Kimi K2.6 (43) [[glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index-ef3ea3a0]]. Note that this is on v4.1 of the AA Intelligence Index, which re-scales scores vs v4.0 (where the GLM-5 line scored 50 for GLM-5 and 51 for GLM-5.1); **v4.0 and v4.1 scores are not directly comparable** due to Artificial Analysis's June 2026 methodology shift toward agentic workloads, upgrading GDPval-AA to v2 and reweighting evaluations [[artificial-analysis-intelligence-index-v4-1-a-shift-toward-agentic-workloads-e0bce552]]. GLM-5.2 scores 11 points higher than GLM-5.1 on the new v4.1 scale, with gains concentrated in scientific reasoning (CritPt +16 to 21%, HLE +12 to 40%), long-context reasoning (AA-LCR +9 to 71%), agentic banking (τ³ +15 to 27%), and SciCode (+7 to 50%) [[glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index-ef3ea3a0]]. Pricing holds at $1.4/$4.4/$0.26 per 1M input/output/cache-hit tokens. The verbosity caveat remains: GLM-5.2 uses 43k output tokens per AA Index task (37k reasoning), up from GLM-5.1's 26k and well above MiniMax-M3 (24k) — a cost multiplier on output-dominated agentic loops [[glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index-ef3ea3a0]].

> Z.ai's GLM-5.2 is the new leading open weights model on the Artificial Analysis Intelligence Index, scoring 51. GLM-5.2 is the same size as GLM-5.1 (744B total / 40B active parameters) but scores 11 points higher on the Intelligence Index v4.1, placing ahead of MiniMax-M3 (44), DeepSeek V4 Pro (max, 44) and Kimi K2.6 (43).

Z.AI's technical blog for GLM-5.2 adds coding benchmark detail: SWE-bench Pro 62.1% (up from GLM-5.1's 58.4%), Terminal-Bench 2.1 81.0% (vs 63.5%), and FrontierSWE Dominance 74.4% (vs 30.5%) [[glm-5-2-built-for-long-horizon-tasks-9e3636b0]]. This positions GLM-5.2 ahead of GPT-5.5 (58.6%) on SWE-bench Pro, while trailing Opus 4.8 (69.2%).

> Terminal-Bench 2.1: 81.0 vs. 63.5 (previous version). SWE-bench Pro: 62.1 vs. 58.4. FrontierSWE (Dominance): 74.4 vs. 30.5. [[glm-5-2-built-for-long-horizon-tasks-9e3636b0]]

GLM-5.2's agentic-leaderboard position is further substantiated on GDPval-AA v2, the highest-weighted sub-evaluation in AA Intelligence Index v4.1 (Agents = 34% of weighting): GLM-5.2 scores **1524** on GDPval-AA v2, ahead of MiniMax-M3 (1418) and DeepSeek V4 Pro (max, 1328), and in-line with proprietary models including GPT-5.5 (xhigh reasoning) [[glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index-ef3ea3a0]].

> GLM-5.2 scores 1524 on GDPval-AA v2, ahead of MiniMax-M3 (1418) and DeepSeek V4 Pro (max, 1328), placing it in-line with proprietary models including GPT-5.5 (xhigh reasoning). [[glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index-ef3ea3a0]]

Z.AI released **GLM-5.3** on August 14, 2026 as the successor to GLM-5.2, using the **same base model as GLM-5.2 with all improvements driven by post-training** [[glm-5-3-overview-7e6c3dd9]]. It delivers markedly stronger agentic-coding results at every effort level while consuming fewer output tokens: Terminal-Bench 3.0 rises 4.6→28.3, DeepSWE v1.1 46.2→66.9, and Agents' Last Exam 23.8→28.5, with a ~50% gain over GLM-5.2 on Z.ai Code Bench; at Max effort GLM-5.3 reaches 34.5% at ~75K output tokens/task versus GLM-5.2's 23.4% at 96K [[glm-5-3-overview-7e6c3dd9]]. Z.AI's own figures place GLM-5.3 at **84.5% on CyberGym** (ahead of Claude Mythos 5, GPT-5.6 Sol and Kimi K3), **GDPval-AA v2 1769** (up from GLM-5.2's 1508) and an AutomationBench lead at 48.2 — but, citing the cyber-capability profile, Z.AI **held back the downloadable weights until ~August 28, 2026** for safety hardening, so unlike prior GLM releases GLM-5.3 shipped API-first without open weights and its benchmark claims remain vendor-reported pending independent verification [[z-ai-delays-glm-5-3-weights-after-cybergym-score-tops-mythos-bca697d6]].

> GLM-5.3 uses the same base model as GLM-5.2, with all improvements driven by post-training. [[glm-5-3-overview-7e6c3dd9]]

> Z.ai says GLM-5.3 scored 84.5% on CyberGym, ahead of Anthropic's Mythos 5, then held the downloadable weights back until around August 28 for safety hardening. [[z-ai-delays-glm-5-3-weights-after-cybergym-score-tops-mythos-bca697d6]]

Artificial Analysis independently places **GLM-5.3 (max) at 60 on the AA Intelligence Index** — up 9 points from GLM-5.2's 51 and the first Z.AI model to reach 60 — priced at $1.40/$4.40 per 1M input/output tokens [[glm-5-3-max-intelligence-performance-price-analysis-26ed0788]]. The model is very verbose: it generated 170M tokens during AA Index evaluation vs. a median of 72M, at 93 tokens/second. The weights remain proprietary and not publicly available as of the source date.

> GLM-5.3 (max) scores 60 on the Artificial Analysis Intelligence Index, placing it well above average among comparable models (median: 35). [[glm-5-3-max-intelligence-performance-price-analysis-26ed0788]]

> Pricing for GLM-5.3 (max) is $1.40 per 1M input tokens (moderately priced, median: $1.75) and $4.40 per 1M output tokens (moderately priced, median: $10.00). [[glm-5-3-max-intelligence-performance-price-analysis-26ed0788]]

**GLM-5.3-Flash** was released 2026-08-26 as a cost-efficient variant within the GLM-5.3 line, using a **320B-total / 18B-active Mixture-of-Experts** architecture — dramatically smaller than the GLM-5.2/5.3 base (744B / 40B active) — while reaching **AA Intelligence Index 57**, matching Kimi K3's open-weights aggregate lead at a fraction of the parameter count and establishing a new intelligence-density benchmark in the efficient/small open-weights segment [[glm-5-3-flash-intelligence-performance-price-analysis-b02205ef]]. This makes GLM-5.3-Flash the highest-intelligence model per active parameter in Z.AI's product line.

> GLM-5.3-Flash scores 57 on the Artificial Analysis Intelligence Index, placing it well above average among comparable models (median: 35).

> GLM-5.3-Flash is a Mixture of Experts (MoE) model with 320 billion total parameters, but only 18 billion active parameters are used during inference.

Pricing is **$0.15 per 1M input tokens** and **$0.50 per 1M output tokens**, dramatically cheaper than GLM-5.3 (max)'s $1.40/$4.40 (~9× cheaper on input, ~9× cheaper on output), with a **1M-token context window** and text+image input support [[glm-5-3-flash-intelligence-performance-price-analysis-b02205ef]]. This positions it for high-volume agentic and game-dev content pipelines where intelligence-per-dollar dominates top-end reasoning.

> Pricing for GLM-5.3-Flash is $0.15 per 1M input tokens (moderately priced, median: $0.30) and $0.50 per 1M output tokens (moderately priced, median: $1.20).

The key caveat is verbosity: Artificial Analysis flags GLM-5.3-Flash as "**notably slow and very verbose**", so the cheap per-token headline understates per-task cost on long agentic loops — the same pattern seen with GLM-5.2 and GLM-5.3 (max) [[glm-5-3-flash-intelligence-performance-price-analysis-b02205ef]].

> GLM-5.3-Flash is amongst the leading models in intelligence and reasonably priced when comparing to other open weight models of similar size. It is also notably slow and very verbose.

## Disputes

- [[glm-5-everything-you-need-to-know-a53ff5c1]] claims GLM-5 (AA Index 50, released Feb 11 2026) is the leading open-weights model, but [[kimi-k26-the-new-leading-open-weights-model-0bea9ccd]] reports a later open-weights leader: Moonshot's Kimi K2.6 at AA Index 54 (released Apr 20), co-tied with Xiaomi's MiMo-V2.5-Pro at 54 (released Apr 22) [[mimo-v2-5-pro-intelligence-performance-price-analysis-51e3baae]]. Qwen3.7 Max scores 57 but is closed-weights API-only [[qwen3-7-max-intelligence-performance-price-analysis-61bdb800]]. Status: resolved-toward-B — GLM-5 was the open-weights leader at its February release but has since been overtaken by the Kimi K2.6 / MiMo-V2.5-Pro co-leadership at 54; the 'new leading open weights model' framing is time-bound to early 2026.
- [[z-ai-delays-glm-5-3-weights-after-cybergym-score-tops-mythos-bca697d6]] reports GLM-5.3 at a vendor-claimed 84.5% on CyberGym, topping Claude Mythos 5; [[claude-mythos-preview-d737ab91]] records Claude Mythos at 83.1% on CyberGym. Status: unresolved — vendor-reported with weights withheld until ~Aug 28, pending independent verification.
- The page Summary states "GLM-5.2 now holds the open-weights #1 position on AA Intelligence Index v4.1 at 51" citing [[glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index-ef3ea3a0]], but [[glm-5-2-built-for-long-horizon-tasks-9e3636b0]] states GLM-5.2 scores 51 on AA Index v4.0 and 41 on AA Index v4.1 (agentic-reweighted). Status: unresolved — if v4.1 = 41, GLM-5.2 would be below MiniMax-M3 (44) and DeepSeek V4-Pro (44) on v4.1, reversing the open-weights leadership claim.
- [[z-ai-introduces-glm-5-1-an-open-weight-754b-agentic-model-that-achieves-sota-on-swe-bench-pro-and-sustains-8-hour-autonomous-execution-27ebed2a]] claims GLM-5.1 sets SWE-Bench Pro SOTA at 58.4 ahead of GPT-5.4 / Opus 4.6 / Gemini 3.1 Pro; independent [[glm-5-1-intelligence-performance-price-analysis-fb6f086c]] places GLM-5.1 at AA Intelligence Index 51 and GDPval-AA #2 among open weights — strong for open weights but below the closed frontier. Status: resolved-toward-A-narrowly — the coding-axis SOTA is plausible but GLM-5.1 is not an aggregate-leaderboard frontier model.

## Open questions

- [ ] How much of GLM-5's agentic-index lead (63) among open-weights models is attributable to DeepSeek Sparse Attention vs. its 28.5T-token pretraining scale-up?
- [ ] Does the sparse-attention integration measurably help long-horizon agentic loops?
- [ ] What is GLM-5's performance on contamination-resistant benchmarks like SWE-bench Pro?
- [ ] What is GLM-5.1's hosted API pricing, and does it maintain GLM-5's $1.00/$3.20 pricing or shift to reflect the 754B parameter scale-up [[z-ai-introduces-glm-5-1-an-open-weight-754b-agentic-model-that-achieves-sota-on-swe-bench-pro-and-sustains-8-hour-autonomous-execution-27ebed2a]]?
- [ ] Does GLM-5.1's 8-hour autonomous-execution claim translate into measurably higher completion rates on long-horizon benchmarks like SWE-Chain or Terminal-Bench compared to GLM-5 [[z-ai-introduces-glm-5-1-an-open-weight-754b-agentic-model-that-achieves-sota-on-swe-bench-pro-and-sustains-8-hour-autonomous-execution-27ebed2a]]?
- [ ] Is there an independent artificialanalysis.ai SWE-Bench Pro placement for GLM-5.1 that confirms or refutes the vendor 58.4 SOTA figure, now that its aggregate AA Index (51) is independently established [[glm-5-1-intelligence-performance-price-analysis-fb6f086c]]?
- [ ] Do GLM-5.3's vendor-reported benchmark claims (CyberGym 84.5%, GDPval-AA v2 1769) survive independent Artificial Analysis testing once the withheld weights ship ~Aug 28, 2026?
- [ ] GLM-5.3 (max) generated 170M tokens during AA Index evaluation vs. a median of 72M [[glm-5-3-max-intelligence-performance-price-analysis-26ed0788]] — does this extreme verbosity make GLM-5.3 net-more-expensive than competitors with lower AA scores but far lower output-token usage on agentic loops?
- [ ] Will Z.AI open-source the GLM-5.3 weights as previously planned, and does the ~Aug 28 safety-hardening timeline slip after the CyberGym score became public?

## See also

- [[frontier-models]]
- [[deepseek-v4]]
- [[claude-opus-4.7]]
