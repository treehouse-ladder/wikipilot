---
fetched_at: &id001 2026-05-22
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 1743f5a55252375aa75ba481b056f38b98d6836d46b8e02a97d652035c29adb6
sources: []
title: 'SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks'
topic: agentic-coding
url: https://arxiv.org/abs/2602.12670
---

## Excerpts

> Agent Skills are structured packages of procedural knowledge that augment LLM agents at inference time. SkillsBench is a benchmark of 86 tasks across 11 domains paired with curated Skills and deterministic verifiers.

> Each task is evaluated under three conditions: no Skills, curated Skills, and self-generated Skills. The researchers tested 7 agent-model configurations over 7,308 trajectories.

> Curated Skills raise average pass rate by 16.2 percentage points (pp), but effects vary widely by domain (+4.5pp for Software Engineering to +51.9pp for Healthcare) and 16 of 84 tasks show negative deltas.

> Self-generated Skills provide no benefit on average, showing that models cannot reliably author the procedural knowledge they benefit from consuming. Focused Skills with 2-3 modules outperform comprehensive documentation, and smaller models with Skills can match larger models without them.