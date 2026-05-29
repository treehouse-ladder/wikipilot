---
title: "Claude Opus 4.8"
kind: entity
aliases: ["Opus 4.8", "claude-opus-4-8", "Claude Opus 4.8"]
sources: ["[[introducing-claude-opus-4-8-5348a7d2]]", "[[claude-opus-4-8-takes-the-lead-on-the-artificial-analysis-intelligence-index-57303c9c]]"]
last_updated: 2026-05-29
last_verified: 2026-05-29
freshness_window_days: 30
input_cost_per_mtoken: 5.00
output_cost_per_mtoken: 25.00
cost_source: "[[introducing-claude-opus-4-8-5348a7d2]]"
aa_intelligence_index: 61.4
aa_intelligence_index_source: "[[claude-opus-4-8-takes-the-lead-on-the-artificial-analysis-intelligence-index-57303c9c]]"
gdpval_aa_elo: 1890
gdpval_aa_elo_source: "[[claude-opus-4-8-takes-the-lead-on-the-artificial-analysis-intelligence-index-57303c9c]]"
swe_bench_verified: 0.886
swe_bench_verified_source: "[[claude-opus-4-8-takes-the-lead-on-the-artificial-analysis-intelligence-index-57303c9c]]"
cybergym: null
cybergym_source: null
arc_agi_2: null
arc_agi_2_source: null
---

## Summary

Claude Opus 4.8 is Anthropic's flagship model, released May 28, 2026 as the successor to Opus 4.7 [[introducing-claude-opus-4-8-5348a7d2]]. It is the new leader on the Artificial Analysis Intelligence Index (v4.0) at 61.4 — up 4.1 points over Opus 4.7 (57) and 1.2 points ahead of GPT-5.5 (xhigh, 60), the previous index leader [[claude-opus-4-8-takes-the-lead-on-the-artificial-analysis-intelligence-index-57303c9c]]. It also retakes GDPval-AA, Anthropic's primary agentic/knowledge-work evaluation, at 1,890 Elo — roughly 121 Elo and an implied ~67% win rate ahead of GPT-5.5, reversing the GPT-5.5 GDPval lead held since late April [[claude-opus-4-8-takes-the-lead-on-the-artificial-analysis-intelligence-index-57303c9c]]. List pricing is unchanged from Opus 4.7 at $5/$25 per Mtoken [[introducing-claude-opus-4-8-5348a7d2]].

> Claude Opus 4.8 is the new leader on the Artificial Analysis Intelligence Index with a score of 61.4, up 4.1 points from Opus 4.7 and 1.2 points ahead of GPT-5.5 (xhigh), the previous Index leader.

> Anthropic retakes the lead on GDPval-AA, their primary evaluation for agentic performance on knowledge work tasks, with Opus 4.8 scoring an 1,890 Elo, reflecting an implied win rate of approximately 67% against GPT-5.5.

On coding, Opus 4.8 scores 88.6% on SWE-bench Verified and 69.2% on the contamination-resistant SWE-bench Pro — up from 64.3% on Opus 4.7 [[claude-opus-4-8-takes-the-lead-on-the-artificial-analysis-intelligence-index-57303c9c]]. Anthropic positions it as the strongest computer-use/browser-agent model tested at 84% on Online-Mind2Web, the only model to complete every Super-Agent case end-to-end, 4x less likely than Opus 4.7 to ship code with unflagged flaws, and ships a research-preview Fast mode in Claude Code running at 2.5x speed for $30/$150 per Mtoken — roughly 3x cheaper than the prior fast tier [[introducing-claude-opus-4-8-5348a7d2]].

> Claude Opus 4.8 is the strongest computer-use and browser-agent model we have tested, scoring 84% on Online-Mind2Web, a meaningful jump over both Opus 4.7 and GPT-5.5.

> On the Super-Agent benchmark, Claude Opus 4.8 is the only model to complete every case end-to-end, beating prior Opus models and GPT-5.5 at parity on cost.

> Opus 4.8 scores 88.6% on SWE-bench Verified and 69.2% on SWE-bench Pro, up from 64.3% on Opus 4.7.

## Disputes

- [[claude-opus-4-8-takes-the-lead-on-the-artificial-analysis-intelligence-index-57303c9c]] claims Opus 4.8 is the public AA Intelligence Index #1 at 61.4; [[claude-mythos-preview-d737ab91]] claims an unreleased Anthropic model (Claude Mythos Preview) is state-of-the-art on SWE-bench Verified (93.9%) and withheld from GA. Status: unresolved — the public leaderboard #1 (Opus 4.8) is not Anthropic's true capability ceiling while Mythos remains invitation-only.

## Open questions

- [ ] What is Claude Opus 4.8's ARC-AGI-2 and CyberGym placement? Neither was published in the launch post [[introducing-claude-opus-4-8-5348a7d2]] or the AA analysis [[claude-opus-4-8-takes-the-lead-on-the-artificial-analysis-intelligence-index-57303c9c]], so both profile fields stay null pending an independent leaderboard.

## See also

- [[frontier-models]]
- [[claude-opus-4.7]]
- [[cost-comparison]]
