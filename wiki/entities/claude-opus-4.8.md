---
title: "Claude Opus 4.8"
kind: entity
aliases: ["Opus 4.8", "claude-opus-4-8", "Claude Opus 4.8"]
sources: ["[[introducing-claude-opus-4-8-5348a7d2]]", "[[claude-opus-4-8-takes-the-lead-on-the-artificial-analysis-intelligence-index-57303c9c]]", "[[claude-opus-4-8-benchmarks-explained-60247f20]]", "[[how-opus-4-8-compares-to-claude-mythos-and-gpt-5-5-80451407]]", "[[nemotron-3-ultra-announced-high-speed-leading-us-open-weights-intelligence-81a38c83]]", "[[claude-fable-5-and-claude-mythos-5-e11fcea9]]", "[[claude-opus-4-8-max-intelligence-performance-price-analysis-27b7d2eb]]", "[[claude-in-microsoft-foundry-is-now-generally-available-9f490039]]", "[[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]]"]
last_updated: 2026-07-08
last_verified: 2026-07-08
freshness_window_days: 30
input_cost_per_mtoken: 5.00
output_cost_per_mtoken: 25.00
cost_source: "[[introducing-claude-opus-4-8-5348a7d2]]"
aa_intelligence_index: 56
aa_intelligence_index_source: "[[claude-opus-4-8-max-intelligence-performance-price-analysis-27b7d2eb]]"
gdpval_aa_elo: 1638
gdpval_aa_elo_source: "[[claude-opus-4-8-max-intelligence-performance-price-analysis-27b7d2eb]]"
swe_bench_verified: 0.886
swe_bench_verified_source: "[[claude-opus-4-8-benchmarks-explained-60247f20]]"
cybergym: 0.788
cybergym_source: "[[how-opus-4-8-compares-to-claude-mythos-and-gpt-5-5-80451407]]"
arc_agi_2: null
arc_agi_2_source: null
---

## Summary

**Note (2026-06-09)**: Claude Opus 4.8 is superseded by [[claude-fable-5]] as Anthropic's publicly-available flagship, which scores 64.9 on AA Intelligence Index (vs Opus 4.8's 61.4) and 1932 on GDPval-AA (vs 1890) at 2× the price ($10/$50 per Mtoken) [[claude-fable-5-and-claude-mythos-5-e11fcea9]]. Opus 4.8 remains available and is the fallback for Fable 5 queries in cybersecurity/biology domains.

Claude Opus 4.8 is Anthropic's flagship model, released May 28, 2026 as the successor to Opus 4.7 [[introducing-claude-opus-4-8-5348a7d2]]. It is the new leader on the Artificial Analysis Intelligence Index (v4.0) at 61.4 — up 4.1 points over Opus 4.7 (57) and 1.2 points ahead of GPT-5.5 (xhigh, 60), the previous index leader [[claude-opus-4-8-takes-the-lead-on-the-artificial-analysis-intelligence-index-57303c9c]]. It also retakes GDPval-AA, Anthropic's primary agentic/knowledge-work evaluation, at 1,890 Elo — roughly 121 Elo and an implied ~67% win rate ahead of GPT-5.5, reversing the GPT-5.5 GDPval lead held since late April [[claude-opus-4-8-takes-the-lead-on-the-artificial-analysis-intelligence-index-57303c9c]]. List pricing is unchanged from Opus 4.7 at $5/$25 per Mtoken [[introducing-claude-opus-4-8-5348a7d2]].

> Claude Opus 4.8 is the new leader on the Artificial Analysis Intelligence Index with a score of 61.4, up 4.1 points from Opus 4.7 and 1.2 points ahead of GPT-5.5 (xhigh), the previous Index leader.

> Anthropic retakes the lead on GDPval-AA, their primary evaluation for agentic performance on knowledge work tasks, with Opus 4.8 scoring an 1,890 Elo, reflecting an implied win rate of approximately 67% against GPT-5.5.

On coding, Opus 4.8 scores 88.6% on SWE-bench Verified and 69.2% on the contamination-resistant SWE-bench Pro — up from 64.3% on Opus 4.7 [[claude-opus-4-8-takes-the-lead-on-the-artificial-analysis-intelligence-index-57303c9c]]. Anthropic positions it as the strongest computer-use/browser-agent model tested at 84% on Online-Mind2Web, the only model to complete every Super-Agent case end-to-end, 4x less likely than Opus 4.7 to ship code with unflagged flaws, and ships a research-preview Fast mode in Claude Code running at 2.5x speed for $30/$150 per Mtoken — roughly 3x cheaper than the prior fast tier [[introducing-claude-opus-4-8-5348a7d2]].

