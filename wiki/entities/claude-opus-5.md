---
title: "Claude Opus 5"
kind: entity
sources: ["[[introducing-claude-opus-5-c34a3276]]", "[[meet-the-new-claude-opus-5-frontier-class-agentic-coding-and-computer-use-at-unchanged-opus-pricing-7f7892b3]]", "[[anthropic-launches-claude-opus-5-its-fourth-model-in-two-months-and-it-tops-fable-5-on-most-benchmarks-7253a489]]"]
last_updated: 2026-07-25
last_verified: 2026-07-25
freshness_window_days: 30
input_cost_per_mtoken: 5.00
output_cost_per_mtoken: 25.00
cost_source: "[[introducing-claude-opus-5-c34a3276]]"
aa_intelligence_index: null
aa_intelligence_index_source: null
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

Claude Opus 5 is Anthropic's standard flagship model, released **July 24, 2026** as the successor to [[claude-opus-4.8]] and Anthropic's fourth model in under two months (after [[claude-fable-5]] in early June and [[claude-sonnet-5]] at end of June) [[anthropic-launches-claude-opus-5-its-fourth-model-in-two-months-and-it-tops-fable-5-on-most-benchmarks-7253a489]]. It ships at **$5/$25 per Mtoken — unchanged from Opus 4.8 and about half of Fable 5's $10/$50** — with a research-preview **Fast mode ~2.5x faster at $10/$50** and a **1M-token context window** [[introducing-claude-opus-5-c34a3276]] [[meet-the-new-claude-opus-5-frontier-class-agentic-coding-and-computer-use-at-unchanged-opus-pricing-7f7892b3]].

> Claude Opus 5 is our most intelligent model, delivering frontier performance for agentic coding, computer use, and complex reasoning at the same price as Claude Opus 4.8: $5 per million input tokens and $25 per million output tokens. [[introducing-claude-opus-5-c34a3276]]

Opus 5 introduces a new **effort setting (low to high plus a max tier)** balancing intelligence against speed, with **thinking on by default** — a change from Opus 4.8 [[introducing-claude-opus-5-c34a3276]].

> Opus 5 introduces a new effort setting, ranging from low to high plus a new max tier. Thinking is on by default on Opus 5. [[introducing-claude-opus-5-c34a3276]]

On benchmarks, Opus 5 **tops Fable 5 on most axes at half the price** [[anthropic-launches-claude-opus-5-its-fourth-model-in-two-months-and-it-tops-fable-5-on-most-benchmarks-7253a489]]: **Frontier-Bench 43.3% max effort** vs Fable 5's 33.7%; **ARC-AGI-3 30.16%** (verified, ~3x next model); **OSWorld 2.0 70.57%** (vs Opus 4.8's 55.7%); **Zapier AutomationBench 26.0%** (vs Opus 4.8 17.0%, Fable 5 17.4%) [[meet-the-new-claude-opus-5-frontier-class-agentic-coding-and-computer-use-at-unchanged-opus-pricing-7f7892b3]]. Fable 5 still leads on **SWE-bench Pro (80.0%)** and remains Anthropic's recommendation for multi-day autonomous agent work [[meet-the-new-claude-opus-5-frontier-class-agentic-coding-and-computer-use-at-unchanged-opus-pricing-7f7892b3]] [[introducing-claude-opus-5-c34a3276]].

> Opus 5 reached 70.57% on OSWorld 2.0 against 55.7% for Opus 4.8. On Zapier AutomationBench it scored 26.0%, against 17.0% for Opus 4.8 and 17.4% for Fable 5. Fable 5 still edges Opus 5 on SWE-bench Pro at 80.0%. [[meet-the-new-claude-opus-5-frontier-class-agentic-coding-and-computer-use-at-unchanged-opus-pricing-7f7892b3]]

> Claude Opus 5 tops Fable 5 on most benchmarks at half the token price and is Anthropic's most aligned model to date. [[anthropic-launches-claude-opus-5-its-fourth-model-in-two-months-and-it-tops-fable-5-on-most-benchmarks-7253a489]]

## Disputes

- [[anthropic-launches-claude-opus-5-its-fourth-model-in-two-months-and-it-tops-fable-5-on-most-benchmarks-7253a489]] claims Opus 5 tops Fable 5 on most benchmarks at half the price; [[meet-the-new-claude-opus-5-frontier-class-agentic-coding-and-computer-use-at-unchanged-opus-pricing-7f7892b3]] notes Fable 5 still edges Opus 5 on SWE-bench Pro (80.0%) and remains the recommendation for multi-day autonomous agent work. Status: unresolved — Opus 5 is the value default; Fable 5 keeps the top-end long-horizon coding crown.

## Open questions

- [ ] What is Claude Opus 5's AA Intelligence Index v4.1 placement? Reported ~61 by re-aggregators but no artificialanalysis.ai primary confirmation as of 2026-07-25.
- [ ] What is Claude Opus 5's ARC-AGI-2 score? Only ARC-AGI-3 (30.16%) was published.

## See also

- [[claude-opus-4.8]]
- [[claude-fable-5]]
- [[claude-sonnet-5]]
- [[frontier-models]]
