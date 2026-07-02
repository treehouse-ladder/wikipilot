---
fetched_at: &id001 2026-07-02
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 867f64ca41c7c01e049eea46359778908a4f6a6d71eaa9c596f5a40a9cb5f496
sources: []
title: Claude Code releases — v2.1.197 Sonnet 5 default and v2.1.198 autonomous background
  agents (July 2026)
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases
---

## Excerpts

> Introducing Claude Sonnet 5: now the default model in Claude Code, with a native 1M-token context window and promotional pricing of $2/$10 per Mtok through August 31. Update to version 2.1.197 for access. — Background agents launched from `claude agents` now commit, push, and open a draft PR when they finish code work in a worktree, instead of stopping to ask. — The built-in Explore agent now inherits the main session's model (capped at opus) instead of running on haiku. — Subagents and context compaction now inherit the session's extended thinking configuration, improving output quality on delegated tasks. — Claude in Chrome is now generally available. — Added `/dataviz` skill for chart and dashboard design guidance with a runnable color-palette validator. — Fixed brief network drops mid-response aborting the turn — transient errors like ECONNRESET now retry with backoff instead of failing. — Subagents now treat messages from the agent that launched them as normal task direction; an agent's message is still never treated as the user's approval.