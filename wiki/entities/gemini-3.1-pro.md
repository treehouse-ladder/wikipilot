---
title: "Gemini 3.1 Pro"
kind: entity
sources: ["[[gemini-31-pro-model-card-225ab705]]", "[[openais-gpt-55-is-the-new-leading-ai-model-097f1222]]", "[[swe-bench-verified-leaderboard-may-2026-marc0-dev-4c34ac5d]]", "[[arc-agi-2-benchmark-leaderboard-benchlm-ai-caa132e2]]", "[[gemini-3-5-frontier-intelligence-with-action-f4ceaac7]]", "[[gemini-3-1-pro-preview-intelligence-performance-price-analysis-3a3f9933]]", "[[google-has-released-gemini-3-8-flash-its-fourth-flash-model-in-under-four-months-8aa591b1]]", "[[gemini-3-8-flash-model-card-1867674a]]"]
last_updated: 2026-09-03
last_verified: 2026-06-21
freshness_window_days: 30
input_cost_per_mtoken: 2.00
output_cost_per_mtoken: 12.00
cost_source: "[[gemini-31-pro-model-card-225ab705]]"
aa_intelligence_index: 46
aa_intelligence_index_source: "[[gemini-3-1-pro-preview-intelligence-performance-price-analysis-3a3f9933]]"
gdpval_aa_elo: null
gdpval_aa_elo_source: null
swe_bench_verified: 0.806
swe_bench_verified_source: "[[swe-bench-verified-leaderboard-may-2026-marc0-dev-4c34ac5d]]"
cybergym: null
cybergym_source: null
arc_agi_2: 0.771
arc_agi_2_source: "[[arc-agi-2-benchmark-leaderboard-benchlm-ai-caa132e2]]"
---

## Summary

Gemini 3.1 Pro Preview is Google DeepMind's current frontier model on the Pro tier, with a 1M-token input context window and up to 64k-token output [[gemini-31-pro-model-card-225ab705]]. Pricing is tiered by context length — a first among major frontier models: $2/$12 per Mtoken (input/output, including thinking tokens) for prompts at or below 200k tokens, jumping to $4/$18 above 200k. It scores **46 on the Artificial Analysis Intelligence Index v4.1** [[gemini-3-1-pro-preview-intelligence-performance-price-analysis-3a3f9933]], down from 57 on v4.0, reflecting the v4.1 re-weighting toward agentic workloads (GDPval-AA, Terminal-Bench, tau3). It retains the #1 spot on AA-Omniscience at 33, though now surpassed by Claude Fable 5 at 40 [[claude-fable-5-launches-at-1-on-the-artificial-analysis-intelligence-index-a03d0111]].

> Gemini 3.1 Pro Preview scores 46 on the Artificial Analysis Intelligence Index, placing it well above average among other reasoning models in a similar price tier (median: 29). On AA-Omniscience, Fable 5 scores 40, +7 points over the previous leader, Gemini 3.1 Pro Preview, driven primarily by higher accuracy. [[gemini-3-1-pro-preview-intelligence-performance-price-analysis-3a3f9933]]

> Input price: $2.00 for prompts <= 200k tokens, $4.00 for prompts > 200k tokens; Output price (including thinking tokens): $12.00 for prompts <= 200k tokens, $18.00 for prompts > 200k tokens. [[gemini-31-pro-model-card-225ab705]]

On [[swe-bench-verified-leaderboard-may-2026-marc0-dev-4c34ac5d]], Gemini 3.1 Pro scores 80.6% (tied with DeepSeek V4 Pro Max), well behind the GPT-5.5 / Opus 4.7 frontier. On [[arc-agi-2-benchmark-leaderboard-benchlm-ai-caa132e2]] Gemini 3.1 Pro is the strongest non-reasoning model at 77.1% — ahead of Opus 4.7 Adaptive (75.8%) and only behind GPT-5.5 and GPT-5.4 Pro.

> Gemini 3.1 Pro at 80.6% [SWE-bench Verified]. [[swe-bench-verified-leaderboard-may-2026-marc0-dev-4c34ac5d]]

> Gemini 3.1 Pro — Non-Reasoning — 77.1 [ARC-AGI-2]. [[arc-agi-2-benchmark-leaderboard-benchlm-ai-caa132e2]]

**Gemini 3.8 Flash (released Sep 2, 2026)** is Google's new Flash-tier workhorse, superseding Gemini 3.7 Flash. Artificial Analysis independently places Gemini 3.8 Flash at **59 (high) / 57 (medium) / 52 (low)** on the Intelligence Index — **+3 over Gemini 3.7 Flash** — with the improvement driven by agentic evaluations (τ³-Banking, Terminal-Bench v2.1, GDPval-AA v2); at 59 (high) it now sits **above Claude Opus 4.8 (56) and GPT-5.5 (55)** on the aggregate index [[google-has-released-gemini-3-8-flash-its-fourth-flash-model-in-under-four-months-8aa591b1]]. Google frames it as its 'most intelligent workhorse model yet, built for long-horizon coding and autonomous agents,' with **text/image/audio/video/PDF input, text output, a 1M-token context, a 64K output ceiling, function calling, search-as-a-tool and computer use**, and it is now the **default model in Google Antigravity** [[gemini-3-8-flash-model-card-1867674a]].

> Gemini 3.8 Flash (high) scores 59 on the Artificial Analysis Intelligence Index, up 3 points from Gemini 3.7 Flash. With medium reasoning it scores 57, and with low reasoning it scores 52. [[google-has-released-gemini-3-8-flash-its-fourth-flash-model-in-under-four-months-8aa591b1]]

> Gemini 3.8 Flash is our most intelligent workhorse model yet, built for long-horizon coding and autonomous agents. The model takes text, image, audio, video and PDF in, gives text out, and holds a 1M token context window with a 64K output ceiling. [[gemini-3-8-flash-model-card-1867674a]]

_no contradictions or gaps known yet (last reviewed: 2026-06-21)_

## Open questions

- [ ] What is the practical retrieval/long-context quality drop-off between 200k and 1M context for Gemini 3.1 Pro?
- [ ] When Gemini 3.5 Pro ships (Google announced ~June 2026 per [[gemini-3-5-frontier-intelligence-with-action-f4ceaac7]]), will it replace Gemini 3.1 Pro as Google's Pro-tier offering, or will both remain available?

## See also

- [[frontier-models]]
- [[claude-opus-4.7]]
- [[gpt-5.5]]
