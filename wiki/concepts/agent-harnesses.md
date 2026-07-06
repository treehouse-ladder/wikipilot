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
  - "[[what-makes-a-harness-a-harness-necessary-and-sufficient-conditions-for-an-agent-harness-1afa2530]]"
  - "[[bayesian-agent-posterior-guided-skill-evolution-for-llm-agent-harnesses-06be4ecd]]"
  - "[[contextbench-a-benchmark-for-context-retrieval-in-coding-agents-ae658e81]]"
  - "[[introducing-claude-sonnet-5-4307222b]]"
  - "[[claude-code-releases-v2-1-197-sonnet-5-default-and-v2-1-198-autonomous-background-agents-july-2026-867f64ca]]"
  - "[[swe-interact-reimagining-swe-benchmarks-as-user-driven-long-horizon-coding-sessions-db9da92b]]"
  - "[[swe-together-evaluating-coding-agents-in-interactive-user-sessions-aa55f80b]]"
  - "[[code-isn-t-memory-a-structural-codebase-index-inside-a-coding-agent-85bf369e]]"
last_updated: 2026-07-06
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

A June 2026 paper supplies the first constitutive definition of "agent harness," cutting through the term's polysemy (product vs. eval scaffold vs. SDK vs. orchestrator): a harness is a stateful program that wraps an LLM and determines what context the model sees at each step, and the definition is operationalized as an inclusion/exclusion test applied to Claude Code, Codex CLI, Aider, Cline, OpenHands, and SWE-agent [[what-makes-a-harness-a-harness-necessary-and-sufficient-conditions-for-an-agent-harness-1afa2530]]. This gives the wiki a load-bearing boundary line: an eval harness (the SWE-bench runner) and an orchestrator are explicitly *not* harnesses under the definition.

> A harness is a stateful program that wraps a language model and determines what context the model sees at each step.

**Self-evolving skills via Bayesian posterior tracking.** Bayesian-Agent reframes the self-evolving skills/SOPs thread by treating each reusable skill as a hypothesis about when a frozen model succeeds, maintaining a feature-conditioned posterior over verified trajectory evidence and mapping posterior state to inspectable harness actions (patch, split, compress, retire, explore) [[bayesian-agent-posterior-guided-skill-evolution-for-llm-agent-harnesses-06be4ecd]]. This is a methodological response to the SkillsBench finding that self-generated skills give no average benefit: the claim is that principled belief-tracking over verified trajectories can make self-authored skills reliable where naive heuristic reflection cannot.

> Bayesian-Agent records verified trajectory evidence, maintains a feature-conditioned categorical posterior over each skill, and maps posterior state into inspectable actions such as patch, split, compress, retire, and explore.

**The "Bitter Lesson" of coding agents: scaffolding yields marginal retrieval gains (June 2026).** ContextBench is a process-oriented context-retrieval benchmark measuring recall, precision, and efficiency across agent trajectories on 1,136 issue-resolution tasks [[contextbench-a-benchmark-for-context-retrieval-in-coding-agents-ae658e81]]. The headline finding: across four frontier LLMs and five coding agents, sophisticated agent scaffolding yields only marginal gains in context retrieval, and LLMs consistently favor recall over precision. This is process-level evidence on the model-vs-harness debate landing on the model-dominates side for the retrieval sub-task specifically, complementing the end-to-end harness≈model finding in Claw-SWE-Bench above — the scaffolding gain may surface at the downstream repair stage rather than retrieval.

> Results show that sophisticated agent scaffolding yields only marginal gains in context retrieval (The Bitter Lesson of coding agents), and LLMs consistently favor recall over precision. [[contextbench-a-benchmark-for-context-retrieval-in-coding-agents-ae658e81]]

**A structural codebase index gives measurable retrieval gains at no cost penalty (July 2026).** An ablation on SWE-PolyBench Verified and SWE-bench Pro finds that adding a structural codebase index to a coding-agent harness produces a large localization gain and a statistically separated resolve gain with no cost penalty [[code-isn-t-memory-a-structural-codebase-index-inside-a-coding-agent-85bf369e]]. The index pays off specifically when tasks involve multi-file changes where structural ranking helps. This is a concrete, configuration-controlled result that lands on the scaffolding-can-help side for the retrieval sub-task, in direct tension with ContextBench's "Bitter Lesson" — possibly reconciled if the structural-index gain is concentrated in the multi-file regime ContextBench's process-oriented retrieval eval does not isolate.

> The within-harness ablation produced a large localization gain and a statistically separated resolve gain, with no cost penalty per cell and lower cost per solve. [[code-isn-t-memory-a-structural-codebase-index-inside-a-coding-agent-85bf369e]]

