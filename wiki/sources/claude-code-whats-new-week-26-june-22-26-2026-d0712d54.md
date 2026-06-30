---
fetched_at: &id001 2026-06-30
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: d0712d54718674f730573e72adbcb480576ccd74f4e7b5f494d6fca298ec6255
sources: []
title: Claude Code Whats New Week 26 June 22-26 2026
topic: agentic-coding
url: https://code.claude.com/docs/en/whats-new/2026-w26
---

## Excerpts

> New `claude mcp login <name>` and `claude mcp logout <name>` commands authenticate a configured MCP server from your shell instead of the interactive /mcp menu. `claude mcp login` runs the server's OAuth flow directly, and `claude mcp logout` clears the stored credentials. Commands you run with the `!` prefix now get a response from Claude once the output lands in the transcript, so you can run `! npm test` and get an explanation of the failures without a second prompt. The response costs the same as sending a normal prompt. To keep the earlier behavior, where the output is added to context without a response, set `respondToBashCommands` to `false` in `settings.json`. Background subagents now surface permission prompts in the main session instead of auto-denying; the dialog shows which agent is asking, and Esc denies only that tool. New `autoMode.classifyAllShell` setting routes all Bash and PowerShell commands through the auto-mode classifier, and denial reasons now show in the transcript, the denial toast, and /permissions. Streaming responses use about 37% less CPU, and long-session memory growth from the terminal output cache is reduced.

> Background subagents now surface permission prompts in the main session instead of auto-denying; the dialog shows which agent is asking, and Esc denies only that tool.