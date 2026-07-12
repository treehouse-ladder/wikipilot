---
fetched_at: &id001 2026-07-12
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 15a50b3d331488e42698c9a4866e3b09a9420f7ef636fa41e46db812d4b8e84a
sources: []
title: Rewriting Bun in Rust
topic: agentic-coding
url: https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/
---

## Excerpts

> Pre-merge, this took 5.9 billion uncached input tokens, 690 million output tokens, and 72 billion cached input token reads — around $165,000 at API pricing. A perk of working at Anthropic is that you don't have to pay for your tokens - handy when the estimated cost is $165,000! An agent harness was used to automate much of the initial port from Bun to Rust, initially as an experiment to try out an earlier version of the model we now have access to as Mythos/Fable. For most of those 11 days (and after), monitors reviewed workflows - manually reading the outputs to check for issues and bugs, and prompting Claude to edit the loop to fix things.