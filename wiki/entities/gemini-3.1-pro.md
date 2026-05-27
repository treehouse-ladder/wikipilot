---
title: "Gemini 3.1 Pro"
kind: entity
sources: ["[[gemini-31-pro-model-card-225ab705]]", "[[openais-gpt-55-is-the-new-leading-ai-model-097f1222]]", "[[swe-bench-verified-leaderboard-may-2026-marc0-dev-4c34ac5d]]", "[[arc-agi-2-benchmark-leaderboard-benchlm-ai-caa132e2]]", "[[gemini-3-5-frontier-intelligence-with-action-f4ceaac7]]"]
last_updated: "2026-05-27"
last_verified: "2026-05-27"
freshness_window_days: 30
input_cost_per_mtoken: 2.00
output_cost_per_mtoken: 12.00
cost_source: "[[gemini-31-pro-model-card-225ab705]]"
aa_intelligence_index: 57
aa_intelligence_index_source: "[[openais-gpt-55-is-the-new-leading-ai-model-097f1222]]"
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

Gemini 3.1 Pro Preview is Google DeepMind's current frontier model on the Pro tier, with a 1M-token input context window and up to 64k-token output [[gemini-31-pro-model-card-225ab705]]. Pricing is tiered by context length — a first among major frontier models: $2/$12 per Mtoken (input/output, including thinking tokens) for prompts at or below 200k tokens, jumping to $4/$18 above 200k. It scores 57 on the Artificial Analysis Intelligence Index [[openais-gpt-55-is-the-new-leading-ai-model-097f1222]], and leads the AA Omniscience Index.

> Input price: $2.00 for prompts <= 200k tokens, $4.00 for prompts > 200k tokens; Output price (including thinking tokens): $12.00 for prompts <= 200k tokens, $18.00 for prompts > 200k tokens.

On [[swe-bench-verified-leaderboard-may-2026-marc0-dev-4c34ac5d]], Gemini 3.1 Pro scores 80.6% (tied with DeepSeek V4 Pro Max), well behind the GPT-5.5 / Opus 4.7 frontier. On [[arc-agi-2-benchmark-leaderboard-benchlm-ai-caa132e2]] Gemini 3.1 Pro is the strongest non-reasoning model at 77.1% — ahead of Opus 4.7 Adaptive (75.8%) and only behind GPT-5.5 and GPT-5.4 Pro.

> Gemini 3.1 Pro at 80.6% [SWE-bench Verified].

> Gemini 3.1 Pro — Non-Reasoning — 77.1 [ARC-AGI-2].

_no contradictions or gaps known yet (last reviewed: 2026-05-22)_

## Open questions

- [ ] What is the practical retrieval/long-context quality drop-off between 200k and 1M context for Gemini 3.1 Pro?
- [ ] When Gemini 3.5 Pro ships (Google announced ~June 2026 per [[gemini-3-5-frontier-intelligence-with-action-f4ceaac7]]), will it replace Gemini 3.1 Pro as Google's Pro-tier offering, or will both remain available?

## See also

- [[frontier-models]]
- [[claude-opus-4.7]]
- [[gpt-5.5]]
