---
title: "Configuration Smells in AGENTS.md Files: Common Mistakes in Configuring Coding Agents"
kind: source
url: "https://arxiv.org/abs/2606.15828"
sha256: "7374633f"
fetched_at: "2026-06-23"
topic: "agentic-coding"
image_count: 0
sources: []
last_updated: 2026-06-23
last_verified: 2026-06-23
freshness_window_days: 365
---

## Excerpts

> Researchers identified six configuration smells in AGENTS.md/CLAUDE.md files via grey literature review and mining of 100 popular open-source repositories. Top smells: Lint Leakage (62% prevalence) — instructions that repeat rules linters already enforce; Context Bloat (42%) — over-specification that raises token costs and buries important instructions; Skill Leakage (35%) — loading rarely-used task-specific workflows into every session instead of isolating them in skill files. Skill Leakage and Conflicting Instructions co-occur in ways that raise the likelihood of Context Bloat.
