---
fetched_at: &id001 2026-05-23
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: badc2592d4666d13d1f26722ce2e0d9b35ad49ff4c9e4c156b6122d9b6372379
sources: []
title: 'The context window has been shattered: Subquadratic debuts a 12-million-token
  window'
topic: frontier-models
url: https://thenewstack.io/subquadratic-12-million-context-window/
---

## Excerpts

> The SSA architecture scales linearly with context length instead of quadratically, cutting attention compute by roughly 1,000x at 12M tokens.

> Selection is content-dependent, with the model picking which positions matter based on what the query and keys actually contain, and the selection mechanism itself does not go quadratic.

> Prefill speedups are reported as 7.2x at 128K, 13.2x at 256K, 23x at 512K, and 52.2x at 1M tokens versus FlashAttention on B200 GPUs.

> SubQ scored 95.0% on RULER 128K, 65.9% on MRCR v2 at 1M tokens, and 81.8% on SWE-Bench Verified. At 1M tokens, SubQ outperforms Gemini 3.1 Pro (65.9% vs 26.3%) on MRCR v2, though it trails GPT-5.5 (74.0%).

> The architecture and launch are real and widely reported, but the headline efficiency claims are vendor-run, single-shot, and not yet independently reproduced.

> Subquadratic is making this model available through an API with a 12-million-token context window, as well as a coding agent (SubQ Code) and a deep research tool (SubQ Search).