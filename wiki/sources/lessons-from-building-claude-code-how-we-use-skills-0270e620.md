---
fetched_at: &id001 2026-06-08
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 0270e620d0fc2b1d341df0f69b63505508b441c180c963ac3ec72812c3d2856c
sources: []
title: 'Lessons from building Claude Code: How we use skills'
topic: agentic-coding
url: https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills
---

## Excerpts

> Skills have become one of the most used extension points in Claude Code. They're flexible, easy to make, and easy to distribute. We have hundreds of them in active use internally at Anthropic.

> We find our skills cluster into nine categories: Library & API Reference, Verification, Data & Analysis, Business Process, Scaffolding & Templates, Code Quality & Review, CI/CD & Deployment, Incident Runbooks, and Infrastructure Operations.

> Verification skills have had the most measurable impact on Claude's output quality internally. A model can give the impression that a task is finished, and the last step — confirming the result — is exactly where work breaks down.

> A common misconception is that skills are 'just markdown files'. The most interesting part is that they're folders that can include scripts, assets, data — things the agent can discover, explore, and manipulate.

> The highest-signal content in any skill is the Gotchas section. Skills with a Gotchas section measurably improve Claude's accuracy because Claude already writes code and reads codebases; restating what it would do by default only adds context without adding value. What earns its place are details that pull the model out of its default assumptions.