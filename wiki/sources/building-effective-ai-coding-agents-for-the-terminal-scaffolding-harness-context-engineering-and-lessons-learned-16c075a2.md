---
fetched_at: &id001 2026-05-26
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 16c075a2e762d042097dd5c33eed929acdd8abb047c7292fdf3ee2ed550c54cf
sources: []
title: 'Building Effective AI Coding Agents for the Terminal: Scaffolding, Harness,
  Context Engineering, and Lessons Learned'
topic: agentic-coding
url: https://arxiv.org/abs/2603.05344
---

## Excerpts

> The paper presents OPENDEV, an open-source, command-line coding agent written in Rust. It identifies three fundamental engineering challenges for long-running terminal agents: managing finite context windows over sessions exceeding token budgets, preventing destructive operations when executing arbitrary shell commands, and extending capabilities without overwhelming the agent's prompt budget. The architectural response is organized around two phases: scaffolding (which assembles the agent before the first prompt) and the harness (which orchestrates tool dispatch, context management, and safety enforcement at runtime). The Prompt Composition engine assembles the system prompt from modular sections, split into cacheable and non-cacheable segments for efficient API caching. Subagent Orchestration enables the main agent to delegate specialized tasks.