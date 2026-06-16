---
title: Parallel Subagents
kind: concept
sources:
  - "[[build-programmatic-agents-with-the-cursor-sdk-fe66773e]]"
  - "[[towards-direct-latent-space-synthesis-for-parallel-branches-in-llm-agent-workflows-726d5fa9]]"
last_updated: 2026-06-16
last_verified: 2026-06-06
freshness_window_days: 30
---

# Parallel Subagents

## Summary

Cursor's 2026-06-04 SDK release adds recursive subagent nesting: a subagent session registers the executor it needs to call Task, so subagents can spawn subagents to any depth with each level keeping its own prompt and model [[build-programmatic-agents-with-the-cursor-sdk-fe66773e]]. This puts Cursor's harness on structural parity with Claude Code's `CLAUDE_CODE_FORK_SUBAGENT` parallel-fork mechanism, but with the orchestration tree explicit in user code (TypeScript/Python SDK) rather than implicit in the agent's tool calls — useful when the orchestration graph itself needs to be tested or version-controlled.

> Subagents can now spawn their own subagents, and a reviewer subagent can delegate to a test-writer, which can delegate further, with each level keeping its own prompt and model. There's nothing to turn on; a subagent session registers the executor it needs to call Task, so nesting works automatically for any agent that defines subagents.

The merge step in parallel-subagent workflows has a measurable cost: Parallel-Synthesis observes that current systems merge fan-out branches by concatenating worker text outputs, discarding parallel structure and re-incurring prefill, and instead has the synthesizer consume the workers' KV caches directly [[towards-direct-latent-space-synthesis-for-parallel-branches-in-llm-agent-workflows-726d5fa9]]. This is a concrete attack on the "merge dominates wall-clock" caveat that makes naive parallel subagents not always faster than serial execution.

> Existing systems typically merge these branches by concatenating their textual outputs, which discards the parallel structure and incurs redundant prefill computation. We introduce Parallel-Synthesis, a plug-and-play framework that enables a synthesizer to directly consume the KV caches produced by parallel worker agents.

## Disputes

## Open questions

- [ ] Does direct KV-cache synthesis (Parallel-Synthesis) hold up when worker branches used different system prompts or models, or does it require homogeneous workers to share a cacheable prefix?

## See also

- [[agentic-coding]]
