---
title: Agent Harnesses
kind: concept
sources:
  - "[[adk-arena-evaluating-agent-development-kits-via-llm-as-a-developer-cf33d068]]"
  - "[[lessons-from-building-claude-code-how-we-use-skills-0270e620]]"
  - "[[human-oversight-of-agentic-systems-in-practice-ab5cc8f1]]"
last_updated: 2026-06-08
last_verified: 2026-06-08
freshness_window_days: 30
---

# Agent Harnesses

## Summary

ADK Arena introduces 'LLM-as-a-Developer' as a measurement methodology for harness/SDK comparison: an LLM coding agent (held constant) learns each framework's API from documentation and writes + iteratively repairs agent code through a validate-and-feedback loop, letting generation effort and resulting agent test-pass rate serve as a controlled proxy for SDK usability [[adk-arena-evaluating-agent-development-kits-via-llm-as-a-developer-cf33d068]]. The framework choice — Claude Agent SDK, Cursor SDK, OpenHands SDK, LangGraph, AutoGen, CrewAI — has been a vendor-marketing variable so far; ADK Arena gives it an empirical surface.

> By holding the developer constant and varying only the framework, generation effort becomes a quantitative proxy for API usability and the resulting agents provide a controlled measure of framework effectiveness.

**Verification as the primary harness lever (Anthropic, June 2026).** In an internal-practice writeup, Anthropic's Claude Code team reports that across hundreds of internal Skills clustering into nine categories, **verification** is the category with the largest measurable impact on output quality [[lessons-from-building-claude-code-how-we-use-skills-0270e620]]. This is the harness-side complement to the agentic-coding-eval shift: as raw model capability saturates SWE-bench Verified, the marginal capability gain comes from harness components that catch the 'looks finished, isn't' failure mode rather than from prompt engineering. The same finding shows up empirically in oversight studies — developers using Claude Code / Cursor / Copilot agent mode spend 60–70% of their oversight effort on post-flight verification [[human-oversight-of-agentic-systems-in-practice-ab5cc8f1]] — suggesting that verification investment pays in both autonomy (less human review needed) and quality (fewer silent regressions).

> Verification skills have had the most measurable impact on Claude's output quality internally. A model can give the impression that a task is finished, and the last step — confirming the result — is exactly where work breaks down.

> Verification is the bottleneck: developers report that 60–70% of their oversight effort lands in post-flight verification because in-flight monitoring scales poorly as agents grow more capable and parallel.

_no contradictions or gaps known yet (last reviewed: 2026-06-08)_

## Disputes

## Open questions

- [ ] Does LLM-as-a-Developer SDK ranking generalize across LLM developer choice (does Claude Opus 4.8-as-developer rank ADKs the same as GPT-5.5-as-developer)?
- [ ] Is there a measurable production-grade taxonomy of verification skill *primitives* (record-and-replay, programmatic state assertions, end-to-end Playwright, etc.) and their per-task-class effectiveness, or is current practice still bespoke per codebase?

## See also

- [[agentic-coding]]
- [[harness-engineering]]
