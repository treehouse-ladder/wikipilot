---
fetched_at: &id001 2026-05-21
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 4d9dc1194a184bcf2f6e470d85f03c245dfac6b293cfcce5e718e9863d5a07b3
sources: []
title: MCP Server — Blender
topic: ai-in-game-dev
url: https://www.blender.org/lab/mcp-server/
---

## Excerpts

> The Blender project has started exploration of LLM powered tools with an implementation of an MCP connector for Blender. LLM assistants can directly inspect scenes, execute Python code, render images, and navigate the Blender interface. The MCP server has two components: a Blender add-on that runs inside Blender and executes requests, and an MCP client that launches the process and communicates with it over stdio, with the server connecting to the add-on's TCP socket to relay requests to Blender. The MCP server will execute LLM generated code in Blender without any guards in place to protect your data from removal or being sent to a remote location.