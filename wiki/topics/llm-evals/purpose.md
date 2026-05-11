---
title: LLM evaluation methods — purpose
kind: purpose
sources: []
last_updated: 2026-05-11
last_verified: 2026-05-11
freshness_window_days: 365
---

# LLM evaluation methods — topic charter

This file is **HUMAN-OWNED** (per the file ownership matrix in `CLAUDE.md`).
Routines never modify it. The topic-researcher reads this charter before
deciding whether to ingest any candidate source.

The synthesis page for this topic is [[llm-evals]] — that's where the
Daily Research routine accumulates findings.

## What this topic is

The methodological state of the art for **evaluating large language
models**. The wiki should accumulate, over time, an opinionated working
answer to questions like:

- Which benchmarks have known contamination or leakage problems, and
  which methods reliably detect them?
- When is LLM-as-judge trustworthy, when is it not, and what are the
  best practices for using it?
- What human-eval protocols actually replicate?
- What's the current view on agentic eval frameworks (SWE-bench-style,
  task-suite-style)?
- What's the methodological status of reward-model evaluation?
- What new evaluation methodologies have emerged that change how the
  field measures progress?

## In scope

- Benchmark design and critique (academic + industrial)
- Contamination, leakage, and memorization detection
- LLM-as-judge methodology — calibration, bias studies, agreement with
  human judgment
- Human-eval protocols (rater training, agreement metrics, cost
  tradeoffs)
- Agentic-eval frameworks (SWE-bench, METR's RE-Bench, AgentBench,
  etc.)
- Reward model evaluation methodology
- Methodology papers that materially change how the field evaluates
  models

## Out of scope

- Leaderboard score updates without methodological novelty (e.g. "model
  X scored Y on benchmark Z")
- Vendor-published "we beat GPT-4" announcements
- Subjective product reviews
- Hypothetical takes without empirical evidence
- General LLM research (training methods, model architectures) —
  those belong in `ai-agents` (if agent-relevant) or a future
  `llm-pretraining` topic

## Citation discipline reminder

Every claim added under this topic MUST be backed by a wikilink to a source page (the source-page slug appears in double square brackets) and a `>` quote from that source — see `CLAUDE.md` "Citation discipline". Off-topic ingests get rejected at proposal time.
