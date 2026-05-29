---
fetched_at: &id001 2026-05-29
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: f07e441f2499617e058bf5945040ded4c110175d2a56b651afcb5b84b10e41ad
sources: []
title: 'Cutscene Agent: An LLM Agent Framework for Automated 3D Cutscene Generation'
topic: ai-in-game-dev
url: https://arxiv.org/abs/2604.25318
---

## Excerpts

> The framework makes three main contributions: (1) a Cutscene Toolkit built on the Model Context Protocol (MCP) that establishes bidirectional integration between LLM agents and the game engine, (2) a multi-agent system where a director agent orchestrates specialist subagents for animation, cinematography, and sound design with a visual reasoning feedback loop, and (3) CutsceneBench, a hierarchical evaluation benchmark for cutscene generation.

> Unlike typical tool-use benchmarks that evaluate short, isolated function calls, cutscene generation requires long-horizon, multi-step orchestration of dozens of interdependent tool invocations with strict ordering constraints.

> LLMs are weak at numerical spatial reasoning, frequently producing degenerate 3D layouts (actors facing away from conversation partners) when asked for raw coordinates, which is why the framework wraps generation in a structured toolkit and validation loop rather than emitting geometry directly.