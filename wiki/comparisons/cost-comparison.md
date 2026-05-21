---
title: "Frontier model cost comparison (May 2026)"
kind: comparison
comparison_of: ["claude-sonnet-4.6", "gemini-3.1-pro", "grok-4.3"]
compare_fields: ["input_cost_per_mtoken", "output_cost_per_mtoken"]
sources: ["[[introducing-claude-sonnet-46-c4a45eed]]", "[[gemini-31-pro-model-card-225ab705]]", "[[xai-launches-grok-43-with-improved-agentic-performance-and-lower-pricing-f1cfb522]]"]
last_updated: "2026-05-20"
last_verified: "2026-05-20"
freshness_window_days: 30
---

## Frontier model pricing snapshot (May 2026)

Prices are USD per million tokens (input / output). Cited per entity below.

| Model | Input $/Mtoken | Output $/Mtoken | Notes | Source |
|---|---|---|---|---|
| Claude Sonnet 4.6 | $3 | $15 | 1M context window (beta) | [[introducing-claude-sonnet-46-c4a45eed]] |
| Gemini 3.1 Pro Preview | $2 (≤200k) / $4 (>200k) | $12 (≤200k) / $18 (>200k) | First frontier model with context-length pricing tier | [[gemini-31-pro-model-card-225ab705]] |
| Grok 4.3 (high) | $1.25 | $2.50 | Well below reasoning-model median ($1.65/$8.00) | [[xai-launches-grok-43-with-improved-agentic-performance-and-lower-pricing-f1cfb522]] |

> Grok 4.3 (high) costs $1.25 per 1M input tokens and $2.50 per 1M output tokens.

> Pricing remains the same as Sonnet 4.5, starting at $3/$15 per million tokens.

> Input price: $2.00 for prompts <= 200k tokens, $4.00 for prompts > 200k tokens.

_no contradictions or gaps known yet (last reviewed: 2026-05-20)_

## Open questions

- [ ] Need to pin Claude Opus 4.7, GPT-5.5, Qwen3.7 Max, and DeepSeek V4-Pro per-Mtoken pricing before this comparison page can be regenerated mechanically via `wikipilot compare regen`.

## See also

- [[frontier-models]]
- [[claude-opus-4.7]]
- [[gpt-5.5]]
- [[gemini-3.1-pro]]
- [[deepseek-v4]]
