---
fetched_at: &id001 2026-07-16
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: a86fc2af5a47622a7d683d4bee5ba54a768ec26525c5ee8e94eb22d4cb111016
sources: []
title: 'PlayCoder: Making LLM-Generated GUI Code Playable'
topic: ai-in-game-dev
url: https://arxiv.org/abs/2604.19742
---

## Excerpts

> Large language models have achieved strong results in code generation, but their ability to generate GUI applications, especially games, remains insufficiently studied. Existing benchmarks mainly evaluate correctness through test cases, which are inadequate for GUI applications because these systems are interactive, event-driven, and require correct state transitions across sequences of user actions.

> We introduce PlayEval, a repository-aware benchmark built from 43 multilingual GUI applications in Python, TypeScript, and JavaScript, together with the Play@k metric and a PlayTester agent that performs task-oriented GUI playthroughs and detects logic violations automatically.

> PlayCoder is a multi-agent, repository-aware framework that generates, evaluates, and iteratively repairs GUI application code in a closed loop.

> Experiments on 10 state-of-the-art code LLMs show that, despite high compilation rates, they achieve near-zero Play@3, revealing major weaknesses in generating logically correct GUI applications.