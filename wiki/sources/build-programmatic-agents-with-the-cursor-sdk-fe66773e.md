---
fetched_at: &id001 2026-06-06
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: fe66773ea4fde6fbefb51402986c490895939dd4c92795a30b0c4ae6079958a0
sources: []
title: Build programmatic agents with the Cursor SDK
topic: agentic-coding
url: https://cursor.com/changelog/sdk-release
---

## Excerpts

> Cursor shipped a batch of new functionality across the TypeScript and Python SDKs: the ability to choose how agent and run metadata is persisted, expose your own functions to the agent as tools, route local tool calls through auto-review, and nest subagents to any depth. Subagents can now spawn their own subagents — a reviewer subagent can delegate to a test-writer, which can delegate further, with each level keeping its own prompt and model. There's nothing to turn on; a subagent session registers the executor it needs to call Task, so nesting works automatically for any agent that defines subagents.