---
title: "Kimi K2.7 Code"
kind: entity
sources: ["[[kimi-k2-7-code-9c6b3767]]", "[[kimi-k2-7-code-intelligence-performance-and-price-analysis-b3d43ac0]]"]
last_updated: 2026-06-28
last_verified: 2026-06-23
freshness_window_days: 30
input_cost_per_mtoken: null
output_cost_per_mtoken: null
cost_source: null
aa_intelligence_index: 42
aa_intelligence_index_source: "[[kimi-k2-7-code-intelligence-performance-and-price-analysis-b3d43ac0]]"
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

Kimi K2.7 Code is Moonshot AI's coding-specialist open-weights model, released June 12, 2026. It is built on the same 1T total / 32B active MoE architecture as [[kimi-k2.6]] but fine-tuned specifically for long-horizon software engineering agentic tasks [[kimi-k2-7-code-9c6b3767]]. It scores **42 on the AA Intelligence Index v4.1** [[kimi-k2-7-code-intelligence-performance-and-price-analysis-b3d43ac0]], placing it one rung above K2.6 (43) on the agentic-reweighted scale.

> With substantial improvements on real-world long-horizon coding tasks, it strengthens end-to-end task completion across complex software engineering workflows...reducing thinking-token usage by approximately 30% compared with Kimi K2.6. [[kimi-k2-7-code-9c6b3767]]

Key benchmark improvements over Kimi K2.6: Kimi Code Bench v2 62.0 vs. 50.9 (+21.8%), MCP Atlas 76.0 vs. 69.4, MCP Mark Verified 81.1 vs. 72.8 [[kimi-k2-7-code-9c6b3767]]. The model reduces thinking-token usage by approximately 30% versus K2.6 — a meaningful cost reduction for agentic-coding loops that consume long reasoning traces. Architecture: 384 experts total, 8 selected per token, 256K context window. License: Modified MIT, self-hostable.

## Disputes

- [[kimi-k2-7-code-intelligence-performance-and-price-analysis-b3d43ac0]] reports K2.7 Code scores 42 on AA Intelligence Index v4.1 and that K2.6 scores 43 on the same scale; the Summary on this page claims K2.7 Code "plac[es] it one rung above K2.6 (43)" but 42 < 43 — K2.7 Code ranks *below* K2.6 on the AA v4.1 scale despite its coding-specialist improvements. Status: unresolved — the math is internally inconsistent; the text likely intended to say K2.7 Code scores lower overall on the general intelligence index while outperforming K2.6 on task-specific coding benchmarks.

## Open questions

- [ ] No SWE-bench Pro or SWE-bench Verified score published independently for K2.7 Code — vendor benchmarks (Kimi Code Bench v2) are internal and not directly comparable to cross-model leaderboards. What is the SWE-bench Verified score?

## See also

- [[kimi-k2.6]]
- [[frontier-models]]
- [[agentic-coding]]