**Harness autonomy escalation: Claude Code v2.1.198 ships background agents that auto-commit/push/open draft PRs (July 2026).** Claude Code's v2.1.198 release escalates background-agent autonomy defaults — background agents now commit, push, and open a draft PR when they finish code work in a worktree, instead of stopping to ask for approval [[claude-code-releases-v2-1-197-sonnet-5-default-and-v2-1-198-autonomous-background-agents-july-2026-867f64ca]]. This shifts the default oversight surface from pre-flight confirmation (approval before the agent acts on the remote) to post-flight review (a draft PR already exists, reviewers inspect after the fact). The same release escalates the built-in Explore subagent's default model from Haiku to the main session's model (capped at Opus), trading token cost for exploration quality. Both changes extend the harness-design thread this page tracks: the post-flight verification bottleneck [[human-oversight-of-agentic-systems-in-practice-ab5cc8f1]] is inherent to the autonomy/oversight Pareto frontier — moving the approval gate later in the workflow (to draft PRs) reduces friction but increases the per-review inspection burden.

> Background agents launched from `claude agents` now commit, push, and open a draft PR when they finish code work in a worktree, instead of stopping to ask. [[claude-code-releases-v2-1-197-sonnet-5-default-and-v2-1-198-autonomous-background-agents-july-2026-867f64ca]]

**Claude Sonnet 5 becomes the default harness model in Claude Code (July 2026).** Claude Code v2.1.197 switches its default model to Claude Sonnet 5, a hybrid reasoning model with a native 1M-token context window and promo pricing of $2/$10 per Mtok through August 31, 2026 (then $3/$15) [[introducing-claude-sonnet-5-4307222b]] [[claude-code-releases-v2-1-197-sonnet-5-default-and-v2-1-198-autonomous-background-agents-july-2026-867f64ca]]. For the cost-vs-quality Pareto frontier that defines harness choice [[claw-swe-bench-a-benchmark-for-evaluating-openclaw-style-agent-harnesses-on-coding-tasks-21a190b1]], this shifts the in-tool default onto a cheaper, natively-long-context tier that reduces the need for aggressive context compaction — relevant to the ContextBench finding that sophisticated retrieval scaffolding yields only marginal gains, since a larger default window may further reduce the marginal value of harness-layer retrieval strategies.

> Claude Sonnet 5 is a hybrid reasoning model with fast, capable intelligence for real-time agents and high-volume work, featuring a 1M context window. [[introducing-claude-sonnet-5-4307222b]]

**The eval frontier pivots from single-turn autonomous resolution to multi-turn interactive collaboration (July 2026).** Two independent benchmarks landing the same week — SWE-INTERACT [[swe-interact-reimagining-swe-benchmarks-as-user-driven-long-horizon-coding-sessions-db9da92b]] and SWE-Together [[swe-together-evaluating-coding-agents-in-interactive-user-sessions-aa55f80b]] — both find that strong single-turn SWE performance does not reliably transfer to multi-turn, user-driven interactive sessions. This convergence signals a measurement shift: harnesses optimized for autonomous single-shot resolution (SWE-bench Verified's bash-only mini-SWE-agent) may systematically under-represent the interactive-collaboration capability that production agentic-coding workflows demand. The harness design space must now account for feedback-driven iteration, progressive requirement revelation, and the number of corrective turns required — dimensions the single-turn eval paradigm does not capture.

> Strong performance on single-turn SWE tasks does not reliably transfer to multi-turn, user-driven workflows. [[swe-interact-reimagining-swe-benchmarks-as-user-driven-long-horizon-coding-sessions-db9da92b]]

> To evaluate agents as collaborators, we measure both final repository correctness and the number of corrective feedback turns required during the interaction. [[swe-together-evaluating-coding-agents-in-interactive-user-sessions-aa55f80b]]

## Disputes

[[lessons-from-building-claude-code-how-we-use-skills]] presents SKILL.md token-efficiency benefits as a uniform property of the skills format; [[scivisagentskills-design-and-evaluation-of-agent-skills-for-scientific-data-analysis-and-visualization-7d613ee6]] finds token-efficiency 'depends on the agent harness and tool setting' — suggesting the benefit is harness-mediated rather than format-intrinsic. Status: unresolved

## Open questions

- [ ] Does LLM-as-a-Developer SDK ranking generalize across LLM developer choice (does Claude Opus 4.8-as-developer rank ADKs the same as GPT-5.5-as-developer)?
- [ ] Is there a measurable production-grade taxonomy of verification skill *primitives* (record-and-replay, programmatic state assertions, end-to-end Playwright, etc.) and their per-task-class effectiveness, or is current practice still bespoke per codebase?

## See also

- [[agentic-coding]]
- [[harness-engineering]]
