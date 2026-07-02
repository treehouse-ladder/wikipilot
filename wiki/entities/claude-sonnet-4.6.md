---
title: "Claude Sonnet 4.6"
kind: entity
sources: ["[[introducing-claude-sonnet-46-c4a45eed]]", "[[gdpval-aa-leaderboard-artificial-analysis-5d24e844]]", "[[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]]"]
last_updated: "2026-07-02"
last_verified: "2026-05-22"
freshness_window_days: 30
input_cost_per_mtoken: 3.00
output_cost_per_mtoken: 15.00
cost_source: "[[introducing-claude-sonnet-46-c4a45eed]]"
aa_intelligence_index: 51
aa_intelligence_index_source: "[[introducing-claude-sonnet-46-c4a45eed]]"
gdpval_aa_elo: 1683
gdpval_aa_elo_source: "[[gdpval-aa-leaderboard-artificial-analysis-5d24e844]]"
swe_bench_verified: null
swe_bench_verified_source: null
cybergym: null
cybergym_source: null
arc_agi_2: 0.604
arc_agi_2_source: "[[introducing-claude-sonnet-46-c4a45eed]]"
---

## Summary

**Note (2026-07-02)**: Claude Sonnet 4.6 has been superseded by [[claude-sonnet-5]], released June 30, 2026, which scores AA Intelligence Index v4.1 = 53 (+6 over Sonnet 4.6's v4.1 re-placement) and SWE-bench Pro 63.2% (up from 58.1%) [[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]].

Claude Sonnet 4.6 is Anthropic's mid-tier frontier model, released February 17, 2026 [[introducing-claude-sonnet-46-c4a45eed]]. Pricing starts at $3/$15 per million input/output tokens, with a 1M-token context window in beta. Sonnet 4.6 scores 51 on the Artificial Analysis Intelligence Index — an 8-point jump over Sonnet 4.5 — and leads all tested models on GDPval-AA and TerminalBench at the time of release (outperforming even Opus 4.6). On the contamination-controlled ARC-AGI-2 it scores 60.4% with 120k thinking tokens at High effort.

> Pricing remains the same as Sonnet 4.5, starting at $3/$15 per million tokens.

> Sonnet 4.6 scores 51 on the Artificial Analysis Intelligence Index, an 8-point jump from Sonnet 4.5. Sonnet 4.6 leads all models tested on GDPval-AA and TerminalBench, outperforming even Claude Opus 4.6.

> Sonnet 4.6 achieved 86.5% on ARC-AGI-1 and 60.4% on ARC-AGI-2 with 120k thinking tokens and High effort.

Sonnet 4.6 currently sits at 1683 Elo on the live [[gdpval-aa-leaderboard-artificial-analysis-5d24e844]] — #4 globally, ahead of every other Anthropic model on this evaluation and 30 Elo points ahead of Opus 4.6.

> Claude Sonnet 4.6 (Adaptive Reasoning, Max Effort) is #4 at 1683.

## Disputes

- [[introducing-claude-sonnet-46-c4a45eed]] claims Sonnet 4.6 is "ahead of every other Anthropic model on this evaluation" on GDPval-AA at 1683 Elo; [[claude-opus-4-8-takes-the-lead-on-the-artificial-analysis-intelligence-index-57303c9c]] shows Opus 4.8 now leads at 1890 Elo and [[claude-opus-47-everything-you-need-to-know-751c1827]] shows Opus 4.7 at 1753 Elo — both Anthropic models now rank higher. Status: unresolved (confidence: high; sweep: 2026-05-31)

## Open questions

- [ ] Exact GDPval-AA Elo, SWE-bench Verified, and Cybench scores for Claude Sonnet 4.6 — release notes claim GDPval-AA leadership over Opus 4.6 but the numeric Elo isn't quoted in current sources.

## See also

- [[frontier-models]]
- [[claude-opus-4.7]]
