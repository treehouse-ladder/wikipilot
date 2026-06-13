---
title: Agent Harnesses
kind: concept
sources:
  - "[[adk-arena-evaluating-agent-development-kits-via-llm-as-a-developer-cf33d068]]"
  - "[[lessons-from-building-claude-code-how-we-use-skills-0270e620]]"
  - "[[human-oversight-of-agentic-systems-in-practice-ab5cc8f1]]"
  - "[[copilot-sdk-is-now-generally-available-f3907ed0]]"
  - "[[shape-copilot-code-review-around-your-team-1a940a72]]"
  - "[[scivisagentskills-design-and-evaluation-of-agent-skills-for-scientific-data-analysis-and-visualization-7d613ee6]]"
  - "[[claw-swe-bench-a-benchmark-for-evaluating-openclaw-style-agent-harnesses-on-coding-tasks-21a190b1]]"
last_updated: 2026-06-13
last_verified: 2026-06-09
freshness_window_days: 30
---

# Agent Harnesses

## Summary

ADK Arena introduces 'LLM-as-a-Developer' as a measurement methodology for harness/SDK comparison: an LLM coding agent (held constant) learns each framework's API from documentation and writes + iteratively repairs agent code through a validate-and-feedback loop, letting generation effort and resulting agent test-pass rate serve as a controlled proxy for SDK usability [[adk-arena-evaluating-agent-development-kits-via-llm-as-a-developer-cf33d068]]. The framework choice — Claude Agent SDK, Cursor SDK, OpenHands SDK, LangGraph, AutoGen, CrewAI — has been a vendor-marketing variable so far; ADK Arena gives it an empirical surface.

> By holding the developer constant and varying only the framework, generation effort becomes a quantitative proxy for API usability and the resulting agents provide a controlled measure of framework effectiveness.

**Verification as the primary harness lever (Anthropic, June 2026).** In an internal-practice writeup, Anthropic's Claude Code team reports that across hundreds of internal Skills clustering into nine categories, **verification** is the category with the largest measurable impact on output quality [[lessons-from-building-claude-code-how-we-use-skills-0270e620]]. This is the harness-side complement to the agentic-coding-eval shift: as raw model capability saturates SWE-bench Verified, the marginal capability gain comes from harness components that catch the 'looks finished, isn't' failure mode rather than from prompt engineering. The same finding shows up empirically in oversight studies — developers using Claude Code / Cursor / Copilot agent mode spend 60–70% of their oversight effort on post-flight verification [[human-oversight-of-agentic-systems-in-practice-ab5cc8f1]] — suggesting that verification investment pays in both autonomy (less human review needed) and quality (fewer silent regressions).

> Verification skills have had the most measurable impact on Claude's output quality internally. A model can give the impression that a task is finished, and the last step — confirming the result — is exactly where work breaks down.

> Verification is the bottleneck: developers report that 60–70% of their oversight effort lands in post-flight verification because in-flight monitoring scales poorly as agents grow more capable and parallel.

**Cross-vendor convergence on the SDK + skills + MCP triad (June 2026).** GitHub's Copilot SDK GA (2026-06-02) exposes the underlying Copilot agent runtime as an embeddable library across six languages with first-class MCP support and OpenTelemetry tracing baked in [[copilot-sdk-is-now-generally-available-f3907ed0]]. Same-day, Copilot code review previewed `.github/skills/<name>/SKILL.md` agent-skills plus per-PR MCP server attachments [[shape-copilot-code-review-around-your-team-1a940a72]]. The pattern mirrors what Claude Code established: harness-as-product + SKILL.md as a portable extension format + MCP as the tool plane.

> The Copilot SDK gives you direct, programmatic access to the same agent runtime behind GitHub Copilot — planning, tool invocation, file edits, streaming, and multi-turn sessions, so you don't have to build your own orchestration layer.

**Skill effectiveness is harness-mediated.** A June 2026 SciVisAgentSkills evaluation on Codex and Claude Code shows that the same SKILL.md preamble can improve task scores on one harness while delivering different token-efficiency on another [[scivisagentskills-design-and-evaluation-of-agent-skills-for-scientific-data-analysis-and-visualization-7d613ee6]].

> The skills are evaluated on Codex and Claude Code using SciVisAgentBench, a benchmark of 108 expert-designed multi-step tasks. Results show that agent skills improve mean task scores across the evaluated suites, with token-efficiency benefits that depend on the agent harness and tool setting.

**Harness choice quantitatively rivals model choice (June 2026).** Claw-SWE-Bench [[claw-swe-bench-a-benchmark-for-evaluating-openclaw-style-agent-harnesses-on-coding-tasks-21a190b1]] (2026-06-13) establishes experimentally that harness choice and model choice have nearly equal impact on coding task Pass@1: 27.4 pp from harness vs. 29.4 pp from model under fixed counterparts, across 350 instances in 8 languages. This quantifies a long-suspected result — harness engineering matters as much as model capability for practical outcomes.

> Model choice changes Pass@1 by 29.4 percentage points and harness choice by 27.4 percentage points under fixed models; systems with similar accuracy can differ substantially in total API cost.

## Disputes

[[lessons-from-building-claude-code-how-we-use-skills]] presents SKILL.md token-efficiency benefits as a uniform property of the skills format; [[scivisagentskills-design-and-evaluation-of-agent-skills-for-scientific-data-analysis-and-visualization-7d613ee6]] finds token-efficiency 'depends on the agent harness and tool setting' — suggesting the benefit is harness-mediated rather than format-intrinsic. Status: unresolved

## Open questions

- [ ] Does LLM-as-a-Developer SDK ranking generalize across LLM developer choice (does Claude Opus 4.8-as-developer rank ADKs the same as GPT-5.5-as-developer)?
- [ ] Is there a measurable production-grade taxonomy of verification skill *primitives* (record-and-replay, programmatic state assertions, end-to-end Playwright, etc.) and their per-task-class effectiveness, or is current practice still bespoke per codebase?

## See also

- [[agentic-coding]]
- [[harness-engineering]]
