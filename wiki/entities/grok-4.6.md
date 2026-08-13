---
title: "Grok 4.6"
kind: entity
aliases: ["Grok4.6", "grok 4.6", "SpaceXAI Grok 4.6"]
sources: ["[[introducing-grok-4-6-66321e57]]", "[[grok-4-6-returns-spacexai-to-the-intelligence-frontier-and-leads-on-cost-efficiency-bdc6284a]]"]
last_updated: 2026-08-13
last_verified: 2026-08-13
freshness_window_days: 30
input_cost_per_mtoken: 2.00
output_cost_per_mtoken: 6.00
cost_source: "[[introducing-grok-4-6-66321e57]]"
aa_intelligence_index: 61
aa_intelligence_index_source: "[[grok-4-6-returns-spacexai-to-the-intelligence-frontier-and-leads-on-cost-efficiency-bdc6284a]]"
gdpval_aa_elo: 1753
gdpval_aa_elo_source: "[[grok-4-6-returns-spacexai-to-the-intelligence-frontier-and-leads-on-cost-efficiency-bdc6284a]]"
swe_bench_verified: null
swe_bench_verified_source: null
cybergym: null
cybergym_source: null
arc_agi_2: null
arc_agi_2_source: null
---

# Grok 4.6

## Summary

Grok 4.6 is SpaceXAI's (formerly xAI) flagship model, released **2026-08-12** as a **post-training upgrade over [[grok-4.5]]** — the base foundation is held constant, with the improvement spent on a longer supplemental training run, regenerated supervised fine-tuning trajectories, and reinforcement learning in agentic environments, targeting long-running agents and more ambitious interactive/visual work [[introducing-grok-4-6-66321e57]]. It ships a **500,000-token context**, is priced at **$2/$6 per Mtoken input/output** (unchanged from Grok 4.5), and launched day-one in **Cursor**, Grok Build, the API, OpenRouter, Vercel and Cloudflare [[introducing-grok-4-6-66321e57]]. On the **Artificial Analysis Intelligence Index v4.1.1** it scores **61 (high)**, **+5 over Grok 4.5 (54)** and +23 over Grok 4.3, **tying GPT-5.6 Sol (max, 61)** for aggregate-index #3 — behind Claude Opus 5 (max, 63) and Claude Fable 5 (62) and just ahead of Kimi K3 (57) [[grok-4-6-returns-spacexai-to-the-intelligence-frontier-and-leads-on-cost-efficiency-bdc6284a]]. On **GDPval-AA v2** it posts **Elo 1753 — second only to Claude Opus 5** (1861), with confidence intervals overlapping Fable 5 and Qwen3.8 Max; it debuts on **AA-Briefcase at Elo 1577**, scores **τ³-Banking 50.7% (top two)** and **Terminal-Bench v2.1 88.4% (level with leaders)** [[grok-4-6-returns-spacexai-to-the-intelligence-frontier-and-leads-on-cost-efficiency-bdc6284a]]. Its distinguishing strength is **token/turn cost efficiency**: Artificial Analysis measures it resolving tasks in **~53 turns and ~0.5B input tokens** versus **~103 turns and ~2.0B input tokens for Claude Opus 5 (max)**, giving a cost advantage well beyond its 60%+ per-token discount on long-horizon agentic loops [[grok-4-6-returns-spacexai-to-the-intelligence-frontier-and-leads-on-cost-efficiency-bdc6284a]]. Grok 4.6 **supersedes [[grok-4.5]]** as the SpaceXAI flagship.

> Grok 4.6 is available today in Cursor and Grok Build. It's also available in the API and other partners like OpenRouter, Vercel, and Cloudflare. Pricing starts at $2 per million input tokens and $6 per million output tokens. [[introducing-grok-4-6-66321e57]]

> Grok 4.6 builds on Grok 4.5 with a particular focus on long-running agents and more ambitious interactive and visual work. [[introducing-grok-4-6-66321e57]]

> Grok 4.6 scores 61 on the Artificial Analysis Intelligence Index, in line with GPT-5.6 Sol (max), behind Claude Opus 5 (max, 63) and Claude Fable 5 (max with fallback, 62), and just ahead of Kimi K3. Grok 4.6 gains 5 points over Grok 4.5. [[grok-4-6-returns-spacexai-to-the-intelligence-frontier-and-leads-on-cost-efficiency-bdc6284a]]

> Grok 4.6 achieves a GDPval-AA v2 Elo of 1753, behind only Claude Opus 5. [[grok-4-6-returns-spacexai-to-the-intelligence-frontier-and-leads-on-cost-efficiency-bdc6284a]]

> Grok 4.6 resolves tasks in ~53 turns and ~0.5B input tokens on average, against ~103 turns and ~2.0B input tokens for Claude Opus 5 (max). [[grok-4-6-returns-spacexai-to-the-intelligence-frontier-and-leads-on-cost-efficiency-bdc6284a]]

## Disputes

_none_

## Open questions

- [ ] Grok 4.6's contamination-resistant coding (SWE-bench Pro) score is unreported — its standing on the credible frontier-coding axis vs Fable 5 (80.0%) and Opus 5 is unknown.

## See also

- [[grok-4.5]]
- [[grok-4.3]]
- [[gpt-5.6-sol]]
- [[claude-opus-5]]
- [[claude-fable-5]]
- [[cost-comparison]]
- [[benchmark-leaders]]
