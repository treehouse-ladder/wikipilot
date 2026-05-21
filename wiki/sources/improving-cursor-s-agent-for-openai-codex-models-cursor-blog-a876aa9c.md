---
fetched_at: &id001 2026-05-21
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: a876aa9c710fa36f835f1a733ae15ddee0ddf0843c91096da3649683a6e3e39d
sources: []
title: Improving Cursor's agent for OpenAI Codex models (Cursor blog)
topic: agentic-coding
url: https://cursor.com/blog/codex-model-harness
---

## Excerpts

> Every model in Cursor's agent harness has specific instructions and tools made available to optimize that model inside the Cursor environment. To encourage tool calling, they made the names and definitions of tools in Cursor closer to their shell equivalents like rg (ripgrep). Codex benefits significantly from clear and literal instructions for when to call the read_lints tool, rather than just providing the tool definition alone. OpenAI's reasoning models emit internal reasoning traces between tool calls as a chain of thought, and the Responses API is designed to capture these reasoning items so the model can maintain continuity across turns.