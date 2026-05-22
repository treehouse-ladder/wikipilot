---
fetched_at: &id001 2026-05-22
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 1eba12a4a8fa384c926895a1f56eed942de137d7d64e90a026c3d5a1def07a15
sources: []
title: Building a C compiler with a team of parallel Claudes
topic: agentic-coding
url: https://www.anthropic.com/engineering/building-c-compiler
---

## Excerpts

> With agent teams, multiple Claude instances work in parallel on a shared codebase without active human intervention, which dramatically expands the scope of what's achievable with LLM agents.

> Over nearly 2,000 Claude Code sessions and $20,000 in API costs, the agent team produced a 100,000-line compiler that can build Linux 6.9 on x86, ARM, and RISC-V. The project consumed 2 billion input tokens and generated 140 million output tokens across two weeks.

> Claude can't tell time and, left alone, will happily spend hours running tests instead of making progress. The harness prints incremental progress infrequently and includes a default --fast option that runs a 1% or 10% random sample.

> When agents started to compile the Linux kernel, they got stuck. Unlike a test suite with hundreds of independent tests, compiling the Linux kernel is one giant task. The fix was to use GCC as an online known-good compiler oracle to compare against. This let each agent work in parallel, fixing different bugs in different files, until Claude's compiler could eventually compile all files.

> Parallelism also enables specialization. One agent was tasked with coalescing any duplicate code it found. Another was put in charge of improving the performance of the compiler itself, and a third was made responsible for outputting efficient compiled code.