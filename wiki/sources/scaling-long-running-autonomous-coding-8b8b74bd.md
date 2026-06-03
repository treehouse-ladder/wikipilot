---
fetched_at: &id001 2026-06-03
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 8b8b74bdb5b3ac0f4bc0be7fcaa58fc53e8154f665f51113876988b4c9775dfd
sources: []
title: Scaling long-running autonomous coding
topic: agentic-coding
url: https://cursor.com/blog/scaling-agents
---

## Excerpts

> We've been experimenting with running hundreds of concurrent agents on a single project, coordinating their work, and watching them write over a million lines of code and trillions of tokens.

> We tested this system by pointing it at building a web browser from scratch, with agents running for close to a week and writing over 1 million lines of code across 1,000 files.

> Planners that continuously explore the codebase and create tasks (and can spawn sub-planners for specific areas), while workers pick up tasks and focus entirely on completing them without coordinating with other workers or worrying about the big picture.

> Model choice matters for extremely long-running tasks, with GPT-5.2 models being much better at extended autonomous work: following instructions, keeping focus, avoiding drift, and implementing things precisely and completely.