> Claude Opus 4.8 is the strongest computer-use and browser-agent model we have tested, scoring 84% on Online-Mind2Web, a meaningful jump over both Opus 4.7 and GPT-5.5.

> On the Super-Agent benchmark, Claude Opus 4.8 is the only model to complete every case end-to-end, beating prior Opus models and GPT-5.5 at parity on cost.

> Opus 4.8 scores 88.6% on SWE-bench Verified and 69.2% on SWE-bench Pro, up from 64.3% on Opus 4.7.

Independent placement detail (post-launch): Opus 4.8 scores 78.8% on CyberGym vulnerability reproduction, third behind Mythos Preview (83.1%) and GPT-5.5 (81.8%) [[how-opus-4-8-compares-to-claude-mythos-and-gpt-5-5-80451407]] — up from Opus 4.7's 73.1%. On SWE-Bench Pro, Opus 4.8's 69.2% is over 10 points ahead of GPT-5.5 (58.6%) and Gemini 3.1 Pro (54.2%) [[claude-opus-4-8-benchmarks-explained-60247f20]]. Mythos still leads by 8.6 points on SWE-bench Pro (77.8 vs 69.2), and by a large margin on the Firefox-exploit subset of CyberGym (70.8% full-exploit rate vs 8.8%), while the two tie on GPQA Diamond at ~94 [[how-opus-4-8-compares-to-claude-mythos-and-gpt-5-5-80451407]].

> Claude Opus 4.8 scored 78.8% on the CyberGym leaderboard, placing it third behind Claude Mythos Preview at 83.1% and GPT-5.5 at 81.8%.

> SWE-Bench Pro (Coding): Opus 4.8 lands at 69.2%, almost 5 points clear of Opus 4.7 (64.3%) and over 10 points ahead of GPT-5.5 (58.6%) and Gemini 3.1 Pro (54.2%).

> Claude Opus 4.8 (Adaptive Reasoning, Max Effort) currently has the highest Artificial Analysis Intelligence Index score, with a score of 61 among models with published results.

> Claude Opus 4.8 (max, 56) is the most intelligent available model according to the Artificial Analysis Intelligence Index v4.1.

> GDPval-AA v2 is the highest weighted evaluation in the Intelligence Index v4.1. Claude Opus 4.8 scored 1638 on GDPval-AA v2, the highest among available models.

> Claude Opus 4.8 ranks #2 on the Intelligence Index with a score of 56, while Claude Sonnet 5 ranks #5 with a score of 53. [[claude-sonnet-5-strong-agentic-performance-at-a-higher-cost-per-task-c4346bb2]]

**Distribution milestone (2026-06-30)**: Claude Opus 4.8 and Claude Haiku 4.5 are now generally available in Microsoft Azure Foundry [[claude-in-microsoft-foundry-is-now-generally-available-9f490039]]. Azure-native deployment with existing Azure identity, networking, and governance controls.

> Claude in Microsoft Foundry is generally available today. Claude Opus 4.8 and Claude Haiku 4.5 are available in the Messages API, with core capabilities like prompt caching and extended thinking to support use cases ranging from coding and agentic work to complex reasoning. [[claude-in-microsoft-foundry-is-now-generally-available-9f490039]]

## Disputes

- [[claude-opus-4-8-takes-the-lead-on-the-artificial-analysis-intelligence-index-57303c9c]] claims Opus 4.8 is the public AA Intelligence Index #1 at 61.4; [[claude-mythos-preview-d737ab91]] claims an unreleased Anthropic model (Claude Mythos Preview) is state-of-the-art on SWE-bench Verified (93.9%) and withheld from GA. Status: unresolved — the public leaderboard #1 (Opus 4.8) is not Anthropic's true capability ceiling while Mythos remains invitation-only.

## Open questions

- [ ] What is Claude Opus 4.8's ARC-AGI-2 placement? It was not published in the launch post [[introducing-claude-opus-4-8-5348a7d2]] or the AA analysis [[claude-opus-4-8-takes-the-lead-on-the-artificial-analysis-intelligence-index-57303c9c]], so the profile field stays null pending an independent leaderboard.
- [ ] Why is the public-vs-Mythos gap an order of magnitude larger on CyberGym Firefox-exploit production (8.8% vs 70.8%) than on aggregate CyberGym (78.8 vs 83.1) or GPQA Diamond (tied at ~94)?

## See also

- [[claude-fable-5]]
- [[frontier-models]]
- [[claude-opus-4.7]]
- [[cost-comparison]]
