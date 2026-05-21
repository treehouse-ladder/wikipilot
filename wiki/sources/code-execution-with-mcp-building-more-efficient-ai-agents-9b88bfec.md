---
fetched_at: &id001 2026-05-20
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 9b88bfec4a46afeb42f39164a0572a45c976260cdb46ec4a2ed6960a53e67e8f
sources: []
title: 'Code execution with MCP: building more efficient AI agents'
topic: agentic-coding
url: https://www.anthropic.com/engineering/code-execution-with-mcp
---

## Excerpts

> Code execution with MCP enables agents to use context more efficiently by loading tools on demand, filtering data before it reaches the model, and executing complex logic in a single step.

> Presenting tools as code on a filesystem allows models to read tool definitions on-demand, rather than reading them all up-front. Being able to write out a conditional tree that gets executed saves on 'time to first token' latency rather than having to wait for a model to evaluate an if-statement.