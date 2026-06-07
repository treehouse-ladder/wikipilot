---
title: Subquadratic attention
kind: concept
sources:
  - "[[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]]"
  - "[[subquadratic-launches-with-29m-to-bring-12m-token-context-windows-to-ai-78c846ee]]"
  - "[[zaya1-8b-frontier-intelligence-density-trained-on-amd-3012ef57]]"
  - "[[zaya1-8b-technical-report-614bf738]]"
  - "[[minimax-m3-frontier-coding-1m-context-native-multimodality-all-in-one-model-d466ccc6]]"
last_updated: 2026-06-07
last_verified: 2026-06-07
freshness_window_days: 30
---

# Subquadratic attention

## Summary

Subquadratic attention is the class of attention mechanisms whose compute cost scales sub-quadratically (ideally linearly) in sequence length, rather than the O(n^2) cost of standard dense attention that has historically capped practical context windows. The first commercial frontier-class instance is SubQ from Miami startup Subquadratic, launched May 5, 2026, whose SSA layer reportedly scales linearly with context length and cuts attention compute by ~1,000x at 12M tokens via content-dependent position selection that itself avoids going quadratic [[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]]. SubQ exposes a 12M-token context window through an API, a SubQ Code coding agent, and a SubQ Search deep-research tool [[subquadratic-launches-with-29m-to-bring-12m-token-context-windows-to-ai-78c846ee]].

> The SSA architecture scales linearly with context length instead of quadratically, cutting attention compute by roughly 1,000x at 12M tokens.

> Selection is content-dependent, with the model picking which positions matter based on what the query and keys actually contain, and the selection mechanism itself does not go quadratic.

Why it matters for agentic workflows: attention cost at long context has been the practical wall on feeding an entire codebase (or a long agent trajectory) into a single prompt. A linear-scaling attention with reported prefill speedups of 7.2x at 128K up to 52.2x at 1M tokens vs FlashAttention on B200 GPUs [[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]] changes the economics of whole-repo context. SubQ also reports frontier-band quality (81.8% SWE-bench Verified, 95.0% RULER 128K), suggesting the long-context cost reduction need not trade away short-context capability — though every figure is vendor-run and not yet independently reproduced [[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]].

> SubQ scored 95.0% on RULER 128K, 65.9% on MRCR v2 at 1M tokens, and 81.8% on SWE-Bench Verified.

An alternative approach is Compressed Convolutional Attention (CCA), shipped in Zyphra's ZAYA1-8B (May 6, 2026). CCA performs sequence mixing in a compressed latent space rather than full multi-head attention, resulting in an 8x reduction in KV-cache size [[zaya1-8b-technical-report-614bf738]]. ZAYA1-8B is an 8.4B-total / ~760M-active MoE optimized for maximum intelligence density per active parameter, reaching 91.9% on AIME'25 and 89.6% on HMMT'25 despite its sub-1B active footprint [[zaya1-8b-frontier-intelligence-density-trained-on-amd-3012ef57]]. Architecturally, CCA addresses memory bandwidth (via cache compression) more directly than inference throughput (SubQ's SSA), and the technical report does not claim linear scaling with context length — so CCA and SSA are complementary routes to efficient attention rather than competing implementations of the same idea [[zaya1-8b-technical-report-614bf738]].

> CCA performs sequence mixing in a compressed latent space, resulting in an 8x reduction in KV-cache size compared to full multi-head attention.

> ZAYA1-8B is a Mixture-of-Experts language model optimized for maximum reasoning performance per active parameter, with 8.4B total parameters but only 760M active per forward pass.

Another implementation is MiniMax Sparse Attention (MSA), shipped in MiniMax M3 (June 1, 2026), the first open-weight model to combine frontier-tier coding, 1M-token context, and native multimodality [[minimax-m3-frontier-coding-1m-context-native-multimodality-all-in-one-model-d466ccc6]]. MSA delivers per-token compute at 1M context that is 1/20 that of the previous-generation MiniMax M2, making M3's long-context inference feasible at frontier capability levels [[minimax-m3-frontier-coding-1m-context-native-multimodality-all-in-one-model-d466ccc6]]. See [[minimax-m3]].

> M3 uses MSA (MiniMax Sparse Attention)... at a context length of 1 million, M3's per-token compute is just 1/20 that of the previous-generation model.

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-05-24)_

## Open questions

- [ ] Is subquadratic/SSA attention architecturally convergent with the DeepSeek Sparse Attention that GLM-5 integrates, and which approach better preserves recall at the 1M-token+ regime [[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]]?
- [ ] Do SubQ's vendor-reported B200 prefill speedups (up to 52.2x at 1M) replicate on independent hardware/eval, or are they single-shot best cases [[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]]?
- [ ] Is ZAYA1-8B's Compressed Convolutional Attention (8x KV-cache reduction) architecturally related to DeepSeek Sparse Attention or SubQ's SSA, or is it a third independent route to efficient attention [[zaya1-8b-technical-report-614bf738]]?

## See also

- [[frontier-models]]
- [[minimax-m3]]
