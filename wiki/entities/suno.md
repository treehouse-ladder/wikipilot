---
title: "Suno"
kind: entity
aliases: ["Suno AI", "Suno music"]
sources:
  - "[[suno-mcp-beta-fbbc54a2]]"
  - "[[can-i-distribute-my-songs-to-spotify-etc-25684551]]"
last_updated: 2026-11-07
last_verified: 2026-11-07
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
commercial_use: "allowed on Pro/Premier paid plans (songs made & downloaded while subscribed carry commercial rights, incl. Spotify/Apple Music distribution); free-tier downloads personal/non-commercial only; no retroactive license (2026-11-07)"
commercial_use_source: "[[can-i-distribute-my-songs-to-spotify-etc-25684551]]"
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

**Commercial-use terms confirmed (2026-11-07): Suno paid plans grant commercial rights.** Songs made while subscribed to a Pro or Premier plan "are granted commercial use rights ... to distribute songs to Spotify, Apple Music, etc, using the distributor of your choice"; any song downloaded as a paying subscriber carries commercial rights for commercial or personal use [[can-i-distribute-my-songs-to-spotify-etc-25684551]]. Free-plan songs cannot be monetized and there is no retroactive license (subscribing after creating a song does not license that song); free users get only a limited number of trial downloads for personal, non-commercial use. Under the updated downloads policy, Pro includes 20 downloads/month and Premier 60 downloads/month, both with commercial use rights [[can-i-distribute-my-songs-to-spotify-etc-25684551]]. For an indie game dev this means Suno-generated music is shippable commercially on a non-enterprise paid plan, subject to the per-month download limits.

> Songs made while subscribed (to a Pro or Premier plan) are granted commercial use rights. This allows you to distribute songs to Spotify, Apple Music, etc, using the distributor of your choice. [[can-i-distribute-my-songs-to-spotify-etc-25684551]]

> For any song that you download from the platform as a paying subscriber, you have the commercial rights to the music and can use it for commercial or personal use. [[can-i-distribute-my-songs-to-spotify-etc-25684551]]

## Open questions

- [ ] Suno credit-to-song cost rate per generated song on paid plans (for pricing frontmatter, still `unknown`).
- [ ] Confirm the current Suno model version (v6 family) and whether commercial rights differ by model variant (v6 / v6-wild / v6-mini).
- [ ] What are Suno's credit-to-cost rates per generated song on paid plans?
- [ ] Does Suno allow commercial use of generated music on all paid plans?

## See also

- [[generative-media-models]]
- [[suno-mcp-beta-fbbc54a2]]

_no contradictions or gaps known yet (last reviewed: 2026-10-31)_
