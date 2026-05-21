---
fetched_at: &id001 2026-05-20
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: b77235353457c81e3b8d5fccd3aef46f77e1c1329aa75b4cc3ca2026e710e935
sources: []
title: Best practices for Claude Code (Anthropic Engineering)
topic: agentic-coding
url: https://www.anthropic.com/engineering/claude-code-best-practices
---

## Excerpts

> Subagents are defined in .claude/agents/ and run in their own context with their own set of allowed tools. An agent can spin off multiple subagents in parallel — each running different queries — and have them return only relevant excerpts rather than full data.

> You can create SKILL.md files in .claude/skills/ to give Claude domain knowledge and reusable workflows, extending Claude's knowledge with information specific to your project, team, or domain.