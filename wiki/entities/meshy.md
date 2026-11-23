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
  - "[[meshy-n1-cleanest-and-fastest-ai-texturing-c7deb738]]"
  - "[[meshy-rigging-api-engine-targeted-skeleton-templates-and-finger-bones-182d1bf5]]"
last_updated: 2026-11-23
last_verified: 2026-11-23
freshness_window_days: 30
profile: tool
modality: 3d
tasks: ["text-to-3d", "image-to-3d", "multi-image-to-3d", "retexture", "low-poly-mode", "rigging"]
vendor: "Meshy"
model_ids: ["meshy-6", "meshy-7", "meshy-7.1", "meshy-t2.5"]
access: ["web", "api"]
open_weights_license: unknown
hardware_floor: unknown
pricing: "Free 100 credits/mo; Pro $20/mo (1,000 credits); Premium $40/mo (3,000 credits); Ultra $100/mo (8,000 credits); Studio $70/mo (5,500 shared credits); Enterprise custom; all paid tiers include commercial rights + private license (2026-11-07)"
pricing_source: "[[meshy-pricing-credits-plans-and-usage-62da5fc3]]"
commercial_use: "free tier CC BY 4.0 (commercial with attribution); all paid plans full private commercial, no attribution (2026-10-26)"
commercial_use_source: "[[can-i-use-meshy-assets-commercially-license-copyright-explained-f2a86115]]"
status: active
status_source: "[[meshy-n1-cleanest-and-fastest-ai-texturing-c7deb738]]"
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

**Pricing and commercial use (confirmed 2026-11-07).** The free tier provides 100 credits/mo (no credit card required) and licenses outputs under CC BY 4.0 — commercial use is permitted with Meshy attribution. Paid tiers are Pro $20/mo (1,000 credits), Premium $40/mo (3,000 credits), Ultra $100/mo (8,000 credits), Studio $70/mo (5,500 shared credits across a team), and Enterprise (custom) — all paid tiers grant full private ownership with commercial rights and no attribution requirement; models generated while on a paid plan retain that plan's rights even after downgrading [[can-i-use-meshy-assets-commercially-license-copyright-explained-f2a86115]][[meshy-pricing-credits-plans-and-usage-62da5fc3]].

> The free plan includes 100 credits per month with no credit card required. [[meshy-pricing-credits-plans-and-usage-62da5fc3]]

> Paid tiers are Pro (1,000 credits/month), Premium (3,000), Ultra (8,000), and Studio (5,500 shared across a team). [[meshy-pricing-credits-plans-and-usage-62da5fc3]]

> The official USD pricing page lists Pro at 20 USD/month and Studio at 70 USD/month; the EUR version lists Pro at 19 EUR and Studio at 67 EUR. All paid plans include commercial-use rights and a private license. [[meshy-pricing-credits-plans-and-usage-62da5fc3]]

> Models generated on the Meshy free plan are licensed under CC BY 4.0, which permits commercial use if Meshy is credited. If you are a paid customer, you own the assets created through our platform. [[can-i-use-meshy-assets-commercially-license-copyright-explained-f2a86115]]

**Meshy Rigging API — engine-targeted skeleton templates and finger bones (2026-11-19).** The Meshy Rigging API (v1 and v2) supports six **skeleton templates**: `meshyrig`, `mixamo`, `ue5_mannequin`, `max_biped`, `unity_humanoid`, and `maya_human_ik` [[meshy-rigging-api-engine-targeted-skeleton-templates-and-finger-bones-182d1bf5]]. The v1 endpoint defaults to `meshyrig`; the v2 endpoint defaults to `mixamo`. An optional `include_fingers` parameter adds standard finger bones (using Mixamo naming: `LeftHandThumb1` etc.) and is only available on the biped rig. Input requirements: textured humanoid GLB delivered as an HTTP/HTTPS URL (≤400 MB) or data URI (≤100 MB), with ≤380,000 triangles [[meshy-rigging-api-engine-targeted-skeleton-templates-and-finger-bones-182d1bf5]].

> skeleton_template supports meshyrig, mixamo, ue5_mannequin, max_biped, unity_humanoid, and maya_human_ik. The v1 Rigging defaults to meshyrig; the v2 endpoint defaults to mixamo. [[meshy-rigging-api-engine-targeted-skeleton-templates-and-finger-bones-182d1bf5]]

