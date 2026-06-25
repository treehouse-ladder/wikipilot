---
title: Parallel Subagents
kind: concept
sources:
  - "[[build-programmatic-agents-with-the-cursor-sdk-fe66773e]]"
  - "[[towards-direct-latent-space-synthesis-for-parallel-branches-in-llm-agent-workflows-726d5fa9]]"
  - "[[cloud-environment-setup-and-cloud-subagents-in-agents-window-ac3775dd]]"
  - "[[customize-cursor-16819559]]"
  - "[[configuration-smells-in-agents-md-files-common-mistakes-in-configuring-coding-agents-7374633f]]"
last_updated: 2026-06-25
last_verified: 2026-06-06
freshness_window_days: 30
---

# Parallel Subagents

## Summary

Cursor's 2026-06-04 SDK release adds recursive subagent nesting: a subagent session registers the executor it needs to call Task, so subagents can spawn subagents to any depth with each level keeping its own prompt and model [[build-programmatic-agents-with-the-cursor-sdk-fe66773e]]. This puts Cursor's harness on structural parity with Claude Code's `CLAUDE_CODE_FORK_SUBAGENT` parallel-fork mechanism, but with the orchestration tree explicit in user code (TypeScript/Python SDK) rather than implicit in the agent's tool calls — useful when the orchestration graph itself needs to be tested or version-controlled.

> Subagents can now spawn their own subagents, and a reviewer subagent can delegate to a test-writer, which can delegate further, with each level keeping its own prompt and model. There's nothing to turn on; a subagent session registers the executor it needs to call Task, so nesting works automatically for any agent that defines subagents.

The merge step in parallel-subagent workflows has a measurable cost: Parallel-Synthesis observes that current systems merge fan-out branches by concatenating worker text outputs, discarding parallel structure and re-incurring prefill, and instead has the synthesizer consume the workers' KV caches directly [[towards-direct-latent-space-synthesis-for-parallel-branches-in-llm-agent-workflows-726d5fa9]]. This is a concrete attack on the "merge dominates wall-clock" caveat that makes naive parallel subagents not always faster than serial execution.

> Existing systems typically merge these branches by concatenating their textual outputs, which discards the parallel structure and incurs redundant prefill computation. We introduce Parallel-Synthesis, a plug-and-play framework that enables a synthesizer to directly consume the KV caches produced by parallel worker agents.

Cursor's June 2026 `/in-cloud` update pushes the isolation boundary from worktree-per-subagent to full cloud VM per subagent: a cloud subagent runs on its own VM and branch, keeping long-running or parallel work (CI fixes, issue investigation, codebase exploration) off the local machine while the workspace stays responsive [[cloud-environment-setup-and-cloud-subagents-in-agents-window-ac3775dd]]. Cloud environment setup completes in under ten minutes and is captured in reusable snapshots for faster subsequent starts. This extends the worktree-isolation mental model (Cursor 2.0, nested subagents) to a full per-subagent VM isolation boundary — structurally heavier but with stronger blast-radius containment for parallel work.

> You can use /in-cloud to spin up a cloud subagent in its own VM to work on the next task you submit. It runs on its own VM and branch, so your local workspace stays clean and responsive. This is especially useful for isolating long-running or parallel work like fixing CI, investigating an issue, or exploring a codebase while you keep working locally.

**Team-wide skill/MCP distribution for parallel-subagent contexts.** Cursor 3.9's Customize page consolidates plugins, skills, MCPs, subagents, rules, commands, and hooks into one place manageable at user/team/workspace scope, with a popularity leaderboard and one-click install across a team [[customize-cursor-16819559]]. This operationalizes the configuration-distribution layer for parallel-subagent workflows: when every team member can spawn subagents with shared skills/MCPs via the leaderboard, curation becomes an organizational asset rather than per-developer config drift — the failure mode catalogued as Skill Leakage (35% prevalence) in the AGENTS.md configuration-smells study [[configuration-smells-in-agents-md-files-common-mistakes-in-configuring-coding-agents-7374633f]].

> You can now add and manage plugins, skills, MCPs, subagents, rules, commands, and hooks at the user, team, or workspace level, and even bring your own custom MCPs. Cursor now shows you a leaderboard of the most popular plugins, skills, and MCPs across your team. [[customize-cursor-16819559]]

## Disputes

## Open questions

- [ ] Does direct KV-cache synthesis (Parallel-Synthesis) hold up when worker branches used different system prompts or models, or does it require homogeneous workers to share a cacheable prefix?

## See also

- [[agentic-coding]]
