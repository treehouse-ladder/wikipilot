---
fetched_at: &id001 2026-10-21
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 56ee56e4f7d91a2c3b8e4f5a6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d
sources: []
title: Redesigning source control at Anthropic
topic: agentic-coding
url: https://www.anthropic.com/engineering/redesigning-source-control
---

## Excerpts

> As merges to our monorepo grew from about 2,500 to more than 30,000 a day, source control became the biggest development bottleneck. Here is how the team built Scion, an in-house version control system designed for always-online agents, and migrated off git in five months. Because nearly all of our clients are agents and jobs, Scion assumes the server is always reachable: clients fetch data on demand and keep a bounded local cache, and the server performs commits, merges, rebases, and history and blame queries that git distributes to every client. The design draws on Google's Piper and Meta's Sapling.
