---
title: Agentic coding tools and harnesses — purpose
kind: purpose
sources: []
last_updated: 2026-05-12
last_verified: 2026-05-12
freshness_window_days: 365
---

# Agentic coding — topic charter

This file is **HUMAN-OWNED** (per the file ownership matrix in `CLAUDE.md`).
Routines never modify it. The topic-researcher reads this charter alongside
`CLAUDE.md`'s "Cross-cutting relevance criteria" before deciding whether to
ingest a candidate source.

The synthesis page for this topic is [[agentic-coding]] — that's where the
Daily Research routine accumulates findings.

## Cross-cutting bar (applies first)

See `CLAUDE.md` "Cross-cutting relevance criteria" for the meta-bar:
**highly relevant**, **highly innovative**, or **directly impacts/improves
agentic workflow OR video game development**. Any one suffices. Bias toward
inclusion when on the fence — better to ingest a slightly-too-broad source
that the user can prune than to silently drop a genuinely interesting one.

The sections below narrow that bar with topic-specific in-scope and
out-of-scope rules.

## What this topic is

The state of practice and research for **agentic coding systems** — tools
where an LLM iterates with files, tests, the shell, and the developer to
deliver software changes. The wiki should accumulate working answers to:

- Which agentic IDE/CLI tools have shipped, who uses them, and how do they
  compare on parallel-subagent dispatch, prompt caching, MCP support, and
  cost?
- What loop and harness patterns have evidence behind them (vs. speculative)?
- What evaluation methodologies for coding agents have proven robust vs.
  been superseded?
- What's the current cost / latency / wall-clock-to-PR Pareto frontier?
- What sandboxing and capability stories exist for agents touching real
  systems?

## In scope

- Agentic IDE/CLI tools — Claude Code (CLI + Cloud Routines), Cursor,
  Codex, GitHub Copilot Workspace, Aider, Devin, OpenHands, SWE-agent,
  Windsurf, Cline. Architecture, evals, postmortems.
- Loops, harnesses, skills frameworks (ReAct, function calling, Anthropic
  Skills, MCP), parallel subagents (`CLAUDE_CODE_FORK_SUBAGENT`),
  prompt caching, agent-to-agent orchestration.
- Coding-specific eval harnesses: SWE-bench (and variants), METR RE-Bench,
  agent-eval reliability papers.
- Sandboxing and security for coding agents (containerized execution,
  capability restrictions, prompt-injection defenses on shell-using agents).
- Cost/latency engineering for coding agents (model routing, prompt
  caching, speculative execution, background agents).

## Out of scope

- Non-coding agents (browser/computer-use unless they're being used
  *for* coding) — those go in a future general-agents topic.
- General LLM research on architectures or training methods — those go
  in `frontier-models` (or future `llm-pretraining`).
- Marketing posts and "AGI is coming" essays without code or experiments.
- Pure UX/product writing about consumer chat assistants.

## Key entities to track

Use these as the priority entity-page seeds (the researcher creates them
under `wiki/entities/` as sources mention them):

- `claude-code`, `claude-code-cli`, `claude-code-cloud-routines`
- `cursor`, `codex`, `github-copilot`
- `aider`, `devin`, `openhands`, `swe-agent`, `windsurf`, `cline`

## Key concepts to track

Priority concept-page seeds (`wiki/concepts/`):

- `agentic-loops`, `agent-harnesses`, `agent-skills`
- `mcp-protocol`, `agent-orchestration`, `parallel-subagents`
- `prompt-caching`, `agent-sandboxing`, `computer-use`
- `background-agents`, `swe-bench`, `metr-re-bench`

## Comparison pages this topic produces

These are first-class wiki pages (Phase 9 Pattern A) under
`wiki/comparisons/`. The topic-researcher seeds them as the underlying
entities accumulate.

- `agentic-ide-comparison` — Claude Code vs Cursor vs Codex vs Aider on
  parallel-subagents, prompt caching, MCP, cost, sandbox model.
- `agent-eval-harness-comparison` — SWE-bench full vs verified vs lite vs
  RE-Bench on contamination, agent-friendliness, scoring.

## Counter-arguments to actively look for

The researcher MUST attempt to find at least one counter-argument or data
gap per non-trivial claim, OR add the literal sentinel
`_no contradictions or gaps known yet (last reviewed: <date>)_` (this is
the divergence-discipline lint, see `CLAUDE.md`). Examples for this topic:

- "Tool X is the fastest agentic IDE" → look for benchmark methodology
  flaws (was it run on the same task suite, same harness, same model?).
- "Parallel subagents always reduce wall-clock" → look for cases where
  the merge step dominates.
- "Prompt caching saves 90% on tokens" → look for cache-invalidation
  cliff cases (file edits that bust the cache mid-run).

## Source quality bar

Prefer first-party engineering writeups (Anthropic blog, Cursor changelog,
arxiv preprints, Simon Willison's deep-dives) over aggregator news.
Reject "X tops Y on benchmark Z" posts that don't cite methodology;
those are noise. Indie postmortems with concrete numbers > vendor-authored
"we beat the competition" posts.

## Voice

Expert. Dense. Jargon OK. No hand-holding. Cite primary sources.

## Citation discipline reminder

Every claim added under this topic MUST be backed by a wikilink to a source
page (the source-page slug appears in double square brackets) and a `>`
quote from that source — see `CLAUDE.md` "Citation discipline". Off-topic
ingests are rejected at proposal time; the researcher's inclusion bias
applies *within* the criteria above, never against them.
