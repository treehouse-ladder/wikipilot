---
freshness_window_days: 365
kind: purpose
last_updated: 2026-05-11
last_verified: 2026-05-11
sources: []
title: AI agents and agentic systems — purpose
---

# AI agents — topic charter

This file is **HUMAN-OWNED** (per the file ownership matrix in `CLAUDE.md`).
Routines never modify it. The topic-researcher reads this charter before
deciding whether to ingest any candidate source.

The synthesis page for this topic is [[ai-agents]] — that's where the
Daily Research routine accumulates findings.

## What this topic is

The state of practice and research for **autonomous LLM agents** —
systems where an LLM iterates with tools, files, the web, or other
agents to accomplish multi-step tasks without per-step human direction.

The wiki should accumulate, over time, a working answer to questions
like:

- Which agentic frameworks have shipped, who uses them, and how do they
  compare on which axes?
- What evaluation methodologies for agents have proven robust vs. been
  superseded?
- What multi-agent orchestration patterns have evidence behind them
  (and which are speculative)?
- What's the current cost / latency Pareto frontier for agentic tasks?
- What sandboxing / security stories exist for agents that touch real
  systems?
- What open problems are blocking agents from compounding into reliable
  workflows?

## In scope

- Agentic frameworks (Claude Code, Codex, Cursor, OpenAI Assistants,
  AutoGen, LangGraph, CrewAI, etc.) — architecture, evals, post-mortems
- Evaluation methodologies for agents (SWE-bench-style harnesses,
  agent-eval reliability)
- Multi-agent orchestration (parallel subagents, hierarchical agents,
  cache sharing, prompt routing)
- Tool-use patterns and skills frameworks (ReAct, function calling,
  Anthropic Skills, MCP, etc.)
- Cost/latency engineering for agents (model routing, prompt caching,
  speculative execution)
- Sandboxing and security (containerized execution, capability
  restrictions, prompt-injection defenses)

## Out of scope

- General LLM research (model architectures, training methods,
  benchmarks for non-agentic tasks) — those belong in `llm-evals` or a
  future `llm-pretraining` topic
- Generic industry news or product launches that don't ship technical
  detail
- Marketing posts and "AGI is coming" essays without code or
  experiments
- Pure UX/product writing about consumer chat assistants

## Citation discipline reminder

Every claim added under this topic MUST be backed by a wikilink to a source page (the source-page slug appears in double square brackets) and a `>` quote from that source — see `CLAUDE.md` "Citation discipline". Off-topic ingests get rejected at proposal time.