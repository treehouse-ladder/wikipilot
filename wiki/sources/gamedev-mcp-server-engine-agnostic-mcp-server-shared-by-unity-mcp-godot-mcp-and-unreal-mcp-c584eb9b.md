---
fetched_at: &id001 2026-07-12
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: c584eb9bf496397445198e153f09cac0d841bc1530db4df611552946288447b7
sources: []
title: 'GameDev-MCP-Server: engine-agnostic MCP server shared by Unity-MCP, Godot-MCP
  and Unreal-MCP'
topic: ai-in-game-dev
url: https://github.com/IvanMurzak/GameDev-MCP-Server
---

## Excerpts

> Engine-agnostic Model Context Protocol server shared by game-engine MCP plugins: Unity-MCP, Godot-MCP, and Unreal-MCP.

> The server bridges MCP clients (Claude, Cursor, Copilot, ...) and an engine plugin over SignalR, with no engine-specific code in the repository — one server binary serves all three engine plugins. Tools, resources and prompts are provided dynamically by whichever engine plugin connects.

> The first release of the shared, engine-agnostic MCP server de-triplicates the per-engine servers (unity-mcp-server 0.80.x, godot-mcp-server 0.3.x, unreal-mcp-server 0.1.x) into one host.