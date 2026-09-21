---
fetched_at: &id001 2026-09-21
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 711c35797a55ef5d7deaabac0960bea36f73ab4bda1464600bca6c47255acb5d
sources: []
title: 'Scanning the Harness: An Empirical Study of Supply-Chain Defects in AI Coding-Agent
  Configurations'
topic: agentic-coding
url: https://arxiv.org/abs/2609.07360
---

## Excerpts

> AI coding agents such as Claude Code, Cursor, GitHub Copilot, and OpenAI Codex are configured through artifacts like instruction files, skills, hooks, MCP server declarations, and subagents.

> We study 3,171 public GitHub repositories, including 2,660 setups that assemble two or more component types and 511 published skill collections.

> 16.0% of setups carry a confirmed security defect, 0.8% have a configuration that cannot work as written, 2.4% contain a skill outside the specification, and 16.7% have a confirmed defect of either kind.

> The harness is a dependency layer installed from marketplaces and public repositories, running with the developer's privileges, with no lockfile, no install-time check, and no vocabulary for what a component may do.