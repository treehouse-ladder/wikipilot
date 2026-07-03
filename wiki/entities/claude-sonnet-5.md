---
title: "Claude Sonnet 5"
kind: entity
sources: ["[[introducing-claude-sonnet-5-4307222b]]", "[[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]]"]
last_updated: 2026-07-03
last_verified: 2026-07-03
freshness_window_days: 30
input_cost_per_mtoken: 2.00
output_cost_per_mtoken: 10.00
cost_source: "[[introducing-claude-sonnet-5-4307222b]]"
aa_intelligence_index: 53
aa_intelligence_index_source: "[[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]]"
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

Claude Sonnet 5 is Anthropic's mid-tier frontier model, released June 30, 2026, succeeding [[claude-sonnet-4.6]] [[introducing-claude-sonnet-5-4307222b]]. Introductory pricing is **$2 input / $10 output per Mtoken through August 31, 2026**, reverting to **$3/$15** thereafter [[introducing-claude-sonnet-5-4307222b]]. Artificial Analysis places Sonnet 5 (Adaptive Reasoning, Max Effort) at **53 on the AA Intelligence Index v4.1** — public #5, behind Claude Fable 5, Opus 4.8, GPT-5.5 (xhigh) and Opus 4.7 [[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]]. It is a strict improvement over Sonnet 4.6 (+9 points on Terminal-Bench v2.1) and matches or outperforms Opus 4.8 on the agentic AA-Briefcase and GDPval-AA knowledge-work evals; early-access partners describe it as "much more agentic" than predecessors [[introducing-claude-sonnet-5-4307222b]]. Cost caveat for agentic loops: despite a lower per-token price than Opus 4.8, Sonnet 5 costs **~$2.29 per Intelligence-Index task (~2x Sonnet 4.6, ~15% more than Opus 4.8)**, driven entirely by increased token usage [[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]].

> Sonnet 5 is available today at an introductory price of $2 per million input tokens and $10 per million output tokens through August 31, 2026, then moves to standard pricing at $3 per million input tokens and $15 per million output tokens. [[introducing-claude-sonnet-5-4307222b]]

> Claude Sonnet 5 (Adaptive Reasoning, Max Effort) scores 53 on the Artificial Analysis Intelligence Index. Claude Sonnet 5 costs $2.29 per task on the Intelligence Index, a ~2x increase compared to Sonnet 4.6 and ~15% more than Claude Opus 4.8. [[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]]

## Open questions

- [ ] What is Claude Sonnet 5's SWE-bench Pro (contamination-resistant) score vs Opus 4.8 (69.2%)? No SWE-bench Pro figure was published at launch [[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]].
- [ ] Does Sonnet 5's lower per-token price ever produce net-cheaper task economics than Opus 4.8 at lower effort settings? [[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]]

## See also

- [[claude-sonnet-4.6]]
- [[claude-opus-4.8]]
- [[claude-fable-5]]
- [[frontier-models]]
