---
title: "Claude Opus 5"
kind: entity
sources: ["[[introducing-claude-opus-5-c34a3276]]", "[[meet-the-new-claude-opus-5-frontier-class-agentic-coding-and-computer-use-at-unchanged-opus-pricing-7f7892b3]]", "[[anthropic-launches-claude-opus-5-its-fourth-model-in-two-months-and-it-tops-fable-5-on-most-benchmarks-7253a489]]", "[[opus-5-fable-5-level-intelligence-at-a-lower-cost-per-task-864f9aa5]]", "[[claude-opus-5-the-new-leader-in-agentic-knowledge-work-92cf92da]]", "[[launching-v4-1-1-of-the-artificial-analysis-intelligence-index-8f7aaf85]]"]
last_updated: 2026-08-09
last_verified: 2026-08-09
freshness_window_days: 30
input_cost_per_mtoken: 5.00
output_cost_per_mtoken: 25.00
cost_source: "[[introducing-claude-opus-5-c34a3276]]"
aa_intelligence_index: 61
aa_intelligence_index_source: "[[opus-5-fable-5-level-intelligence-at-a-lower-cost-per-task-864f9aa5]]"
gdpval_aa_elo: 1861
gdpval_aa_elo_source: "[[claude-opus-5-the-new-leader-in-agentic-knowledge-work-92cf92da]]"
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

Artificial Analysis's primary evaluation (published 2026-07-26) confirms **Claude Opus 5 (max) at 61 on the AA Intelligence Index v4.1 — narrowly the most intelligent model in the world**, ahead of Fable 5 (max, 60), GPT-5.6 Sol (max, 59) and Kimi K3 (57) [[opus-5-fable-5-level-intelligence-at-a-lower-cost-per-task-864f9aa5]]. It reaches Fable-5-class intelligence at **~26% lower cost per Intelligence Index task ($2.03 vs $2.75)** [[opus-5-fable-5-level-intelligence-at-a-lower-cost-per-task-864f9aa5]], and leads agentic knowledge work with the highest recorded **GDPval-AA v2 (1861 Elo)** and **AA-Briefcase (1720 Elo, +146 over Fable 5)** [[claude-opus-5-the-new-leader-in-agentic-knowledge-work-92cf92da]].

> Claude Opus 5 (max) scores 61 on the Artificial Analysis Intelligence Index, effectively tied with Claude Fable 5 (max, 60), and ahead of GPT-5.6 Sol (max, 59), Kimi K3 (57). [[opus-5-fable-5-level-intelligence-at-a-lower-cost-per-task-864f9aa5]]

> On GDPval-AA v2, Claude Opus 5 (max) scores 1861 Elo, more than 100 points ahead of Claude Fable 5 and GPT-5.6 Sol (max), making it a leader in agentic knowledge work tasks. [[claude-opus-5-the-new-leader-in-agentic-knowledge-work-92cf92da]]

Under the Artificial Analysis Intelligence Index **v4.1.1** patch (2026-08-06 — grader upgrade to GPT-5.6 Luna medium for HLE/AA-LCR/AA-Omniscience, τ³-Banking → v1.0.1), Opus 5 (max) **remains #1 and re-scales up from v4.1 = 61 to 63** as a grading-robustness effect rather than a capability change [[launching-v4-1-1-of-the-artificial-analysis-intelligence-index-8f7aaf85]]. (Entity frontmatter still records the v4.1 = 61 figure; Opus 5 is outside [frontier_models].roster, so the 63 value is filed for backfill under the topic's Open questions.)

> Claude Opus 5 remains in the #1 position with an Index of 63. Overall model rankings remain largely consistent, with a slight increase in scores due to improved grading robustness. [[launching-v4-1-1-of-the-artificial-analysis-intelligence-index-8f7aaf85]]

## Disputes

- [[anthropic-launches-claude-opus-5-its-fourth-model-in-two-months-and-it-tops-fable-5-on-most-benchmarks-7253a489]] claims Opus 5 tops Fable 5 on most benchmarks at half the price; [[meet-the-new-claude-opus-5-frontier-class-agentic-coding-and-computer-use-at-unchanged-opus-pricing-7f7892b3]] notes Fable 5 still edges Opus 5 on SWE-bench Pro (80.0%) and remains the recommendation for multi-day autonomous agent work. Status: unresolved — Opus 5 is the value default; Fable 5 keeps the top-end long-horizon coding crown.

## Open questions

- [ ] What is Claude Opus 5's ARC-AGI-2 score? Only ARC-AGI-3 (30.16%) was published.

## See also

- [[claude-opus-4.8]]
- [[claude-fable-5]]
- [[claude-sonnet-5]]
- [[frontier-models]]
