---
fetched_at: &id001 2026-08-14
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 2308d6cf9a7da45bb08cb33e3030afaeb8af877b26eb7bbeb70d2bfb6b3bb4b2
sources: []
title: Claude Code v2.1.230 to v2.1.232 Major Updates - Sub-agent Fork Defaults and
  Cross-session Mentions
topic: agentic-coding
url: https://dev.classmethod.jp/en/articles/20260814-cc-updates-v2-1-232/
---

## Excerpts

> Subagent forking is now on by default: a subagent_type: "fork" subagent inherits the full conversation and prompt cache, and non-teammate agent spawns in interactive sessions now run in the background by default. Type @ in the prompt to mention another Claude session by name; Claude then uses SendMessage to reach that session directly.