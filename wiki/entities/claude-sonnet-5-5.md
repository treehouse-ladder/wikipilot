---
title: "Claude Sonnet 5.5"
kind: entity
sources: ["[[release-v2-1-284-anthropics-claude-code-cdf0d632]]"]
last_updated: 2026-09-29
last_verified: 2026-09-29
freshness_window_days: 30
input_cost_per_mtoken: 2.00
output_cost_per_mtoken: 10.00
cost_source: "[[release-v2-1-284-anthropics-claude-code-cdf0d632]]"
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

Claude Sonnet 5.5 (`claude-sonnet-5-5`) is Anthropic's mid-tier frontier model, made the default Sonnet on the Anthropic API via Claude Code v2.1.284 (released 2026-09-28) [[release-v2-1-284-anthropics-claude-code-cdf0d632]]. It features a **1M context window** and pricing of **$2 input / $10 output per Mtoken with $0.20/Mtoken cache reads** — matching the $2/$10 per-token pricing of its predecessor [[claude-sonnet-5]] while adding cheaper prompt caching.

> Added Claude Sonnet 5.5 (claude-sonnet-5-5), now the default Sonnet model on the Anthropic API — 1M context, $2/$10 per Mtok with $0.20/Mtok cache reads [[release-v2-1-284-anthropics-claude-code-cdf0d632]]

The model's launch coincides with Claude Code v2.1.284 making auto mode the default permission mode across all plans and providers, expanding the auto-mode rollout previously gated to Pro/Max/Team tiers [[release-v2-1-284-anthropics-claude-code-cdf0d632]].

## Open questions

- [ ] What is Claude Sonnet 5.5's standing on SWE-bench Verified, Terminal-Bench, and the AA Intelligence Index vs Claude Sonnet 5 and Claude Opus 5.5? No benchmark figures accompanied the v2.1.284 release note [[release-v2-1-284-anthropics-claude-code-cdf0d632]].
- [ ] Does Sonnet 5.5 exhibit the RL-co-adaptation tool-schema drift (newer Anthropic models inventing extra tool-call fields) reported for Opus 4.8/Sonnet 5 in agentic-coding harnesses?
- [ ] Does the $0.20/Mtoken cache read price materially reduce per-task cost in long-running agentic sessions vs Claude Sonnet 5's cache pricing?

## See also

- [[claude-sonnet-5]]
- [[claude-opus-5-5]]
- [[frontier-models]]
- [[agentic-coding]]
