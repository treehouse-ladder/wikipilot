---
title: "GPT-5.5"
kind: entity
sources: ["[[introducing-gpt-55-dfe7e0c6]]", "[[openais-gpt-55-is-the-new-leading-ai-model-097f1222]]", "[[openai-api-pricing-fa525e16]]", "[[gdpval-aa-leaderboard-artificial-analysis-5d24e844]]", "[[swe-bench-verified-leaderboard-may-2026-marc0-dev-4c34ac5d]]", "[[arc-agi-2-benchmark-leaderboard-benchlm-ai-caa132e2]]", "[[cybergym-benchmark-leaderboard-llm-stats-com-81499a0b]]", "[[claude-opus-4-8-max-intelligence-performance-price-analysis-27b7d2eb]]", "[[previewing-gpt-5-6-sol-a-next-generation-model-30f48121]]"]
last_updated: 2026-06-29
last_verified: 2026-06-18
freshness_window_days: 30
input_cost_per_mtoken: 5.00
output_cost_per_mtoken: 30.00
cost_source: "[[openai-api-pricing-fa525e16]]"
aa_intelligence_index: 55
aa_intelligence_index_source: "[[claude-opus-4-8-max-intelligence-performance-price-analysis-27b7d2eb]]"
gdpval_aa_elo: 1531
gdpval_aa_elo_source: "[[claude-opus-4-8-max-intelligence-performance-price-analysis-27b7d2eb]]"
swe_bench_verified: 0.887
swe_bench_verified_source: "[[swe-bench-verified-leaderboard-may-2026-marc0-dev-4c34ac5d]]"
cybergym: 0.818
cybergym_source: "[[cybergym-benchmark-leaderboard-llm-stats-com-81499a0b]]"
arc_agi_2: 0.850
arc_agi_2_source: "[[arc-agi-2-benchmark-leaderboard-benchlm-ai-caa132e2]]"
---

## Summary

GPT-5.5 was released April 23, 2026, alongside GPT-5.5 Pro [[introducing-gpt-55-dfe7e0c6]]. GPT-5.5 (xhigh) currently ranks #1 on the Artificial Analysis Intelligence Index at 60, followed by GPT-5.5 (high) at 59 [[openais-gpt-55-is-the-new-leading-ai-model-097f1222]]. The model is priced higher than GPT-5.4 but is also more token-efficient — OpenAI claims it delivers better results with fewer tokens on most tasks. It is positioned for agentic coding, computer use, and knowledge work.

> GPT-5.5 is priced higher than GPT-5.4, but it is both more intelligent and much more token efficient, delivering better results with fewer tokens.

> GPT-5.5 (xhigh) currently ranks #1 on the Artificial Analysis LLM Leaderboard with an Intelligence Index score of 60.

GPT-5.5 standard API pricing is $5.00 per million input tokens and $30.00 per million output tokens; cached input is $0.50/M [[openai-api-pricing-fa525e16]]. Prompts above 272K input tokens are priced at 2x input and 1.5x output for the full session.

> GPT-5.5: Input $5.00 / 1M tokens. Cached input $0.50 / 1M tokens. Output $30.00 / 1M tokens.

On the live [[gdpval-aa-leaderboard-artificial-analysis-5d24e844]], GPT-5.5 (xhigh) is now the new #1 at 1769 Elo, with GPT-5.5 (high) at 1754 — both ahead of Claude Opus 4.7's 1753, ending Opus 4.7's brief week-long lead. GPT-5.5 also leads [[swe-bench-verified-leaderboard-may-2026-marc0-dev-4c34ac5d]] at 88.7% (April 23 release), edging Opus 4.7's 87.6%. On [[arc-agi-2-benchmark-leaderboard-benchlm-ai-caa132e2]] (the hardest public abstract-reasoning benchmark), GPT-5.5 leads at 85.0% — well clear of GPT-5.4 Pro (83.3%) and Gemini 3.1 Pro (77.1%). And on [[cybergym-benchmark-leaderboard-llm-stats-com-81499a0b]], GPT-5.5 is the highest-scoring generally-available model at 81.8% (behind only the invitation-only Mythos Preview at 83.1%).

> GPT-5.5 (xhigh) scores the highest on GDPval with a score of 1769.

> GPT-5.5 from OpenAI takes the new #1 spot on SWE-Bench Verified at 88.7%.

> GPT-5.5 leads the ARC-AGI-2 leaderboard with 85%.

> GPT-5.5 sits at 81.8% [on CyberGym].

> GPT-5.5 (xhigh) scores 55 [on the Artificial Analysis Intelligence Index v4.1].

> GPT-5.5 xhigh scored 1531 [on GDPval-AA v2].

OpenAI announced a successor flagship line, **GPT-5.6 (Sol / Terra / Luna)**, in limited preview on June 26, 2026 — Sol is positioned as OpenAI's new strongest model, setting a new state of the art on Terminal-Bench 2.1 and improving over GPT-5.5 on software engineering, computer use, knowledge work, scientific research, and cybersecurity [[previewing-gpt-5-6-sol-a-next-generation-model-30f48121]]. GPT-5.6 Sol lists at the same $5/$30 per Mtoken as GPT-5.5, with cheaper Terra ($2.50/$15) and Luna ($1/$6) tiers; the family is partner-gated in preview (no public Artificial Analysis Intelligence Index placement yet) ahead of planned general availability in ChatGPT, Codex, and the API "in the coming weeks." GPT-5.5 (AA Intelligence Index v4.1 = 55) therefore remains OpenAI's current publicly-placed flagship until GPT-5.6 is independently benchmarked and reaches GA.

> We're beginning a limited preview of the GPT-5.6 series: Sol, our new flagship model; Terra, a balanced model for everyday work; and Luna, a fast and affordable model. GPT-5.6 Sol is OpenAI's strongest model yet. [[previewing-gpt-5-6-sol-a-next-generation-model-30f48121]]

## Disputes

- [[openais-gpt-55-is-the-new-leading-ai-model-097f1222]] claims GPT-5.5 #1 on aggregate AA Intelligence Index, but [[claude-opus-47-everything-you-need-to-know-751c1827]] claims Claude Opus 4.7 leads GDPval-AA (the agentic/economic-value sub-benchmark) by 79 Elo points. Status: unresolved — top-of-leaderboard depends on whether you weight aggregate intelligence or agentic task performance.
- [[introducing-gpt-55-dfe7e0c6]] claims GPT-5.5 was released "April 24, 2026"; [[openais-gpt-55-is-the-new-leading-ai-model-097f1222]] claims "April 23, 2026". Status: unresolved — one-day discrepancy may reflect announcement vs. API availability dates. Confidence: high. Sweep: 2026-05-21.
- [[openais-gpt-55-is-the-new-leading-ai-model-097f1222]] claims GPT-5.5 (xhigh) is "#1 on the Artificial Analysis Intelligence Index at 60" and "#1 on GDPval-AA at 1769 Elo"; [[claude-opus-4-8-takes-the-lead-on-the-artificial-analysis-intelligence-index-57303c9c]] shows Claude Opus 4.8 (released May 28, 2026) now leads at AA Intelligence Index 61.4 and GDPval-AA 1890 Elo. Status: unresolved (confidence: high; sweep: 2026-05-31)

## Open questions

- [ ] How much of GPT-5.5's GDPval-AA advantage over GPT-5.4 (1769 vs 1676) is attributable to the new tokenizer + extended-thinking behavior vs. base model improvements — knowing this would help estimate where GPT-5.6 lands.

## See also

- [[frontier-models]]
- [[claude-opus-4.7]]
- [[gemini-3.1-pro]]
