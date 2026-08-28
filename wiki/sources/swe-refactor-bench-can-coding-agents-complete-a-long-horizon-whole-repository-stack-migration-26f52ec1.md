---
fetched_at: &id001 2026-08-28
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 26f52ec15f9065a89e15abbf946f34ac36ed48df21a1cbd11f1df8b4c21f65ee
sources: []
title: 'SWE Refactor Bench: Can Coding Agents Complete a Long-Horizon, Whole-Repository
  Stack Migration?'
topic: agentic-coding
url: https://arxiv.org/abs/2608.23564
---

## Excerpts

> Existing benchmarks cannot answer whether migrations actually occurred because they evaluate only behavioral correctness, which leads to an easy hack where agents copy the original implementation to make tests pass. We call this Blindness.

> Across 520 runs from 8 frontier models and 26 model-effort configurations, only 28 of 520 runs (5.4%) pass all three stages, 13 of the 20 tasks receive no accepted solution, and the best model (claude-opus-5) scores 47.0/100.

> Migration completeness and behavioral correctness are distinct abilities: a few runs preserve behavior by skipping the migration and are stopped at Migration Audit; most attempt it and break behavior, and are stopped at Behavioral Tests.

> The benchmark uses a three-stage protocol combining a hard migration audit with 130,118 fixed behavioral checks and agentic verification, where six independent coding agents actively search for hidden behavioral differences after submission.