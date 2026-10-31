---
title: "Suno"
kind: entity
aliases: ["Suno AI", "Suno music"]
sources:
  - "[[suno-mcp-beta-fbbc54a2]]"
last_updated: 2026-10-31
last_verified: 2026-10-31
freshness_window_days: 30
profile: tool
modality: music
tasks: ["text-to-music", "audio-to-music", "remix", "extension"]
vendor: "Suno"
model_ids: []
access: ["api"]
open_weights_license: unknown
hardware_floor: unknown
pricing: unknown
pricing_source: null
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[suno-mcp-beta-fbbc54a2]]"
last_release: unknown
arena_rank: []
arena_rank_source: []
---

# Suno

## Summary

Suno is an AI music generation service accessible via API and, as of 2026-10-31, via an **MCP (beta)** server at `https://api.suno.com/mcp` [[suno-mcp-beta-fbbc54a2]]. The MCP beta connects Suno to Claude, Claude Code, ChatGPT, and other MCP clients via HTTP transport with no API key required — Claude Code users run `claude mcp add --transport http suno https://api.suno.com/mcp` and sign in with `/mcp`.

Capabilities via MCP: create songs from plain-language descriptions, start from an uploaded audio clip, remix songs from your Suno library (covers, extensions, mashups). Every song lands in the user's Suno library. The MCP beta is available on all plans including Free; song creation uses credits per plan.

> Suno MCP (beta) connects Suno to Claude, ChatGPT, Claude Code and other MCP clients.

> Setup for Claude Code: run claude mcp add --transport http suno https://api.suno.com/mcp in your terminal, then in a Claude Code session run /mcp to sign in to Suno. No API key is needed.

> The beta is available on all Suno plans, including Free. Creating music uses credits based on your plan.

## Open questions

- [ ] What are Suno's credit-to-cost rates per generated song on paid plans?
- [ ] Does Suno allow commercial use of generated music on all paid plans?

## See also

- [[generative-media-models]]
- [[suno-mcp-beta-fbbc54a2]]

_no contradictions or gaps known yet (last reviewed: 2026-10-31)_
