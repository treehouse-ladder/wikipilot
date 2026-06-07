---
fetched_at: &id001 2026-06-07
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 5abc49c856bbb7cc12d801b2b5cb29ab59c8f2cc9c672b3f91ccb20d848ef25f
sources: []
title: 'Harness-Bench: Measuring Harness Effects across Models in Realistic Agent
  Workflows'
topic: agentic-coding
url: https://arxiv.org/abs/2605.27922
---

## Excerpts

> LLM agents are increasingly deployed as executable systems that use tools, modify workspaces, and produce concrete artifacts. In such workflows, performance depends not only on the base model, but also on the harness: the system layer that manages context, tools, state, constraints, permissions, tracing, and recovery. However, existing benchmarks typically abstract away execution, compare complete agent systems, or hold the harness fixed, making execution-layer variation difficult to study.

> We introduce Harness-Bench, a diagnostic benchmark for evaluating configuration-level harness effects in realistic agent workflows.

> Harness-Bench is focused on controlled, sandboxed offline workflows, improving reproducibility at the cost of coverage of live services, user feedback, changing external state, and long-term production memory. The authors recommend that future agent benchmarks should report both the model and the harness conditions under which a score is obtained.