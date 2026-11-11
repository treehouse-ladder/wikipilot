---
title: "Claude Fable 5.2"
kind: entity
aliases: ["Fable 5.2", "fable-5.2", "Claude Fable 5.2", "Claude Mythos 5.2", "Mythos 5.2"]
sources:
  - "[[introducing-claude-fable-5-2-and-claude-mythos-5-2-a989f158]]"
  - "[[claude-fable-5-2-max-intelligence-performance-price-analysis-fbdf36c6]]"
last_updated: 2026-11-11
last_verified: 2026-11-11
freshness_window_days: 30
---

## Summary

Claude Fable 5.2 is Anthropic's flagship Mythos-class model, shipped **2026-11-11** alongside Claude Mythos 5.2 — the two are the **same underlying model** at different safeguard levels: Fable 5.2 is generally available, while Mythos 5.2 is restricted to trusted-access programs [[introducing-claude-fable-5-2-and-claude-mythos-5-2-a989f158]]. It supersedes [[claude-fable-5.1]].

> Claude Fable 5.2 and Claude Mythos 5.2 are the same underlying model. Mythos 5.2 is available only through our trusted access programs. [[introducing-claude-fable-5-2-and-claude-mythos-5-2-a989f158]]

**Intelligence.** Artificial Analysis places Fable 5.2 (max, Default Fallback) at **65 on the Artificial Analysis Intelligence Index v5.0.1 — the highest score measured, #1 out of 104 models evaluated**, ahead of the prior leader Gemini 4 Carbon (59) [[claude-fable-5-2-max-intelligence-performance-price-analysis-fbdf36c6]]. Effort-level scores span **54→65**: max 65, xhigh 62, high 62, medium 56, low 54. Cost per Intelligence Index task at max is **$26.54**, and time per task is **44.4 minutes** (notably slow vs. the median 12.7 minutes) [[claude-fable-5-2-max-intelligence-performance-price-analysis-fbdf36c6]].

> Claude Fable 5.2 (max, Default Fallback) leads the Artificial Analysis Intelligence Index with a score of 65, out of 104 models evaluated. [[claude-fable-5-2-max-intelligence-performance-price-analysis-fbdf36c6]]

> Claude Fable 5.2 (max) cost per Intelligence Index task is $26.54. It takes 44.4 minutes per Intelligence Index task, notably slow compared with the median of 12.7 minutes. [[claude-fable-5-2-max-intelligence-performance-price-analysis-fbdf36c6]]

**Specialty benchmarks.** Fable 5.2 posts decisive leads on new axes where Fable 5.1 and Opus 5.5 had not been tested: **FrontierCode 2.0 (xhigh): 49.1%** — the highest score of any released model tested; **BenchCAD 2.1 (max): 83.5**, ahead of Opus 5.5 (65.3) and Fable 5.1 (44.4); **RoboDojo Sim (max): 64.9%**, more than double GPT-6 Astra (29.8%) and Fable 5.1 (27.6%) [[introducing-claude-fable-5-2-and-claude-mythos-5-2-a989f158]].

> On FrontierCode 2.0 at Xhigh effort, Fable 5.2 reaches 49.1%, the highest score of any released model we've tested. At High effort it roughly matches Opus 5.5's best score at about half the cost per task. [[introducing-claude-fable-5-2-and-claude-mythos-5-2-a989f158]]

> On BenchCAD 2.1 at Max effort, Fable 5.2 scores 83.5, ahead of Opus 5.5 (65.3) and Fable 5.1 (44.4). [[introducing-claude-fable-5-2-and-claude-mythos-5-2-a989f158]]

> On RoboDojo Sim at Max effort, Fable 5.2 scores 64.9%, more than double GPT-6 Astra (29.8%) and Fable 5.1 (27.6%). [[introducing-claude-fable-5-2-and-claude-mythos-5-2-a989f158]]

**Pricing.** List price is **$8/$40 per Mtoken** — a 20% cut from Fable 5.1 ($10/$50). Fast mode runs up to 2.5× faster at **$16/$80 per Mtoken**. Cache reads: **$0.20 per Mtoken**. US-only inference available at 1.1× input/output pricing [[introducing-claude-fable-5-2-and-claude-mythos-5-2-a989f158]].

> Claude Fable 5.2 is priced at $8 per million input tokens and $40 per million output tokens, down from $10 and $50 for Fable 5.1. [[introducing-claude-fable-5-2-and-claude-mythos-5-2-a989f158]]

> Fast mode runs up to 2.5x faster. It costs $16 per million input tokens and $80 per million output tokens. [[introducing-claude-fable-5-2-and-claude-mythos-5-2-a989f158]]

**Recommended use.** Anthropic explicitly recommends **[[claude-opus-5.5]] for most workloads**, positioning Fable 5.2 for tasks that require the absolute maximum intelligence ceiling [[introducing-claude-fable-5-2-and-claude-mythos-5-2-a989f158]].

> If you're unsure which model to use, start with Claude Opus 5.5 for most workloads. [[introducing-claude-fable-5-2-and-claude-mythos-5-2-a989f158]]

## Disputes

_none_

## Open questions

- [ ] No independent AA Coding Agent Index placement for Fable 5.2 as of 2026-11-11 — does it displace Fable 5.1 / GPT-6 Astra from the coding co-leadership?
- [ ] FrontierCode 2.0 score of 49.1% (xhigh) is vendor-reported; independent AA FrontierCode placement not yet confirmed.
- [ ] cybergym and arc_agi_2 scores not yet published.

## See also

- [[claude-fable-5.1]]
- [[claude-opus-5.5]]
- [[frontier-models]]
- [[benchmark-leaders]]
- [[cost-comparison]]

_no contradictions or gaps known yet (last reviewed: 2026-11-11)_