> include_fingers adds finger bones to the biped rig using Mixamo naming (LeftHandThumb1, etc.). [[meshy-rigging-api-engine-targeted-skeleton-templates-and-finger-bones-182d1bf5]]

**Meshy N1 — first native texturing model (2026-11-18).** Meshy N1 is the first native texturing model that generates color directly on the 3D surface instead of projecting 2D images onto a mesh, eliminating seams and color bleeding [[meshy-n1-cleanest-and-fastest-ai-texturing-c7deb738]]. At approximately 20 seconds per output, it is the fastest texturing model on the market, roughly 3× faster than Meshy 7's ~60 seconds. N1 outputs a 2K base color map only — it does not generate PBR maps and does not support 4K or 8K resolution. It works from reference images rather than text prompts. N1 is available to all registered users through the Meshy API (Retexture, Image to 3D, Multi-Image to 3D, and Text to 3D refine) and is the default texture mode for T-series models in the web app; multi-view texturing (which takes several reference images) is limited to subscribers [[meshy-n1-cleanest-and-fastest-ai-texturing-c7deb738]].

> Meshy N1 is our first native texturing model. Instead of projecting multiple 2D images onto a mesh, it generates color directly on the 3D surface, which removes seams and color bleeding. [[meshy-n1-cleanest-and-fastest-ai-texturing-c7deb738]]

> N1 is the fastest texturing model on the market, producing textured output in about 20 seconds, compared with roughly a minute for Meshy 7. [[meshy-n1-cleanest-and-fastest-ai-texturing-c7deb738]]

> N1 outputs a 2K base color map only. It does not generate PBR maps and does not support 4K or 8K resolution. It works from reference images, not text prompts. [[meshy-n1-cleanest-and-fastest-ai-texturing-c7deb738]]

> Quadruped rigging: sending animation_type "quadruped" rigs a four-legged animal and includes walking and running animations; pricing matches the biped rig. [[meshy-7-is-live-higher-fidelity-image-to-3d-generation-with-ultra-mode-f27c1d9b]]

## Disputes

- Open questions section claims "Pricing (per-credit / per-generation cost and plan tiers) — no ingested source states a figure" but frontmatter cites [[meshy-pricing-credits-plans-and-usage-62da5fc3]] with confirmed plan tiers (free 100 credits/mo; Pro $20/mo with 1,000 credits; Studio $70/mo with 5,500 shared credits). Status: unresolved (confidence: high; sweep: 2026-11-01)

> The free plan includes 100 credits per month with no credit card required. Paid tiers are Pro (1,000 credits/month), Premium (3,000), Ultra (8,000), and Studio (5,500 shared across a team). The official USD pricing page lists Pro at 20 USD/month and Studio at 70 USD/month. [[meshy-pricing-credits-plans-and-usage-62da5fc3]]

- Open questions section claims "Commercial-use terms per plan (free vs subscribed) — only 'subscribed users can download 7.1 models' is on record" but frontmatter cites [[can-i-use-meshy-assets-commercially-license-copyright-explained-f2a86115]] with full commercial-use details (free tier: CC BY 4.0 with attribution required; all paid plans: full private ownership, no attribution). Status: unresolved (confidence: high; sweep: 2026-11-01)

> Models generated on the Meshy free plan are licensed under CC BY 4.0, which permits commercial use if Meshy is credited. If you are a paid customer, you own the assets created through our platform. Models generated while you were on a paid plan keep the rights associated with that plan. [[can-i-use-meshy-assets-commercially-license-copyright-explained-f2a86115]]

- [[ai-in-game-dev]] Updates 2026-11-19 claims "Meshy was last_verified 2026-11-07... no `last_verified` bumps this run"; [[meshy]] frontmatter shows last_verified: 2026-11-19. Status: unresolved (confidence: high; sweep: 2026-11-22)

> Roster sweep (tool entities — ai-in-game-dev derived roster). Meshy was last_verified 2026-11-07 (pricing completeness update) and Tripo was last_verified 2026-11-05. No new source from today's run contains updated pricing, commercial_use, status, or arena_rank data for either tool; no `last_verified` bumps this run. [[ai-in-game-dev]]

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
