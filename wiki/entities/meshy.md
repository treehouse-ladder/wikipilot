---
title: "Meshy"
kind: entity
aliases: ["Meshy AI", "Meshy-7", "Meshy 7.1", "meshy.ai"]
sources:
  - "[[meshy-7-1-ultra-4k-detail-richness-benchmark-45c8801a]]"
  - "[[meshy-7-is-live-higher-fidelity-image-to-3d-generation-with-ultra-mode-f27c1d9b]]"
  - "[[meshy-6-smarter-geometry-faster-workflows-limitless-3d-creativity-3d2a1b1b]]"
  - "[[meshy-brings-ai-agents-to-3d-creation-meshy-3d-agent-beta-launches-f384359e]]"
  - "[[meshy-raises-nearly-400-million-at-a-1-5-billion-valuation-the-largest-round-to-date-in-ai-3d-629b40da]]"
  - "[[meshy-image-to-3d-api-meshy-t2-5-is-the-default-smart-topology-model-lowpoly-retires-30-oct-2026-82720073]]"
  - "[[can-i-use-meshy-assets-commercially-license-copyright-explained-f2a86115]]"
  - "[[meshy-pricing-credits-plans-and-usage-62da5fc3]]"
last_updated: 2026-10-26
last_verified: 2026-10-26
freshness_window_days: 30
profile: tool
modality: 3d
tasks: ["text-to-3d", "image-to-3d", "multi-image-to-3d", "retexture", "low-poly-mode"]
vendor: "Meshy"
model_ids: ["meshy-6", "meshy-7", "meshy-7.1", "meshy-t2.5"]
access: ["web", "api"]
open_weights_license: unknown
hardware_floor: unknown
pricing: "free 100 credits/mo; Pro $20/mo (1,000 credits); Studio $70/mo (5,500 shared credits) (2026-10-26)"
pricing_source: "[[meshy-pricing-credits-plans-and-usage-62da5fc3]]"
commercial_use: "free tier CC BY 4.0 (commercial with attribution); all paid plans full private commercial, no attribution (2026-10-26)"
commercial_use_source: "[[can-i-use-meshy-assets-commercially-license-copyright-explained-f2a86115]]"
status: active
status_source: "[[meshy-7-1-ultra-4k-detail-richness-benchmark-45c8801a]]"
last_release: unknown
arena_rank: []
arena_rank_source: []
---

# Meshy

## Summary

Meshy is a hosted AI 3D-generation platform (web app plus API) whose current model line is Meshy 7.1; it covers text-to-3D, image-to-3D, multi-image-to-3D and retexturing, and the 7.1 release added an "Ultra 4K" geometry mode that scales generation from 2048³ to 4096³ voxels with raw meshes up to 80 million triangles before simplification [[meshy-7-1-ultra-4k-detail-richness-benchmark-45c8801a]]. The 7.1 model is open to all registered users, but Ultra 2K/4K resolution and downloads are gated to subscribers, and Ultra 4K is single-view only [[meshy-7-1-ultra-4k-detail-richness-benchmark-45c8801a]]. Meshy's own "Detail Richness" benchmark ranks 7.1 first at 1K/2K/4K — a vendor-run benchmark, so it is reported here as a claim rather than recorded in `arena_rank` [[meshy-7-1-ultra-4k-detail-richness-benchmark-45c8801a]].

> A new Ultra 4K mode scales geometry generation from 2048 cubed to 4096 cubed, and as of this release is the only 3D generative model to reach it, with raw meshes up to 80 million triangles before simplification.

Meshy 7 (the previous step) introduced the `ultra_mode` API parameter, a multi-view generation model for the Multi-Image to 3D API, and a new texturing model for the Retexture API [[meshy-7-is-live-higher-fidelity-image-to-3d-generation-with-ultra-mode-f27c1d9b]]. Meshy 6 brought a dedicated Low Poly Mode aimed at game developers and "upgraded APIs" [[meshy-6-smarter-geometry-faster-workflows-limitless-3d-creativity-3d2a1b1b]].

> Meshy 7 introduces the ultra_mode parameter, which enables Ultra generation for even finer surface detail. For the Multi-Image to 3D API, Meshy 7 is Meshy's multi-view generation model, which conditions on all of your input views together and drives texturing from them.

