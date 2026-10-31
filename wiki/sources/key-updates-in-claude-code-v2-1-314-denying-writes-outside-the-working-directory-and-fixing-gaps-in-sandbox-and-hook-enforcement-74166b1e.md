---
fetched_at: &id001 2026-10-31
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 74166b1e3ab45102ef50dce18a70d8e27293cae0c06d7fe2bb3e4a86f0c69d9d
sources: []
title: Key Updates in Claude Code v2.1.314 - Denying Writes Outside the Working Directory
  and Fixing Gaps in Sandbox and Hook Enforcement
topic: agentic-coding
url: https://dev.classmethod.jp/en/articles/20261030-cc-updates-v2-1-314/
---

## Excerpts

> Added permissions.blockWritesOutsideWorkingDirectories: Write, Edit and NotebookEdit refuse paths outside the working directories in every permission mode.

> Added idle compaction to VS Code and Claude Desktop's Code tab: the summary is computed while you're away and only used if your next message comes an hour or more later.

> Fixed claude -p exiting with code 0 and no output when startup failed, now exits with an error.
