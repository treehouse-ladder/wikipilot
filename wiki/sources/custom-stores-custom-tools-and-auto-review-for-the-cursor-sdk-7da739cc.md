---
title: "Custom stores, custom tools, and auto-review for the Cursor SDK"
kind: source
url: "https://cursor.com/changelog/sdk-updates-jun-2026"
sha256: "7da739ccef233deac952f1ab5b26fd030ea6d74b610bd5a4b527eaafb7ebaf4f"
fetched_at: "2026-06-12"
topic: agentic-coding
image_count: 0
sources: []
last_updated: 2026-06-12
last_verified: 2026-06-12
freshness_window_days: 365
---

## Excerpts

> Cursor ships major SDK upgrades for TypeScript and Python, adding custom tools, auto-review controls, JSONL and custom metadata stores, and deeply nested subagents.

> The Python SDK exposes host, JSONL, and composed JSONL stores through the bridge. Every send() now carries a platform-generated requestId, exposed on Run and RunResult and persisted across the in-memory, SQLite, and JSONL stores.

> Subagents can now spawn their own subagents, and so on — a reviewer subagent can delegate to a test-writer, which can delegate further, with each level keeping its own prompt and model.
