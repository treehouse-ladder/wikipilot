---
title: "Claude Sonnet 5"
kind: entity
aliases: ["Claude Sonnet 5", "Sonnet 5", "claude-sonnet-5"]
sources: ["[[introducing-claude-sonnet-5-4307222b]]", "[[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]]"]
last_updated: 2026-07-02
last_verified: 2026-07-02
freshness_window_days: 30
input_cost_per_mtoken: 3.00
output_cost_per_mtoken: 15.00
cost_source: "[[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]]"
aa_intelligence_index: 53
aa_intelligence_index_source: "[[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]]"
gdpval_aa_elo: 1603
gdpval_aa_elo_source: "[[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]]"
swe_bench_verified: 0.852
swe_bench_verified_source: "[[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]]"
cybergym: null
cybergym_source: null
arc_agi_2: null
arc_agi_2_source: null
---

## Summary

Claude Sonnet 5 is Anthropic's mid-tier frontier model, released June 30, 2026, and Anthropic's most agentic Sonnet to date — able to plan, use tools (browsers, terminals), and run autonomously, with performance Anthropic describes as similar to Opus 4.8 [[introducing-claude-sonnet-5-4307222b]]. It is the default model for Free and Pro plans and has a 1M-token context window. Standard pricing is $3/$15 per Mtoken (same as Sonnet 4.6), with introductory pricing of $2/$10 through August 31, 2026 [[introducing-claude-sonnet-5-4307222b]].

> Claude Sonnet 5 is our most agentic Sonnet model to date, able to make plans, use tools like browsers and terminals, and run autonomously. Sonnet 5's performance is similar to Opus 4.8... It launches with introductory pricing of $2 per million input tokens and $10 per million output tokens through August 31, 2026. [[introducing-claude-sonnet-5-4307222b]]

Artificial Analysis places Sonnet 5 at **AA Intelligence Index v4.1 = 53** (max effort, +6 over Sonnet 4.6; #5 overall, below Opus 4.8's 56 and GPT-5.5's 55), with **SWE-bench Verified 85.2%** and **SWE-bench Pro 63.2%** (up from Sonnet 4.6's 58.1%) [[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]]. On agentic knowledge-work axes it punches above its aggregate rank: **GDPval-AA v2 = 1603**, edging Opus 4.8 (1594 on the live leaderboard), and it sits just ahead of Opus 4.8 on AA-Briefcase [[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]].

> Claude Sonnet 5 achieves 53 on the Artificial Analysis Intelligence Index... Claude Sonnet 5 (Adaptive Reasoning, Max Effort) scores 1603 on GDPval-AA v2, compared to Claude Opus 4.8 with a score of 1594. [[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]]

The key economic caveat: despite Sonnet 5's lower per-token price vs Opus 4.8 ($3/$15 vs $5/$25), it costs **~$2.29 per Intelligence-Index task — ~15% MORE than Opus 4.8** — because at max effort it burns ~40% more output tokens per task than Sonnet 4.6 and ~3x the agentic turns for GDPval-AA [[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]].

> Claude Sonnet 5 costs $2.29 per task on the Intelligence Index, approximately 15% more than Claude Opus 4.8. This higher cost is driven entirely by increased token usage. [[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]]

## Disputes

- [[introducing-claude-sonnet-5-4307222b]] frames Sonnet 5's performance as 'similar to Opus 4.8'; [[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]] shows it trails Opus 4.8 on the aggregate AA Intelligence Index (53 vs 56) yet edges Opus 4.8 on GDPval-AA v2 (1603 vs 1594) and AA-Briefcase. Status: resolved-toward-B (axis-dependent — 'similar' holds on agentic knowledge-work axes but not on the aggregate reasoning index)

## Open questions

- [ ] Per-task economics vs Opus 4.8 after the $2/$10 introductory pricing expires (Aug 31, 2026).
- [ ] cybergym and ARC-AGI-2 scores for Sonnet 5 — not yet published.

## See also

- [[frontier-models]]
- [[claude-opus-4.8]]
