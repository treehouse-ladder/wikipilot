---
title: "GPT-6 Astra"
kind: entity
aliases: ["GPT 6 Astra", "gpt6-astra", "Astra", "OpenAI Astra"]
sources: ["[[gpt-6-astra-a-new-generation-of-intelligence-039a4975]]", "[[benchmarking-gpt-6-astra-b4150b17]]", "[[openai-launches-astra-its-powerful-and-controversial-new-model-939b4e3d]]", "[[openai-astra-and-looped-transformers-beac0586]]"]
last_updated: 2026-09-04
last_verified: 2026-09-04
freshness_window_days: 30
---

# GPT-6 Astra

## Summary

GPT-6 Astra is OpenAI's next-generation flagship, launched **2026-09-03**. OpenAI calls it 'our most intelligent model yet, with state-of-the-art performance in computer use, browsing, software engineering, science, and professional work' [[gpt-6-astra-a-new-generation-of-intelligence-039a4975]]. Artificial Analysis places it at **AA Intelligence Index 61 — tied with GPT-5.6 Sol (max)** — superseding Sol as OpenAI's flagship without moving OpenAI up the aggregate board (Claude Fable 5.1 = 66 #1, Claude Opus 5 = 63 #2) [[benchmarking-gpt-6-astra-b4150b17]]. Pricing: **$10/$50 per Mtoken** (2.5x GPT-5.6 Sol's $4/$20, matching Claude Fable 5/5.1), 90% cache-read discount, 272K+ long-context tier at 2x input / 1.5x output with 2.5x-faster Fast mode [[gpt-6-astra-a-new-generation-of-intelligence-039a4975]] [[benchmarking-gpt-6-astra-b4150b17]]. Standout gain: **hallucination rate drops 92%→51% at max effort; accuracy up 4 points** simultaneously [[benchmarking-gpt-6-astra-b4150b17]]. Architecture: constrained **recurrent depth / looped Transformers** — reusing a core layer stack in a loop without new parameters, which can obscure chain-of-thought; OpenAI says use is capped for legibility [[openai-launches-astra-its-powerful-and-controversial-new-model-939b4e3d]] [[openai-astra-and-looped-transformers-beac0586]].

> GPT-6 Astra is our most intelligent model yet. [[gpt-6-astra-a-new-generation-of-intelligence-039a4975]]

> GPT-6 Astra scores 61 on the Artificial Analysis Intelligence Index, equal to GPT-5.6 Sol. [[benchmarking-gpt-6-astra-b4150b17]]

> Pricing is 2.5x GPT-5.6 Sol's current prices across the board, up from $4/$20 to $10/$50 per million input/output tokens. [[benchmarking-gpt-6-astra-b4150b17]]

> GPT-6 Astra sees a large jump in AA-Omniscience, driven by a significant decrease in hallucination rate from 92% to 51% at max effort, and increased accuracy by 4 points at the same time. [[benchmarking-gpt-6-astra-b4150b17]]

> OpenAI's new Astra model uses a reasoning technique called "recurrent depth" ... This technique is known to obscure an important model-monitoring process known as chain of thought. [[openai-launches-astra-its-powerful-and-controversial-new-model-939b4e3d]]

> If a model uses more recurrent passes, it may need to generate fewer intermediate reasoning tokens, with more of its computation happening in latent activations that cannot be read as text. [[openai-astra-and-looped-transformers-beac0586]]

## Disputes

- [[benchmarking-gpt-6-astra-b4150b17]] measures GPT-6 Astra at 75% more expensive per Intelligence-Index task than GPT-5.6 Sol at max effort; [[gpt-6-astra-a-new-generation-of-intelligence-039a4975]] reports Astra costing 'about the same as GPT-5.6 Sol (max)' and 'less than half the cost of Claude Fable 5 for the same score.' Status: unresolved — likely different task suites (Intelligence Index vs Coding Agent Index) and/or different GPT-5.6 Sol price baselines.

## Open questions

- [ ] GPT-6 Astra's SWE-bench Pro placement is unpublished at launch; only the aggregate AA Index (61) and Coding Agent Index delta (+2 vs GPT-5.6 Sol) are known. [[benchmarking-gpt-6-astra-b4150b17]] [[gpt-6-astra-a-new-generation-of-intelligence-039a4975]]
- [ ] GPT-6 Astra's maximum context window beyond the 272K long-context pricing threshold is not confirmed from the ingested sources. [[gpt-6-astra-a-new-generation-of-intelligence-039a4975]]

## See also

- [[frontier-models]]
- [[gpt-5.6-sol]]
- [[claude-fable-5]]
- [[claude-opus-5]]
