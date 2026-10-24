---
title: "Tripo"
kind: entity
aliases: ["Tripo AI", "Tripo Studio", "Tripo P2.0", "Tripo P1.0"]
sources:
  - "[[tripo-ai-launches-p2-0-model-to-generate-native-quad-meshes-for-production-pipelines-55aa361e]]"
  - "[[tripo-ai-debuts-production-grade-native-3d-diffusion-at-gdc-2026-46b8acea]]"
  - "[[tripo-ai-raises-nearly-200-million-in-series-a-and-series-a-financing-to-advance-ai-3d-and-world-model-roadmap-999735d1]]"
last_updated: 2026-10-24
last_verified: 2026-10-24
freshness_window_days: 30
profile: tool
modality: 3d
tasks: ["3d-generation", "quad-mesh-generation", "smart-mesh-low-poly", "mesh-edit"]
vendor: "Tripo AI"
model_ids: ["tripo-p1.0", "tripo-p2.0"]
access: ["web"]
open_weights_license: unknown
hardware_floor: unknown
pricing: unknown
pricing_source: null
commercial_use: unknown
commercial_use_source: null
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

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-24)_

## Open questions

- [ ] Does Tripo expose a public API (and fal / Replicate endpoints)? No ingested source mentions one; `access` lists only the Studio web app.
- [ ] Pricing and commercial-use terms — no source on record.
- [ ] P2.0 official launch date (source says "following the P2.0 Preview in August" without a date).
- [ ] Third-party arena placement — none cited.

## See also

- [[ai-in-game-dev]]
- [[3d-tools]]
- [[meshy]]
- [[hunyuan3d]]
