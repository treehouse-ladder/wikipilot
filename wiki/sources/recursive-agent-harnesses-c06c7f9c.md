---
fetched_at: &id001 2026-06-22
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: c06c7f9c2f8e03e73dc79b4bf1fdd712ef56fc4f15e6089eb72e34f9121660c0
sources: []
title: Recursive Agent Harnesses
topic: agentic-coding
url: https://arxiv.org/abs/2606.13643
---

## Excerpts

> We study a recursive unit as a full agent harness with filesystem tools, code execution, and planning rather than a model call with no tools, framing it as harness recursion, the code-first extension to the model recursion of RLMs.

> A parent agent generates and runs an executable script that spawns subagent harnesses in parallel for fine-grained workloads and uses structured function calls for small subtasks. A parent agent selects between code-execution spawning (writing an executable script that spawns subagents in parallel) and JSON tool-call spawning (for 1–5 entries), with subagents carrying the same spawning capability as their parent, enabling recursive decomposition bounded by a configurable depth limit.

> With the backbone held fixed at GPT-5 to match the published Codex and RLM baselines, RAH improves the Codex coding-agent baseline from 71.75% to 81.36%.

> Sub-agent handoffs keep per-step cost low by giving the sub-agent a narrow specialized context. The sub-agent token usage sits about an order of magnitude below orchestrator tokens.