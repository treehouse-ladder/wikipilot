---
title: "Claude Opus 4.7"
kind: entity
sources: ["[[introducing-claude-opus-47-b8af8104]]", "[[claude-opus-47-everything-you-need-to-know-751c1827]]", "[[swe-chain-benchmarking-coding-agents-on-chained-release-level-package-upgrades-26980c45]]", "[[building-a-c-compiler-with-a-team-of-parallel-claudes-1eba12a4]]"]
last_updated: "2026-05-22"
last_verified: "2026-05-22"
freshness_window_days: 30
---

## Summary

Claude Opus 4.7 is Anthropic's flagship model released April 16, 2026 [[introducing-claude-opus-47-b8af8104]]. It scores 57 on the Artificial Analysis Intelligence Index in Adaptive Reasoning Max Effort mode (a 4-point uplift over Opus 4.6) and is the leader on GDPval-AA at 1,753 Elo, ~79 Elo points ahead of the next-tier models [[claude-opus-47-everything-you-need-to-know-751c1827]]. On Anthropic's 93-task internal coding benchmark, Opus 4.7 lifted resolution by 13% over Opus 4.6. Despite being more capable, Opus 4.7 (Adaptive Reasoning, Max Effort) costs ~$4,406 to run the Intelligence Index, ~11% less than Opus 4.6 (~$4,970). It ranks #2 on the AA Omniscience Index (behind Gemini 3.1 Pro), with the improvement coming primarily from reduced hallucination rather than higher accuracy.

> Claude Opus 4.7 is our most intelligent model, with state-of-the-art performance on coding, agentic tasks, and reasoning.

> Opus 4.7 is the new leader on GDPval-AA, scoring 1,753 Elo, around 79 Elo points ahead of the next closest models.

On multi-step package upgrades, Claude Opus 4.7 (Claude Code) scores 60.8% resolving, 80.6% precision, and 68.5% F1 on SWE-Chain, which measures chained release-level upgrades where each transition builds on the agent's prior codebase [[swe-chain-benchmarking-coding-agents-on-chained-release-level-package-upgrades-26980c45]]. The C compiler parallel-agents case study ran on Opus 4.7 (then referred to as Claude Code) across "nearly 2,000 Claude Code sessions and $20,000 in API costs" producing a 100,000-line compiler consuming "2 billion input tokens and 140 million output tokens across two weeks" [[building-a-c-compiler-with-a-team-of-parallel-claudes-1eba12a4]].

> SWE-Chain contains 12 upgrade chains across 9 real Python packages, with 155 version transitions and 1,660 grounded upgrade requirements, where each transition builds on the agent's prior codebase. Claude-Opus-4.7 (Claude Code) leads at 60.8% resolving, 80.6% precision, and 68.5% F1.

> Over nearly 2,000 Claude Code sessions and $20,000 in API costs, the agent team produced a 100,000-line compiler that can build Linux 6.9 on x86, ARM, and RISC-V. The project consumed 2 billion input tokens and 140 million output tokens across two weeks.

_no contradictions or gaps known yet (last reviewed: 2026-05-22)_

## Open questions

- [ ] What are Opus 4.7's SWE-bench Pro and ARC-AGI-2 scores? The launch materials emphasize coding and GDPval-AA but the contamination-sensitive frontier benchmarks aren't called out.
- [ ] How does Claude-Opus-4.7's 60.8% on SWE-Chain [[swe-chain-benchmarking-coding-agents-on-chained-release-level-package-upgrades-26980c45]] degrade across the chain length — is the per-transition success rate roughly constant, or does error accumulate so that long chains collapse?

## See also

- [[frontier-models]]
- [[gpt-5.5]]
- [[gemini-3.1-pro]]
