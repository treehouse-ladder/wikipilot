---
fetched_at: &id001 2026-05-20
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 8334be02408b27cd4257881c59b9b56fdf4a6a46e8760e49e6ce61f97481666c
sources: []
title: Subagents — OpenAI Codex (developers.openai.com)
topic: agentic-coding
url: https://developers.openai.com/codex/subagents
---

## Excerpts

> Current Codex releases enable subagent workflows by default, and subagent activity is currently surfaced in the Codex app and CLI. With subagent workflows, you can define your own custom agents with different model configurations and instructions depending on the task.

> Codex lets you define custom agents as TOML files in ~/.codex/agents/, which can have custom instructions and be assigned to use specific models.

> Codex handles orchestration across agents, including spawning new subagents, routing follow-up instructions, waiting for results, and closing agent threads. When many agents are running, Codex waits until all requested results are available, then returns a consolidated response.