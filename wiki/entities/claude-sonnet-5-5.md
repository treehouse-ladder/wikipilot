---
title: "Claude Sonnet 5.5"
kind: entity
sources: ["[[release-v2-1-284-anthropics-claude-code-cdf0d632]]", "[[introducing-claude-sonnet-5-5-4e3ca8a9]]", "[[claude-sonnet-5-5-reaches-2-on-the-artificial-analysis-intelligence-index-4075a9b8]]", "[[gemini-4-argon-google-is-back-as-one-of-the-top-three-labs-in-intelligence-achieved-52050b56]]"]
last_updated: 2026-10-04
last_verified: 2026-09-30
freshness_window_days: 30
input_cost_per_mtoken: 2.00
output_cost_per_mtoken: 10.00
cost_source: "[[release-v2-1-284-anthropics-claude-code-cdf0d632]]"
aa_intelligence_index: 56
aa_intelligence_index_source: "[[claude-sonnet-5-5-reaches-2-on-the-artificial-analysis-intelligence-index-4075a9b8]]"
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

Claude Sonnet 5.5 (`claude-sonnet-5-5`) is Anthropic's mid-tier frontier model, released 2026-09-29. It scores **56 on the Artificial Analysis Intelligence Index (max effort) — #2 overall, behind only Opus 5.5 (58) and +18 points over Claude Sonnet 5** [[claude-sonnet-5-5-reaches-2-on-the-artificial-analysis-intelligence-index-4075a9b8]]. This is described as "an unusually large generational jump for a mid-tier model" [[claude-sonnet-5-5-reaches-2-on-the-artificial-analysis-intelligence-index-4075a9b8]].

> Claude Sonnet 5.5 (max) scores 56 on the Artificial Analysis Intelligence Index, reaching #2, behind only Claude Opus 5.5 (max, 58) and ahead of Claude Fable 5.1 (max with fallback) and GPT-6 Astra (max) at 53. [[claude-sonnet-5-5-reaches-2-on-the-artificial-analysis-intelligence-index-4075a9b8]]

The jump is driven primarily by agentic coding: **Terminal-Bench v4.0 at 70.6%, up from Sonnet 5's 10.3%** — a 60-point gain on the agentic terminal benchmark [[introducing-claude-sonnet-5-5-4e3ca8a9]]. It scores two points below Opus 5.5 on GDPval-AA, a test of real-world work across occupations [[introducing-claude-sonnet-5-5-4e3ca8a9]]. On several benchmarks, Sonnet 5.5 at Low or Medium effort beats Sonnet 5's best score for about a tenth of the cost per task — using about a third fewer tool calls and roughly half the shell runs to finish a task [[introducing-claude-sonnet-5-5-4e3ca8a9]].

> With max effort, Sonnet 5.5 gains 18 points over Sonnet 5 and moves to #2 on the Intelligence Index, behind only Opus 5.5 (max). [[introducing-claude-sonnet-5-5-4e3ca8a9]]

> Sonnet 5.5 scores 70.6% on Terminal-Bench 4.0, an agentic coding evaluation, compared to Sonnet 5's 10.3%. It scores two points below Opus 5.5 on GDPval-AA. [[introducing-claude-sonnet-5-5-4e3ca8a9]]

Sonnet 5.5 is priced at **$2/$10 per Mtoken** (matching Sonnet 5) with up to 90% prompt-caching savings and 50% batch savings, and runs **~30% cheaper than Sonnet 5 for typical token-billed workloads** [[introducing-claude-sonnet-5-5-4e3ca8a9]]. It is the **first Sonnet model to beat Pokémon Red working only from screenshots** [[introducing-claude-sonnet-5-5-4e3ca8a9]]. Made the default Sonnet on the Anthropic API via Claude Code v2.1.284 (released 2026-09-28) alongside auto-mode becoming default across all plans [[release-v2-1-284-anthropics-claude-code-cdf0d632]].

## Disputes

- [[introducing-claude-sonnet-5-5-4e3ca8a9]] and [[claude-sonnet-5-5-reaches-2-on-the-artificial-analysis-intelligence-index-4075a9b8]] claim Terminal-Bench 4.0 score is 70.6%; [[gemini-4-argon-google-is-back-as-one-of-the-top-three-labs-in-intelligence-achieved-52050b56]] claims 64%. Status: unresolved (confidence: high; sweep: 2026-10-04)

> On Terminal-Bench 4.0, Sonnet 5.5 scores 70.6%, up from Sonnet 5's 10.3%. [[claude-sonnet-5-5-reaches-2-on-the-artificial-analysis-intelligence-index-4075a9b8]]

> Sonnet 5.5 scores 70.6% on Terminal-Bench 4.0, an agentic coding evaluation, compared to Sonnet 5's 10.3%. It scores two points below Opus 5.5 on GDPval-AA. [[introducing-claude-sonnet-5-5-4e3ca8a9]]

> On Terminal Bench 4, Gemini 4 Argon achieves 57%, only behind Claude Sonnet 5.5 (max, 64%), Claude Opus 5.5 (max, 60%) and GPT-6 Astra (59%). [[gemini-4-argon-google-is-back-as-one-of-the-top-three-labs-in-intelligence-achieved-52050b56]]

## Open questions

- [x] What is Claude Sonnet 5.5's standing on SWE-bench Verified, Terminal-Bench, and the AA Intelligence Index vs Claude Sonnet 5 and Claude Opus 5.5? **Answered 2026-09-30**: AA Index 56 (#2), Terminal-Bench 4.0 70.6% (vs Sonnet 5's 10.3%), 2 pts below Opus 5.5 on GDPval-AA [[introducing-claude-sonnet-5-5-4e3ca8a9]] [[claude-sonnet-5-5-reaches-2-on-the-artificial-analysis-intelligence-index-4075a9b8]].
- [ ] Does Sonnet 5.5 exhibit the RL-co-adaptation tool-schema drift (newer Anthropic models inventing extra tool-call fields) reported for Opus 4.8/Sonnet 5 in agentic-coding harnesses?
- [ ] Does the $0.20/Mtoken cache read price materially reduce per-task cost in long-running agentic sessions vs Claude Sonnet 5's cache pricing?

## See also

- [[claude-sonnet-5]]
- [[claude-opus-5-5]]
- [[frontier-models]]
- [[agentic-coding]]
