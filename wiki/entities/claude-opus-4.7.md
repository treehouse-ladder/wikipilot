---
title: "Claude Opus 4.7"
kind: entity
sources: ["[[introducing-claude-opus-47-b8af8104]]", "[[claude-opus-47-everything-you-need-to-know-751c1827]]", "[[swe-chain-benchmarking-coding-agents-on-chained-release-level-package-upgrades-26980c45]]", "[[building-a-c-compiler-with-a-team-of-parallel-claudes-1eba12a4]]", "[[swe-bench-verified-leaderboard-may-2026-marc0-dev-4c34ac5d]]", "[[arc-agi-2-benchmark-leaderboard-benchlm-ai-caa132e2]]", "[[cybergym-benchmark-leaderboard-llm-stats-com-81499a0b]]", "[[roadmapbench-evaluating-long-horizon-agentic-software-development-across-version-upgrades-b9814b39]]", "[[featurebench-benchmarking-agentic-coding-for-complex-feature-development-12948611]]", "[[claude-opus-4-8-takes-the-lead-on-the-artificial-analysis-intelligence-index-57303c9c]]"]
last_updated: 2026-05-29
last_verified: 2026-05-29
freshness_window_days: 30
input_cost_per_mtoken: 5.00
output_cost_per_mtoken: 25.00
cost_source: "[[introducing-claude-opus-47-b8af8104]]"
aa_intelligence_index: 57
aa_intelligence_index_source: "[[claude-opus-47-everything-you-need-to-know-751c1827]]"
gdpval_aa_elo: 1753
gdpval_aa_elo_source: "[[claude-opus-47-everything-you-need-to-know-751c1827]]"
swe_bench_verified: 0.876
swe_bench_verified_source: "[[swe-bench-verified-leaderboard-may-2026-marc0-dev-4c34ac5d]]"
cybergym: 0.731
cybergym_source: "[[cybergym-benchmark-leaderboard-llm-stats-com-81499a0b]]"
arc_agi_2: 0.758
arc_agi_2_source: "[[arc-agi-2-benchmark-leaderboard-benchlm-ai-caa132e2]]"
---

## Summary

Claude Opus 4.7 is Anthropic's flagship model released April 16, 2026 [[introducing-claude-opus-47-b8af8104]]. It scores 57 on the Artificial Analysis Intelligence Index in Adaptive Reasoning Max Effort mode (a 4-point uplift over Opus 4.6) and is the leader on GDPval-AA at 1,753 Elo, ~79 Elo points ahead of the next-tier models [[claude-opus-47-everything-you-need-to-know-751c1827]]. On Anthropic's 93-task internal coding benchmark, Opus 4.7 lifted resolution by 13% over Opus 4.6. Despite being more capable, Opus 4.7 (Adaptive Reasoning, Max Effort) costs ~$4,406 to run the Intelligence Index, ~11% less than Opus 4.6 (~$4,970). It ranks #2 on the AA Omniscience Index (behind Gemini 3.1 Pro), with the improvement coming primarily from reduced hallucination rather than higher accuracy.

> Claude Opus 4.7 is our most intelligent model, with state-of-the-art performance on coding, agentic tasks, and reasoning.

> Opus 4.7 is the new leader on GDPval-AA, scoring 1,753 Elo, around 79 Elo points ahead of the next closest models.

> Pricing remains the same as Opus 4.6: $5 per million input tokens and $25 per million output tokens.

On the current `[[swe-bench-verified-leaderboard-may-2026-marc0-dev-4c34ac5d]]`, Opus 4.7 scores 87.6% — dropped to #2 in May 2026 when GPT-5.5 took the lead at 88.7%. On `[[arc-agi-2-benchmark-leaderboard-benchlm-ai-caa132e2]]`, Opus 4.7 (Adaptive) scores 75.8%, ranking #4 overall — solidly mid-pack among reasoning configurations. On `[[cybergym-benchmark-leaderboard-llm-stats-com-81499a0b]]` (the active successor to the now-saturated original Cybench), Opus 4.7 (Adaptive) scores 73.1%, third behind the invitation-only Claude Mythos Preview (83.1%) and GPT-5.5 (81.8%).

> Claude Opus 4.7 drops to 87.6% at #2 (April 16, 2026, 1M context).

> Claude Opus 4.7 (Adaptive) — 75.8.

> Claude Opus 4.7 (Adaptive) ... 73.1%.