> A dedicated Low Poly Mode built specifically for game developers produces efficient wireframes optimized for real-time performance, making assets easier to integrate into game engines without extensive manual retopology.

On the product side, Meshy 3D Agent Beta (a chat-based, multi-step ideation-to-asset workflow) became available to all users on meshy.ai on June 4, 2026 [[meshy-brings-ai-agents-to-3d-creation-meshy-3d-agent-beta-launches-f384359e]]. Commercially, Meshy raised nearly $400M in a Series B at a $1.5B valuation and reported 12M+ registered users and 100M+ models created as of July 2026 [[meshy-raises-nearly-400-million-at-a-1-5-billion-valuation-the-largest-round-to-date-in-ai-3d-629b40da]].

> At launch, Meshy 3D Agent Beta became available to all users on meshy.ai from June 4, 2026.

> As of July 2026, the company's annual recurring revenue is growing about 12x year over year, with more than 12 million registered users and over 100 million models created.

**Meshy T2.5 is the new default Smart Topology model (Oct 15, 2026); LowPoly model type retires Oct 30, 2026.** `meshy-t2.5` was added on October 15, 2026 as the default when `model_type: smart-topology` is set without an explicit `ai_model` [[meshy-image-to-3d-api-meshy-t2-5-is-the-default-smart-topology-model-lowpoly-retires-30-oct-2026-82720073]]. It supports Image to 3D and Text to 3D (not Multi-Image to 3D), with `target_polycount` 100–30,000 (default 15,000), priced the same as `meshy-t2`. `model_type: lowpoly` retires October 30, 2026 and returns an error after that date; the recommended migration is `smart-topology` with `meshy-t2.5`. Also: `meshy-5` was retired October 10 (replaced by `meshy-6-lite`), and USDZ exports switched to metres October 12.

> meshy-t2.5 (default): sharper detail for game assets. [[meshy-image-to-3d-api-meshy-t2-5-is-the-default-smart-topology-model-lowpoly-retires-30-oct-2026-82720073]]

> Meshy retires lowpoly on October 30, 2026. After that date, a request with model_type: "lowpoly" returns an error; the recommended replacement is smart-topology with meshy-t2.5. [[meshy-image-to-3d-api-meshy-t2-5-is-the-default-smart-topology-model-lowpoly-retires-30-oct-2026-82720073]]

**Pricing and commercial use (confirmed 2026-10-26).** The free tier provides 100 credits/mo and licenses outputs under CC BY 4.0 — commercial use is permitted with Meshy attribution. Paid plans (Pro $20/mo, Studio $70/mo) grant full private ownership with no attribution requirement; models generated while on a paid plan retain that plan's rights even after downgrading [[can-i-use-meshy-assets-commercially-license-copyright-explained-f2a86115]][[meshy-pricing-credits-plans-and-usage-62da5fc3]].

> Models generated on the Meshy free plan are licensed under CC BY 4.0, which permits commercial use if Meshy is credited. If you are a paid customer, you own the assets created through our platform. [[can-i-use-meshy-assets-commercially-license-copyright-explained-f2a86115]]

> The official USD pricing page lists Pro at 20 USD/month and Studio at 70 USD/month. All paid plans include commercial-use rights and a private license. [[meshy-pricing-credits-plans-and-usage-62da5fc3]]

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-24)_

## Open questions

- [ ] Pricing (per-credit / per-generation cost and plan tiers) — no ingested source states a figure; the sweep should cite meshy.ai pricing or docs.meshy.ai.
- [ ] Commercial-use terms per plan (free vs subscribed) — only "subscribed users can download 7.1 models" is on record.
- [ ] Exact release dates for Meshy 7 and 7.1 (sources carry no dates; `last_release` is `unknown`).
- [ ] Is Meshy listed on any third-party board (Artificial Analysis image-to-3D arena, etc.)? Only the vendor-run Detail Richness benchmark is cited.
- [ ] fal / Replicate endpoint ids, if any (`model_ids` carries vendor ids only).

## See also

- [[ai-in-game-dev]]
- [[3d-tools]]
- [[tripo]]
- [[hyper3d-rodin]]
- [[hunyuan3d]]
