---
fetched_at: &id001 2026-10-02
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: d320458473217aca7741df910284fb6c7490fcd5aa879bebadb2bb1e490fa0d6
sources: []
title: Release v2.1.287 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.287
---

## Excerpts

> Added Claude Mods: plugins may now modify deeper behavior.

> A mod is a plugin that changes how Claude Code looks and behaves. Mods are made of JavaScript or TypeScript event handlers: Claude Code calls one when an event happens, such as a tool call, a submitted prompt, or a part of the interface being drawn, and the handler can watch the event, change it, or take it over.

> A mod can rewrite a prompt, add new UI, replace a built-in feature, or add entirely new functionality.

> Fixed Bedrock and Vertex startup model checks ignoring an enforced availableModels list, which could collapse /model to one Opus row.

> Fixed switching between Opus 5.5 and Sonnet 5.5 rewriting earlier MCP tool announcements, which could drop earlier extended thinking.

> Fixed a dangerous rm losing its always-ask safeguard when the same command also redirected output to a ~ or wildcard path.