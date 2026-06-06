---
title: Agent Harnesses
kind: concept
sources:
  - "[[adk-arena-evaluating-agent-development-kits-via-llm-as-a-developer-cf33d068]]"
last_updated: 2026-06-06
last_verified: 2026-06-06
freshness_window_days: 30
---

# Agent Harnesses

## Summary

ADK Arena introduces 'LLM-as-a-Developer' as a measurement methodology for harness/SDK comparison: an LLM coding agent (held constant) learns each framework's API from documentation and writes + iteratively repairs agent code through a validate-and-feedback loop, letting generation effort and resulting agent test-pass rate serve as a controlled proxy for SDK usability [[adk-arena-evaluating-agent-development-kits-via-llm-as-a-developer-cf33d068]]. The framework choice — Claude Agent SDK, Cursor SDK, OpenHands SDK, LangGraph, AutoGen, CrewAI — has been a vendor-marketing variable so far; ADK Arena gives it an empirical surface.

> By holding the developer constant and varying only the framework, generation effort becomes a quantitative proxy for API usability and the resulting agents provide a controlled measure of framework effectiveness.

_no contradictions or gaps known yet (last reviewed: 2026-06-06)_

## Disputes

## Open questions

- [ ] Does LLM-as-a-Developer SDK ranking generalize across LLM developer choice (does Claude Opus 4.8-as-developer rank ADKs the same as GPT-5.5-as-developer)?

## See also

- [[agentic-coding]]
- [[harness-engineering]]
