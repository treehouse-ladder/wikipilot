---
title: "Tripo"
kind: entity
aliases: ["Tripo AI", "Tripo Studio", "Tripo P2.0", "Tripo P1.0"]
sources:
  - "[[tripo-ai-launches-p2-0-model-to-generate-native-quad-meshes-for-production-pipelines-55aa361e]]"
  - "[[tripo-ai-debuts-production-grade-native-3d-diffusion-at-gdc-2026-46b8acea]]"
  - "[[tripo-ai-raises-nearly-200-million-in-series-a-and-series-a-financing-to-advance-ai-3d-and-world-model-roadmap-999735d1]]"
  - "[[3d-assets-license-guide-scale-game-dev-with-tripo-ai-a3638764]]"
last_updated: 2026-10-26
last_verified: 2026-10-26
freshness_window_days: 30
profile: tool
modality: 3d
tasks: ["3d-generation", "quad-mesh-generation", "smart-mesh-low-poly", "mesh-edit"]
vendor: "Tripo AI"
model_ids: ["tripo-p1.0", "tripo-p2.0"]
access: ["web"]
open_weights_license: unknown
hardware_floor: unknown
pricing: "free 300 credits/mo (non-commercial); Pro $19.90/mo (3,000 credits); API billed under separate commercial contract (2026-10-26)"
pricing_source: "[[3d-assets-license-guide-scale-game-dev-with-tripo-ai-a3638764]]"
commercial_use: "free tier non-commercial; commercial licence permanently attached to assets generated on paid (Pro+) tiers (2026-10-26)"
commercial_use_source: "[[3d-assets-license-guide-scale-game-dev-with-tripo-ai-a3638764]]"
status: active
status_source: "[[tripo-ai-launches-p2-0-model-to-generate-native-quad-meshes-for-production-pipelines-55aa361e]]"
last_release: unknown
arena_rank: []
arena_rank_source: []
---

# Tripo

## Summary

Tripo AI's current model is P2.0, which is reported as the first AI 3D generator to natively output quad meshes (up to 25,000 quad faces or 50,000 triangles) rather than triangulated output; the official launch followed a P2.0 Preview in August and added multi-version generation per prompt and a Mesh Edit feature [[tripo-ai-launches-p2-0-model-to-generate-native-quad-meshes-for-production-pipelines-55aa361e]]. Quad output matters for game pipelines because it deforms more cleanly under animation and cuts manual cleanup before production [[tripo-ai-launches-p2-0-model-to-generate-native-quad-meshes-for-production-pipelines-55aa361e]].

> P2.0 is the first model in the industry able to natively generate quad meshes (four-sided polygons) instead of the triangulated output every AI-based 3D generator has used until now. It can generate up to 25,000 quad faces or 50,000 triangular ones.

The predecessor, Tripo P1.0 ("native 3D diffusion"), was announced at GDC 2026; it resolves an object's global structure holistically rather than sequentially, generates assets in as little as two seconds, and ships as "Smart Mesh" inside Tripo Studio, producing structured low-poly topology directly at generation time [[tripo-ai-debuts-production-grade-native-3d-diffusion-at-gdc-2026-46b8acea]]. The only access path named in the ingested sources is the Tripo Studio product, hence `access: ["web"]`.

> Smart Mesh (P1.0) is now available in Tripo Studio, allowing creators to generate clean, optimized topology meshes directly from AI. Smart Mesh generates clean, structured low-poly topology directly during generation, making assets far easier to use in games, XR, and interactive applications.

Tripo AI raised nearly $200M across Series A+ and A++ rounds and announced Project Eden, a world-model research initiative that decouples persistent world state from generative rendering [[tripo-ai-raises-nearly-200-million-in-series-a-and-series-a-financing-to-advance-ai-3d-and-world-model-roadmap-999735d1]].

> Tripo AI announced the completion of its Series A+ and Series A++ financing rounds, raising nearly $200 million in total.

**Pricing and commercial use confirmed (2026-10-26).** The free tier is non-commercial (300 credits/mo); commercial use requires a paid plan. On Pro+ tiers, the commercial licence is permanently attached to assets generated using Pro-tier credits — the licence persists after downgrading. The Pro plan is $19.90/mo (3,000 credits). API access is handled via a separate commercial contract, not bundled into subscription plans [[3d-assets-license-guide-scale-game-dev-with-tripo-ai-a3638764]].

> Commercial use is unlocked on paid tiers: once a model is generated using Pro-tier credits, the commercial license is permanently attached to that asset. The Pro plan is listed at 19.90 USD per month with 3,000 credits per month. API access is never bundled as an add-on feature to Subscription Plans; it requires a separate commercial contract and account setup. [[3d-assets-license-guide-scale-game-dev-with-tripo-ai-a3638764]]

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-26)_

## Open questions

- [ ] Does Tripo expose a public API (and fal / Replicate endpoints)? The API exists but requires a separate commercial contract [[3d-assets-license-guide-scale-game-dev-with-tripo-ai-a3638764]]; no fal/Replicate endpoint named in any ingested source — `access` stays `["web"]` until confirmed.
- [ ] P2.0 official launch date (source says "following the P2.0 Preview in August" without a date).
- [ ] Third-party arena placement — none cited.

## See also

- [[ai-in-game-dev]]
- [[3d-tools]]
- [[meshy]]
- [[hunyuan3d]]
