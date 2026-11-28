---
fetched_at: &id001 2026-11-28
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 69fbec9981f84b435a9deadb2f44143e2e52e655849d0255056557c8b934cbaf
sources: []
title: Migrating our Messages API to Rust
topic: agentic-coding
url: https://www.anthropic.com/research/migrating-api-to-rust
---

## Excerpts

> In this post, we share how we turned the production Messages API itself into a verifier—and how that helped us test the new Rust version on production traffic, find where it differed, and automatically dispatch agents to fix those differences. This allowed us to ship an API on Rust that uses about 70% less CPU per request and cuts median time to first token by about 20% without ever taking the service offline or freezing feature development.

> This coordinator assigned a worker agent to own each new kind of record. It also created a new thread in a shared Slack channel where human engineers could follow along and steer it when necessary.

> A fast inner loop gave agents a sandbox in which they could test ideas and propose fixes. A slower outer loop then validated fixes in production. In addition, a memory loop recorded any mistakes along the way, saving them so that agents could learn over time

> We allowed a fix to cross into the outer loop only after it had undergone PR review; this allowed engineers to focus their attention on proposed fixes (rather than on guesses) and on the questions the verifiers couldn’t answer, such as whether a difference between the Rust and Python APIs was the result of a bug or a deliberate change.

> Verification is the new bottleneck. Previously, large software projects like migrations were hard to justify because they took too much effort and carried too much risk. But if writing code is no longer the bottleneck, the main constraint becomes how quickly you can verify results.

> Each agent ran in a cloud sandbox with both codebases and fast, local checks for what happens before and after the model call.