---
fetched_at: &id001 2026-09-24
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 17628ac5b9c5dd288b5cdf87830a2d48bdef92500f838ecf78ff3141e75daa93
sources: []
title: 'GameLogicBench: Evaluating Coding Agents on Runtime Game Logic with Tick-Level
  State Assertions'
topic: ai-in-game-dev
url: https://arxiv.org/abs/2609.21562
---

## Excerpts

> GameLogicBench is a benchmark of 72 gameplay-logic tasks in Godot projects that can be checked with deterministic, tick-level state assertions.

> An automated evaluator checks each game's rules at every simulation tick, and across 403 hand-designed scenarios, seeded parameter variations produce 1,451 test cases.

> This is important because a game can end in a valid state even after violating its rules during the run.

> Across 20 model-scaffold configurations, the best result solves 52.78% of the task library.

> The benchmark is limited to Godot and GDScript and does not test network synchronization within its single-container harness.