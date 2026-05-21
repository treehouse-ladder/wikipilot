---
fetched_at: &id001 2026-05-21
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 3262892cb3f5021f06a7bf661e4a817c10171c15dc846d89785481d0acf8d4bf
sources: []
title: "Subagents — Agentic Engineering Patterns"
topic: agentic-coding
url: https://simonwillison.net/guides/agentic-engineering-patterns/subagents/
---

## Excerpts

> When a coding agent uses a subagent it effectively dispatches a fresh copy of itself to achieve a specified goal, with a new context window that starts with a fresh prompt.

> The principle advantage of this kind of subagent is that it can work with a fresh context in a way that avoids spending tokens from the parent's available limit.

> Subagents can provide a significant performance boost by having the parent agent run multiple subagents at the same time, potentially also using faster and cheaper models such as Claude Haiku to accelerate those tasks.

> While it can be tempting to go overboard breaking up tasks across dozens of different specialist subagents, it's important to remember that the main value of subagents is in preserving that valuable root context and managing token-heavy operations.
