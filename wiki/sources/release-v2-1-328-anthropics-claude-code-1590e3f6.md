---
fetched_at: &id001 2026-11-19
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 1590e3f6387642d1f8fc94a639289586bce982eda9abd63a35928546a7164efc
sources: []
title: Release v2.1.328 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.328
---

## Excerpts

> Added auto mode for Claude Opus 4.6 and Sonnet 4.6 on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry and Claude apps gateway; interactive sessions with no permission mode start in it

> Added "onFailure": "block" for mcp_tool hooks, as for command and HTTP hooks: a hook whose call fails blocks the action

> Added CLAUDE_CODE_DISABLE_DEFERRED_TOOL_RESUME, which lets a host stop claude -p --resume and --continue from running a tool call that a hook deferred

> Added a warning when a message from a session that skips permission prompts may be held and dropped by a cloud session

> Fixed automatic compaction reusing the session's earlier system prompt instead of rebuilding it the way /compact does

> Fixed Code Mode losing a loaded skill, hook context or a note typed with a permission approval when resuming a session in which one reply ran several scripts

> Fixed Code Mode offering write() and edit() to read-only subagents that can't call them

> Fixed effort being turned off for a subagent's model for the session if Bedrock, Google Cloud's Agent Platform or Foundry refused its progress summary's effort setting (regression in 2.1.327)

> Self-hosted runner: Added an orchestrator metric, claude_code_self_hosted_orchestrator_sessions_given_up_total, that counts by cause how often Anthropic gave up starting a runner for a session

> Fixed Bash commands in zsh stopping with a "not found" error at a word that starts with =, such as echo ==== or [ a == b ]; =cmd no longer expands to a command's path