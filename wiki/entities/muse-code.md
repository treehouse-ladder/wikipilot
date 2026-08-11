---
title: "Muse Code"
kind: entity
sources: ["[[introducing-muse-code-and-muse-spark-1-2-a73147b0]]", "[[introducing-muse-glimmer-c60b75d4]]"]
last_updated: 2026-08-11
last_verified: 2026-08-06
freshness_window_days: 30
---

## Summary

**Muse Code** is Meta's terminal coding agent, launched in public beta (macOS/Linux) on 2026-08-05 as a competitor to Claude Code and OpenAI Codex [[introducing-muse-code-and-muse-spark-1-2-a73147b0]]. It is paired with **Muse Spark 1.2**, a coding-focused model that was *co-trained with the Muse Code harness itself* — training incorporated rejection-sampled harness trajectories and integration of the Muse Code toolset, so the model and harness are tuned to each other rather than the harness wrapping a general model [[introducing-muse-code-and-muse-spark-1-2-a73147b0]]. Muse Spark 1.2 is priced at $1.25/M input and $4.25/M output, with a data-sharing `muse-spark-1.2-contributor` tier at $0.10/$0.20 that lets Meta use your data "to improve our products" [[introducing-muse-code-and-muse-spark-1-2-a73147b0]].

> Muse Spark 1.2 was co-trained with Muse Code ... training that included rejection sampled harness trajectories and recipe optimizations alongside the integration of the Muse Code toolset. The muse-spark-1.2 model is priced at $1.25/million input and $4.25/million output, but if you agree to let Meta use your data 'to improve our products' you can use muse-spark-1.2-contributor which is $0.10/$0.20. [[introducing-muse-code-and-muse-spark-1-2-a73147b0]]

Five days after the Muse Code + Muse Spark 1.2 launch, Meta also released **Muse Glimmer**, a 30B Apache-2.0 open-weights model optimized for agentic task completion [[introducing-muse-glimmer-c60b75d4]]. Unlike Muse Spark 1.2 (API-only, $1.25/$4.25 per Mtoken), Muse Glimmer is an open-weights model users can run in their own harness. Meta positions it as optimized for end-to-end task completion on full-task benchmarks (SWE-Bench, MCP-Atlas, τ-Bench, DeepSearch QA), but the numbers are all Meta's own — no independent third-party verification yet [[introducing-muse-glimmer-c60b75d4]].

> Muse Glimmer is a new 30B model from Meta released under a clean Apache 2.0 license, optimized for end-to-end agentic task completion. It achieves strong success rates on full-task benchmarks including DeepSearch QA, MCP-Atlas, tau-Bench and SWE-Bench, measuring its ability to work within scaffolds, write and debug code, and resolve multi-turn requests from start to finish. [[introducing-muse-glimmer-c60b75d4]]

_no contradictions or gaps known yet (last reviewed: 2026-08-11)_

## Disputes

## Open questions

## See also

- [[muse-spark]]
- [[agentic-coding]]
