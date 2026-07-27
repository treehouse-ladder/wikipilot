---
compare_fields:
- input_cost_per_mtoken
- output_cost_per_mtoken
comparison_of:
- claude-opus-5
- claude-fable-5
- claude-opus-4.8
- claude-sonnet-4.6
- gpt-5.6-sol
- gpt-5.5
- gemini-3.1-pro
- grok-4.5
- grok-4.3
- deepseek-v4
- glm-5
- kimi-k2.6
- qwen3.7-max
- mai-code-1-flash
- minimax-m3
freshness_window_days: 30
highlight_leaders: true
kind: comparison
last_updated: 2026-07-27
last_verified: '2026-05-22'
show_glosses: true
sources:
- '[[introducing-claude-sonnet-46-c4a45eed]]'
- '[[gemini-31-pro-model-card-225ab705]]'
- '[[xai-launches-grok-43-with-improved-agentic-performance-and-lower-pricing-f1cfb522]]'
- '[[minimax-m3-api-pricing-benchmarks-openrouter-fbc88cb0]]'
title: Frontier model cost comparison
---

# Frontier model cost comparison

## Summary

This comparison aggregates `input_cost_per_mtoken, output_cost_per_mtoken` across 15 entities. Cells marked _unknown_ are missing on the source entity page; backfill the value there and re-run `wikipilot compare regen frontier-model-cost-comparison` to refresh.

## What each column means for me

- **`input_cost_per_mtoken`** — USD/Mtoken input. Lower = cheaper to feed long codebases + cached prompts to the agent.
- **`output_cost_per_mtoken`** — USD/Mtoken output. Lower = cheaper for long-running parallel-agent sessions.

| Entity | input_cost_per_mtoken | output_cost_per_mtoken |
| --- | --- | --- |
| [[claude-opus-5]] | 5.0 | 25.0 |
| [[claude-fable-5]] | 10.0 | 50.0 |
| [[claude-opus-4.8]] | 5.0 | 25.0 |
| [[claude-sonnet-4.6]] | 3.0 | 15.0 |
| [[gpt-5.6-sol]] | _unknown_ | _unknown_ |
| [[gpt-5.5]] | 5.0 | 30.0 |
| [[gemini-3.1-pro]] | 2.0 | 12.0 |
| [[grok-4.5]] | _unknown_ | _unknown_ |
| [[grok-4.3]] | 1.25 | _2.5_ |
| [[deepseek-v4]] | 1.74 | 3.48 |
| [[glm-5]] | 1.0 | 3.2 |
| [[kimi-k2.6]] | 0.95 | 4.0 |
| [[qwen3.7-max]] | 2.5 | 7.5 |
| [[mai-code-1-flash]] | _0.75_ | 4.5 |
| [[minimax-m3]] | **0.6** | **2.4** |