---
title: "Claude Haiku 5.5"
kind: entity
aliases: ["claude-haiku-5-5", "Haiku 5.5"]
sources: ["[[introducing-claude-haiku-5-5-cdb1d51f]]", "[[anthropic-has-released-claude-haiku-5-5-2072257c]]"]
last_updated: 2026-10-08
last_verified: 2026-10-08
freshness_window_days: 30
input_cost_per_mtoken: 0.10
output_cost_per_mtoken: 0.50
cost_source: "[[introducing-claude-haiku-5-5-cdb1d51f]]"
aa_intelligence_index: 43
aa_intelligence_index_source: "[[anthropic-has-released-claude-haiku-5-5-2072257c]]"
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

Claude Haiku 5.5 (`claude-haiku-5-5`) is Anthropic's smallest and cheapest model in the Claude 5.5 family, released 2026-10-08, completing the Claude 5.5 lineup alongside Opus 5.5 and Sonnet 5.5 [[introducing-claude-haiku-5-5-cdb1d51f]]. It is designed for high-volume, cost-sensitive workloads: summarization, subagents, and browser use. It carries a **1M-token context window** and is available on all major Anthropic distribution surfaces (Claude Platform, AWS, Google Cloud, Microsoft Azure, Claude.ai, Claude Code).

**Pricing (two tiers):** For prompts ≤100K tokens: **$0.10 input / $0.50 output per Mtoken** — 90% below Claude Haiku 4.5 at this tier. For prompts >100K tokens: $0.50/$2.50 per Mtoken (50% below Haiku 4.5) [[introducing-claude-haiku-5-5-cdb1d51f]]. On average, Anthropic reports it costs ~75% less to run than prior Haiku.

> Claude Haiku 5.5 is our cheapest, fastest, and most capable small model, built for high-volume, cost-sensitive work such as summarization, subagents, and browser use. On average, it now costs around 75% less to run. [[introducing-claude-haiku-5-5-cdb1d51f]]

On the **AA Intelligence Index, Haiku 5.5 scores 43 (max)** — a +26-point jump year-over-year, well above the median for comparable models (median: 13) [[anthropic-has-released-claude-haiku-5-5-2072257c]]. Effort scores: max 43, xhigh 41, high 38, medium 34, low 29.

> Claude Haiku 5.5 scores 43 on the Artificial Analysis Intelligence Index, up 26 points one year after the last Haiku release. The result places it well above average among comparable models (median: 13). [[anthropic-has-released-claude-haiku-5-5-2072257c]]

Token efficiency caveat: Haiku 5.5 (max) uses ~162K output tokens per Intelligence Index task — more than Opus 5.5 (max) and ~3× GPT-6 Luna (max) — making it token-hungry at max effort despite the low per-token rate. On AutomationBench-AA it scores 35% (vs 53–60% for flash-class peers), but Artificial Analysis flags this may understate capability due to a pre-release safety over-refusal issue.

> Claude Haiku 5.5 (max) uses ~162k output tokens per Intelligence Index task, more than Opus 5.5 (max) and ~3x GPT-6 Luna (max). [[anthropic-has-released-claude-haiku-5-5-2072257c]]

## Disputes

- [[introducing-claude-haiku-5-5-cdb1d51f]] describes Haiku 5.5 as ~75% cheaper on average; [[anthropic-has-released-claude-haiku-5-5-2072257c]] highlights that at max effort it uses ~162K output tokens (more than Opus 5.5 max), potentially erasing the per-token price advantage. Status: unresolved — the 75% cheaper claim is for typical/average use; at max effort the output-volume expansion means per-task cost savings depend heavily on effort level.

## Open questions

- [ ] Does the Haiku 5.5 safety refusal issue (over-refusal on AutomationBench-AA in pre-release) persist in the GA release, and is the 35% AutomationBench-AA score a stable measurement or a testing artifact?
- [ ] What is Haiku 5.5's per-task cost at low or medium effort (typical subagent use) compared to Haiku 4.5?

## See also

- [[frontier-models]] — topic index
- [[claude-sonnet-5-5]] — sibling model in the Claude 5.5 family
- [[claude-opus-5-5]] — flagship in the Claude 5.5 family
- [[cost-comparison]] — comparison page
