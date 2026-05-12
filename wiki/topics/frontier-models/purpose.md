---
title: Frontier LLM landscape — purpose
kind: purpose
sources: []
last_updated: 2026-05-12
last_verified: 2026-05-12
freshness_window_days: 365
---

# Frontier models — topic charter

This file is **HUMAN-OWNED** (per the file ownership matrix in `CLAUDE.md`).
The synthesis page for this topic is [[frontier-models]].

## Cross-cutting bar (applies first)

See `CLAUDE.md` "Cross-cutting relevance criteria" for the meta-bar:
**highly relevant**, **highly innovative**, or **directly impacts/improves
agentic workflow OR video game development**. Any one suffices. Bias
toward inclusion when on the fence.

The sections below narrow that bar with topic-specific in-scope and
out-of-scope rules.

## What this topic is

The frontier-LLM landscape: which models exist, what they cost, what they
can and can't do, how their capabilities are evolving, and what the
current public benchmarks say about them.

The wiki should accumulate working answers to:

- What are the current frontier models from each major provider, and
  what are their cost/context-window/reasoning-capability profiles?
- How do they actually compare on real benchmarks (SWE-bench, GPQA,
  MMLU, ARC-AGI) — and how much should we trust each benchmark?
- Which open-weight models are competitive with closed frontier?
- Which capability axes (long-context, reasoning mode, multi-modal) are
  moving fastest?

## In scope

- Frontier model releases (Claude Opus/Sonnet, GPT-5/5.5, Gemini, Llama,
  DeepSeek, Qwen, Mistral, etc.) — capabilities, cost per Mtoken,
  context window, reasoning mode availability.
- Benchmark results that include methodology — SWE-bench, GPQA, MMLU,
  ARC-AGI, BBH, MATH; contamination analyses.
- Open-weight releases competitive with closed frontier.
- Multi-modal capabilities (vision, audio, video input/output).
- Reasoning models (o-series, Claude reasoning, DeepSeek-R variants) —
  effort/quality tradeoffs.

## Out of scope

- Training methodology in depth (architectures, loss curves, scaling
  experiments) — defer to a future `llm-pretraining` topic.
- Application-layer products (those go in `agentic-coding` or
  `ai-in-game-dev`).
- Marketing announcements without methodology — "we beat GPT-X on
  internal eval" with no public scores or methods.

## Key entities to track

Models (`wiki/entities/`):

- `claude-opus-4.7`, `claude-sonnet-4.5`
- `gpt-5`, `gpt-5.5`
- `gemini-2.5-pro`
- `deepseek-v4`
- `llama-4`, `qwen-3`, `mistral-large-3`

Providers (`wiki/entities/`):

- `anthropic`, `openai`, `google-deepmind`, `meta-ai`, `deepseek`,
  `mistral`, `xai`

## Key concepts to track

`wiki/concepts/`:

- `scaling-laws-post-chinchilla`, `mixture-of-experts`
- `reasoning-models`, `multi-modal-models`
- `post-training`, `distillation`
- `model-contamination`

## Comparison pages this topic produces

`wiki/comparisons/` — see `CLAUDE.md` "Comparison pages":

- `cost-comparison` — input/output cost per Mtoken across frontier models.
- `benchmark-comparison` — SWE-bench, GPQA, MMLU, ARC-AGI scores across
  frontier models with methodology notes.
- `context-window-comparison` — max context, per-token pricing of long
  context, retrieval/RAG behavior at the long end.
- `reasoning-mode-comparison` — which models offer reasoning, what the
  effort/quality knob looks like, what it costs.

## Counter-arguments to actively look for

The researcher MUST attempt to find at least one counter-argument or data
gap per non-trivial claim, OR add the divergence sentinel. Examples:

- "Model X is the best at coding" → look for benchmark contamination,
  prompt-format sensitivity, or a benchmark that disagrees.
- "Reasoning mode helps on Y" → look for cases where it's worse or
  no-different but more expensive.
- "Open-weight is closing the gap" → look for benchmarks where the gap
  is actually widening.

## Source quality bar

Prefer first-party model cards, technical reports, arxiv papers, and
artificialanalysis.ai (independent eval). Reject re-aggregated
"X dominates Y" posts that don't link primary numbers.

## Voice

Expert. Dense. Jargon OK. No hand-holding. Cite primary sources.

## Citation discipline reminder

Every claim MUST be backed by a wikilink to a source page (slug in double
square brackets) and a `>` quote from that source.
