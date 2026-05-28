---
fetched_at: &id001 2026-05-28
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 2c281b8209f9cab55af5b1551db50638fd1ef9730210da62951b4ca4f8aa1fef
sources: []
title: How to Minimize Game Runtime Inference Costs with Coding Agents
topic: ai-in-game-dev
url: https://developer.nvidia.com/blog/how-to-minimize-game-runtime-inference-costs-with-coding-agents/
---

## Excerpts

> AI agents driven by local small language models (SLMs) can make excessive calls to the GPU. With code agents, the SLM composes new strategies at runtime from the same simple primitives.

> Once an instruction is given, the code is written, and the program doesn't touch the SLM again until a new instruction is given. A tool call chain may produce the same results, but at the cost of repeated inference calls eating into the allocated frame time slice.

> The NVIDIA In-Game Inferencing SDK 1.5 introduces a new code agent sample in which an AI agent works with the player to defeat monsters in a 2D dungeon.