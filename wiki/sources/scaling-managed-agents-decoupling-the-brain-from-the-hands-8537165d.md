---
fetched_at: &id001 2026-05-22
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 8537165d23c701b725b2bce439662fb49ed4f754c559a7da693b26df6360b710
sources: []
title: 'Scaling Managed Agents: Decoupling the brain from the hands'
topic: agentic-coding
url: https://www.anthropic.com/engineering/managed-agents
---

## Excerpts

> Decoupling the brain from the hands makes each hand a tool, with a simple interface (execute(name, input) -> string) that supports any custom tool, any MCP server, and their own tools.

> The harness doesn't know whether the sandbox is a container, a phone, or a Pokemon emulator, and because no hand is coupled to any brain, brains can pass hands to one another.

> Fetched events can be transformed in the harness before being passed to Claude's context window, with transformations including context organization for prompt cache hit rate and context engineering, separated because future models may require different context management.

> Managed Agents is Anthropic's hosted service for long-horizon agent work, built around interfaces that stay stable as harnesses change, running long-horizon agents on your behalf through a small set of interfaces meant to outlast any particular implementation.