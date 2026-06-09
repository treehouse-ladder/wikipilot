---
fetched_at: &id001 2026-06-09
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: c5e037f4a6e0a8a54256538b1b4b15fabda403d2af2a7aeb5d3e719122f99371
sources: []
title: 'UE 5.7''s Built-In AI Assistant vs. MCP: Which AI Workflow Actually Ships
  Games?'
topic: ai-in-game-dev
url: https://www.strayspark.studio/blog/ue57-ai-assistant-vs-mcp-comparison
---

## Excerpts

> UE 5.7's AI Assistant is a docked panel inside the editor that connects to a cloud-based LLM, currently powered by an Epic-hosted model with options to connect Claude or GPT-4. However, it has some limitations: the assistant only knows about Unreal Engine and cannot bridge workflows involving external tools like Blender, Substance, or Houdini, living entirely inside the UE editor. MCP takes a fundamentally different approach by exposing the editor's functionality as a structured tool API that external AI agents can call. If using both Blender and Unreal MCP Servers, an AI agent can coordinate workflows across both tools — modeling in Blender, exporting, importing into Unreal, setting up materials, and placing items in levels from a single conversation. The Unreal MCP Server exposes 359 editor tools, 15 resources, and 11 prompts to AI agents via JSON-RPC 2.0 over HTTP.