On multi-step package upgrades, Claude Opus 4.7 (Claude Code) scores 60.8% resolving, 80.6% precision, and 68.5% F1 on SWE-Chain, which measures chained release-level upgrades where each transition builds on the agent's prior codebase [[swe-chain-benchmarking-coding-agents-on-chained-release-level-package-upgrades-26980c45]]. The C compiler parallel-agents case study ran on Opus 4.7 (then referred to as Claude Code) across "nearly 2,000 Claude Code sessions and $20,000 in API costs" producing a 100,000-line compiler consuming "2 billion input tokens and 140 million output tokens across two weeks" [[building-a-c-compiler-with-a-team-of-parallel-claudes-1eba12a4]].

On long-horizon coding benchmarks beyond single-issue resolution, Opus 4.7 shows substantial capability degradation. RoadmapBench reports "resolved rates range from 5.2% to 39.1%, with Claude-Opus-4.7 resolving 39.1% of tasks" on "115 long-horizon coding tasks grounded in real open-source version upgrades ... with a median modification of 3,700 lines across 51 files" [[roadmapbench-evaluating-long-horizon-agentic-software-development-across-version-upgrades-b9814b39]]. FeatureBench, evaluating end-to-end feature-oriented development, reports that "Claude 4.5 Opus, which achieves 74.4% resolved rate on SWE-bench, succeeds on only 11.0% of tasks" across "200 evaluation tasks and 3825 executable environments from 24 open source GitHub repositories" [[featurebench-benchmarking-agentic-coding-for-complex-feature-development-12948611]] — a ~7x gap representing the largest single-issue-vs-real-task delta the wiki has recorded.

> RoadmapBench is a benchmark of 115 long-horizon coding tasks grounded in real open-source version upgrades across 17 repositories and 5 programming languages, with a median modification of 3,700 lines across 51 files. Resolved rates range from 5.2% to 39.1%, with Claude-Opus-4.7 resolving 39.1% of tasks.

> FeatureBench is a benchmark designed to evaluate agentic coding performance in end-to-end, feature-oriented software development. The benchmark comprises 200 evaluation tasks and 3825 executable environments from 24 open source GitHub repositories. Claude 4.5 Opus, which achieves 74.4% resolved rate on SWE-bench, succeeds on only 11.0% of tasks, highlighting the gap between traditional bug-fixing benchmarks and complex feature development.

> SWE-Chain contains 12 upgrade chains across 9 real Python packages, with 155 version transitions and 1,660 grounded upgrade requirements, where each transition builds on the agent's prior codebase. Claude-Opus-4.7 (Claude Code) leads at 60.8% resolving, 80.6% precision, and 68.5% F1.

> Over nearly 2,000 Claude Code sessions and $20,000 in API costs, the agent team produced a 100,000-line compiler that can build Linux 6.9 on x86, ARM, and RISC-V. The project consumed 2 billion input tokens and 140 million output tokens across two weeks.

> Claude Opus 4.8 is the new leader on the Artificial Analysis Intelligence Index with a score of 61.4, up 4.1 points from Opus 4.7 and 1.2 points ahead of GPT-5.5 (xhigh), the previous Index leader.

As of May 28, 2026, Opus 4.7 is superseded by [[claude-opus-4.8]] as Anthropic's flagship model. The AA Intelligence Index re-confirms Opus 4.7's score at 57 [[claude-opus-4-8-takes-the-lead-on-the-artificial-analysis-intelligence-index-57303c9c]].

## Disputes

- [[claude-opus-47-everything-you-need-to-know-751c1827]] claims Opus 4.7 leads GDPval-AA at 1753 Elo "around 79 Elo points ahead of the next closest models"; the live [[gdpval-aa-leaderboard-artificial-analysis-5d24e844]] now shows GPT-5.5 (xhigh) ahead at 1769 Elo and GPT-5.5 (high) at 1754 — both released after the Opus 4.7 article. Status: resolved-toward-current-leaderboard — Opus 4.7's "ahead by 79 Elo" was true at its April 16 launch but was overtaken by GPT-5.5 on April 23.

## Open questions

- [ ] How does Claude-Opus-4.7's 60.8% on SWE-Chain [[swe-chain-benchmarking-coding-agents-on-chained-release-level-package-upgrades-26980c45]] degrade across the chain length — is the per-transition success rate roughly constant, or does error accumulate so that long chains collapse?

## See also

- [[frontier-models]]
- [[gpt-5.5]]
- [[gemini-3.1-pro]]
