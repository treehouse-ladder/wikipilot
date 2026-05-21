---
fetched_at: &id001 2026-05-20
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 7f7a70a6764975801eea23bab1b78e6c353c5ce311b10461d278849bb098ac5d
sources: []
title: Effective harnesses for long-running agents (Anthropic Engineering)
topic: agentic-coding
url: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
---

## Excerpts

> The core challenge of long-running agents is that they must work in discrete sessions, and each new session begins with no memory of what came before. Because context windows are limited, and because most complex projects cannot be completed within a single window, agents need a way to bridge the gap between coding sessions.

> We developed a two-fold solution to enable the Claude Agent SDK to work effectively across many context windows: an initializer agent that sets up the environment on the first run, and a coding agent that is tasked with making incremental progress in every session, while leaving clear artifacts for the next session.