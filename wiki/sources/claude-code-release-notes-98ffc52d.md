---
fetched_at: &id001 2026-08-03
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 98ffc52d602549ffa0cac22654af0c4e92bc96e8d3dfb9862320b400bc44c33c
sources: []
title: Claude Code release notes
topic: agentic-coding
url: https://docs.anthropic.com/en/release-notes/claude-code
---

## Excerpts

> Changed dynamic workflows to default to a medium size guideline (aim for fewer than 15 agents), and removed Opus 4.7 from fast mode so /fast now applies to Opus 5 and Opus 4.8.

> The CLI (version 1.16.0) now sends agent-memory-2026-07-22 on all memory store calls instead of managed-agents-2026-04-01. Fixed auto-compact never triggering for Claude Opus 4.8 on Bedrock. Fixed Windows auto-update failures that could leave claude.exe missing; failed updates now restore the preserved executable automatically.