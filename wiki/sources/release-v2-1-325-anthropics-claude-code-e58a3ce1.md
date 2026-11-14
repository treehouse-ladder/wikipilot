---
fetched_at: &id001 2026-11-14
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: e58a3ce1f17ad846cacd2e2ab7abc0d4baff55f9bb76d89b44eb35823e0ff20e
sources: []
title: Release v2.1.325 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.325
---

## Excerpts

> Fixed a security issue in how zstd-compressed responses are decoded

> Fixed a gap in Bash permission checks where some compound commands could run without asking; these now ask for permission

> Fixed a case where a Bash allow rule could run a different program than the one it names

> Fixed relative deny and ask permission rules (e.g. Read(./.env)) no longer covering the project after a cd; they now also apply in added directories

> Fixed deny and ask permission rules and hooks for the Artifact tool not applying in some cloud sessions

> Fixed sandboxed commands being able to write to the native updater's download folder in some cases

> Fixed Code Mode scripts ignoring a worktree entered with EnterWorktree, writing ~ paths into the project, and leaving /mcp showing an MCP server as connected after its sign-in expired

> Fixed words typed with a Yes at a permission dialog or plan approval not reaching Claude in Code Mode

> Fixed Claude starting work by itself when you resumed a session that ended during a Code Mode script; it now waits for your next prompt

> Fixed subagents with their own model being moved to the plan-mode model when the model setting is opusplan or haiku