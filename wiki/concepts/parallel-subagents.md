---
title: Parallel Subagents
kind: concept
sources:
  - "[[build-programmatic-agents-with-the-cursor-sdk-fe66773e]]"
last_updated: 2026-06-06
last_verified: 2026-06-06
freshness_window_days: 30
---

# Parallel Subagents

## Summary

Cursor's 2026-06-04 SDK release adds recursive subagent nesting: a subagent session registers the executor it needs to call Task, so subagents can spawn subagents to any depth with each level keeping its own prompt and model [[build-programmatic-agents-with-the-cursor-sdk-fe66773e]]. This puts Cursor's harness on structural parity with Claude Code's `CLAUDE_CODE_FORK_SUBAGENT` parallel-fork mechanism, but with the orchestration tree explicit in user code (TypeScript/Python SDK) rather than implicit in the agent's tool calls — useful when the orchestration graph itself needs to be tested or version-controlled.

> Subagents can now spawn their own subagents, and a reviewer subagent can delegate to a test-writer, which can delegate further, with each level keeping its own prompt and model. There's nothing to turn on; a subagent session registers the executor it needs to call Task, so nesting works automatically for any agent that defines subagents.

## Disputes

## Open questions

## See also

- [[agentic-coding]]
