---
title: Subquadratic attention
kind: concept
sources:
  - "[[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]]"
  - "[[subquadratic-launches-with-29m-to-bring-12m-token-context-windows-to-ai-78c846ee]]"
last_updated: 2026-05-23
last_verified: 2026-05-23
freshness_window_days: 30
---

# Subquadratic attention

## Summary

Subquadratic attention is the class of attention mechanisms whose compute cost scales sub-quadratically (ideally linearly) in sequence length, rather than the O(n^2) cost of standard dense attention that has historically capped practical context windows. The first commercial frontier-class instance is SubQ from Miami startup Subquadratic, launched May 5, 2026, whose SSA layer reportedly scales linearly with context length and cuts attention compute by ~1,000x at 12M tokens via content-dependent position selection that itself avoids going quadratic [[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]]. SubQ exposes a 12M-token context window through an API, a SubQ Code coding agent, and a SubQ Search deep-research tool [[subquadratic-launches-with-29m-to-bring-12m-token-context-windows-to-ai-78c846ee]].

> The SSA architecture scales linearly with context length instead of quadratically, cutting attention compute by roughly 1,000x at 12M tokens.

> Selection is content-dependent, with the model picking which positions matter based on what the query and keys actually contain, and the selection mechanism itself does not go quadratic.

Why it matters for agentic workflows: attention cost at long context has been the practical wall on feeding an entire codebase (or a long agent trajectory) into a single prompt. A linear-scaling attention with reported prefill speedups of 7.2x at 128K up to 52.2x at 1M tokens vs FlashAttention on B200 GPUs [[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]] changes the economics of whole-repo context. SubQ also reports frontier-band quality (81.8% SWE-bench Verified, 95.0% RULER 128K), suggesting the long-context cost reduction need not trade away short-context capability — though every figure is vendor-run and not yet independently reproduced [[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]].

> SubQ scored 95.0% on RULER 128K, 65.9% on MRCR v2 at 1M tokens, and 81.8% on SWE-Bench Verified.

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-05-23)_

## Open questions

- [ ] Is subquadratic/SSA attention architecturally convergent with the DeepSeek Sparse Attention that GLM-5 integrates, and which approach better preserves recall at the 1M-token+ regime [[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]]?
- [ ] Do SubQ's vendor-reported B200 prefill speedups (up to 52.2x at 1M) replicate on independent hardware/eval, or are they single-shot best cases [[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]]?

## See also

- [[frontier-models]]
