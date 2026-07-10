---
fetched_at: &id001 2026-07-10
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: c21acdb9bc98b95bdf5041d5928fa93fa303ffbb6e171268c64af4837e9a75f1
sources: []
title: Programmatic Tool Calling
topic: agentic-coding
url: https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling
---

## Excerpts

> Programmatic Tool Calling lets a model write and run JavaScript that coordinates the tools in a Responses API request.

> A program can call tools in parallel, use loops and conditions, and keep intermediate results in the hosted runtime. This is useful when a task needs a sequence of related tool calls or needs to process large tool outputs before returning a result.

> OpenAI runs each generated program in a fresh, isolated V8 runtime. The runtime supports JavaScript with top-level await, but it does not provide Node.js, package installation, direct network access, a general-purpose filesystem, subprocess execution, a console, or persistent JavaScript state.