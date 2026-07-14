---
fetched_at: &id001 2026-07-14
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 9038596b5237bca9f4738b48b0fca46ac4752ff4837a7a01775e896413ecaa98
sources: []
title: 'GameEngineBench: Evaluating Coding Agents on Real C++ Runtime Environments'
topic: ai-in-game-dev
url: https://arxiv.org/abs/2607.03525
---

## Excerpts

> GameEngineBench is a benchmark for evaluating coding agents on scoped C++ implementation tasks inside Unreal Engine 5 projects, built from nine real-world game repositories.

> The evaluation set consists of 110 tasks spanning gameplay mechanics, multiplayer behavior, AI and world orchestration, animation and movement, UI and session code, loading behavior, online-service integration, persistence, data serialization, XR behavior, and rendering-oriented plugins.

> Each task gives the model a buildable start state, scoped editable C++ files, and a behavior specification. After the model finishes, tests are injected and executed through Unreal's Play-in-Editor automation, and judge auditing determines whether the implementation satisfies the requested behavior rather than merely matching a reference solution.

> Across twelve evaluated configurations, the strongest model reaches 55.5% pass@1, while 31 tasks remain unsolved by every configuration.

> The results demonstrate that frontier coding agents continue to struggle with deeply integrated C++ development for real-time interactive software, highlighting game-engine benchmarks as a valuable complement to existing software engineering evaluations.