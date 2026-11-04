---
fetched_at: &id001 2026-11-04
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: fbfedaa618aab83de97c316224d853d433fb17521a388aa372165e1391d040f0
sources: []
title: Release v2.1.314 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
---

## Excerpts

> Added permissions.blockWritesOutsideWorkingDirectories so that Write, Edit and NotebookEdit refuse paths outside the working directories in every permission mode, even in bypass mode

> Idle compaction in VS Code and Claude Desktop's Code tab: a 200K+ token conversation left idle is summarized, and the summary is used on your next message if the prompt cache has expired. It now also runs on Bedrock, Vertex, Foundry and gateways once the 1h cache is on