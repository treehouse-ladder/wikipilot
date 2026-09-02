---
title: "Claude Fable 5.1"
kind: entity
aliases: ["Fable 5.1", "fable-5.1", "Claude Fable 5.1"]
sources: ["[[introducing-claude-fable-5-1-and-claude-mythos-5-1-e7232d52]]", "[[claude-fable-5-1-tops-the-artificial-analysis-intelligence-index-88ebeee8]]"]
last_updated: 2026-09-02
last_verified: 2026-09-02
freshness_window_days: 30
---

## Summary

Claude Fable 5.1 is Anthropic's flagship Mythos-class model, shipped **September 1, 2026** alongside Claude Mythos 5.1 — the two are the **same underlying model with different safeguard levels**: Fable 5.1 is generally available (day-one across the Claude API, AWS, Google Cloud and Microsoft Foundry), while [[claude-mythos]] 5.1 is restricted to Anthropic's trusted-access programs for cybersecurity and life-sciences work [[introducing-claude-fable-5-1-and-claude-mythos-5-1-e7232d52]]. It supersedes [[claude-fable-5]] and is positioned as 'a new standard for coding, knowledge work, and long-running problem-solving tasks' [[introducing-claude-fable-5-1-and-claude-mythos-5-1-e7232d52]].

> Claude Fable 5.1 and Claude Mythos 5.1 are the same model, but with different levels of safeguards. Fable 5.1 is generally available, while Mythos 5.1 is available only through our trusted access programs; its safeguards are specifically designed to support work in cybersecurity and the life sciences. [[introducing-claude-fable-5-1-and-claude-mythos-5-1-e7232d52]]

**Intelligence.** Artificial Analysis places Fable 5.1 (max) at **66 on the AA Intelligence Index — the highest score ever measured (#1)**, a +4 gain over Fable 5, ahead of [[claude-opus-5]] (max, 63), Fable 5 (max, 62), [[gpt-5.6-sol]] (max, 61) and [[grok-4.6]] (high, 61) [[claude-fable-5-1-tops-the-artificial-analysis-intelligence-index-88ebeee8]]. Its five effort settings span **58→66** across an 11× output-token range (13.1M at low → 143.7M at max) [[claude-fable-5-1-tops-the-artificial-analysis-intelligence-index-88ebeee8]]. It leads **GDPval-AA v2 at 1,853 Elo** (over Opus 5's 1,824, confidence intervals overlapping) and posts the narrowly-highest **Terminal-Bench v2.1 (91.4%)**, **SciCode (62.0%)** and **HLE (59.1%, vs Fable 5's 55.5%)**, plus +9 on τ³-Banking over Fable 5 [[claude-fable-5-1-tops-the-artificial-analysis-intelligence-index-88ebeee8]].

> Claude Fable 5.1 at max effort scores 66 on the Artificial Analysis Intelligence Index, the highest score measured, ahead of Claude Opus 5 (max, 63), Claude Fable 5 (max, 62), GPT-5.6 Sol (max, 61) and Grok 4.6 (high, 61). [[claude-fable-5-1-tops-the-artificial-analysis-intelligence-index-88ebeee8]]

> On HLE, Fable 5.1 scores 59.1%, ahead of the previous best of 55.5% from Claude Fable 5. It posts the narrowly highest scores on Terminal-Bench v2.1 (91.4%) and SciCode (62.0%), and on τ³-Banking it gains 9 points over Fable 5. [[claude-fable-5-1-tops-the-artificial-analysis-intelligence-index-88ebeee8]]

**Pricing and specs.** List price is unchanged from Fable 5 at **$10/$50 per Mtoken**, but cache reads are cut 75% to **$0.25/Mtok** (from $1), which Anthropic estimates lowers typical-workload cost ~25% and highly-agentic-workload cost up to ~45% [[introducing-claude-fable-5-1-and-claude-mythos-5-1-e7232d52]]. It keeps a **1M-token context**, **128K max output tokens**, and **always-on adaptive thinking** [[introducing-claude-fable-5-1-and-claude-mythos-5-1-e7232d52]]. Despite the cache cut, at max effort Fable 5.1 costs **$3.76 per Intelligence Index task — 20% more than Fable 5 ($3.14) and 1.6× Opus 5 ($2.34)** — driven by ~1.7× Fable 5's output tokens, so [[claude-opus-5]] remains the cost-per-task value leader at the top of the board [[claude-fable-5-1-tops-the-artificial-analysis-intelligence-index-88ebeee8]].

> Fable 5.1 will cost an estimated 25% less than Fable 5 for typical workloads. Cache reads now cost $0.25 per million tokens, 75% less than Fable 5, which reduces the cost of typical workloads by an estimated 25% and highly agentic workloads by up to approximately 45%. Fable 5.1's pricing is otherwise the same as Fable 5's: $10 per million input tokens and $50 per million output tokens. [[introducing-claude-fable-5-1-and-claude-mythos-5-1-e7232d52]]

> Claude Fable 5.1 (max) costs $3.76 per Intelligence Index task, 20% more than Claude Fable 5 (max) at $3.14 and 1.6x Claude Opus 5 (max) at $2.34, driven by ~1.7x the output tokens of Fable 5. [[claude-fable-5-1-tops-the-artificial-analysis-intelligence-index-88ebeee8]]

**Safeguards.** Fable 5.1's newest cybersecurity safeguards block 60% fewer false positives than Fable 5, and Fable 5.1 can now be used to discover software vulnerabilities (defensive security work) — though not to develop exploits for them [[introducing-claude-fable-5-1-and-claude-mythos-5-1-e7232d52]].

> In cybersecurity, our newest safeguards block 60% fewer false positives than before. Fable 5.1 can now be used to discover software vulnerabilities—though not to develop exploits for them. [[introducing-claude-fable-5-1-and-claude-mythos-5-1-e7232d52]]

_no contradictions or gaps known yet (last reviewed: 2026-09-02)_

## Disputes

## Open questions

- [ ] Fable 5.1's GDPval-AA v2 lead over Opus 5 (1,853 vs 1,824) has overlapping confidence intervals [[claude-fable-5-1-tops-the-artificial-analysis-intelligence-index-88ebeee8]] — is the lead statistically meaningful?
- [ ] Fable 5.1's SWE-bench Pro (contamination-resistant coding) score was not reported at launch — does it hold Fable 5's 80.0% long-horizon-coding lead?

## See also

- [[frontier-models]]
- [[claude-fable-5]]
- [[claude-opus-5]]
- [[claude-mythos]]
