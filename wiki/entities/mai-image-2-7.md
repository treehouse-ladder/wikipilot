---
title: "MAI-Image-2.7"
kind: entity
aliases: ["MAI Image 2.7", "MAI-Image-2.7 Flash", "Microsoft AI Image 2.7"]
sources:
  - "[[mai-image-2-7-microsoft-ai-image-generator-and-editor-7d6eaf21]]"
last_updated: 2026-11-21
last_verified: 2026-11-21
freshness_window_days: 30
profile: tool
modality: image
tasks: ["text-to-image", "image-editing"]
vendor: "Microsoft AI"
model_ids: ["mai-image-2.7", "mai-image-2.7-flash", "fal:fal-ai/mai-image-2.7", "fal:fal-ai/mai-image-2.7/flash"]
access: ["fal"]
open_weights_license: unknown
hardware_floor: unknown
pricing: "~$0.035/image (1024×1024, standard); ~$0.010/image (1024×1024, Flash) on fal (2026-11-21)"
pricing_source: "[[mai-image-2-7-microsoft-ai-image-generator-and-editor-7d6eaf21]]"
commercial_use: "allowed on fal outputs per fal terms (2026-11-21)"
commercial_use_source: "[[mai-image-2-7-microsoft-ai-image-generator-and-editor-7d6eaf21]]"
status: active
status_source: "[[mai-image-2-7-microsoft-ai-image-generator-and-editor-7d6eaf21]]"
last_release: 2026-11-17
arena_rank: []
arena_rank_source: []
---

# MAI-Image-2.7

## Summary

**MAI-Image-2.7** (and **MAI-Image-2.7 Flash**) is Microsoft AI's closed-weights text-to-image and image-editing model, out of preview around 2026-11-17 and reachable on fal as four pay-per-use endpoints [[mai-image-2-7-microsoft-ai-image-generator-and-editor-7d6eaf21]]. A 1024x1024 output costs ~$0.035/image on the standard model and ~$0.010/image on Flash; fal states outputs can be used in commercial projects per its terms [[mai-image-2-7-microsoft-ai-image-generator-and-editor-7d6eaf21]]. Current Artificial Analysis snapshots place MAI-Image-2.7 at the top of AA-Image-Editing v2.1 (~Elo 1215), narrowly ahead of [[gpt-image]] GPT Image 2.6 Sunburst within margin of error, and #3-4 on AA-Image-T2I v2.1 — but that board URL is already ingested/immutable so the ranking is tracked under Open questions, not arena_rank.

> MAI Image 2.7 is Microsoft AI's image generation and editing model, available on fal as four pay-per-use endpoints: text-to-image and edit for both the standard model and the cheaper Flash variant. A 1024x1024 output costs approximately $0.035 for the standard MAI-Image-2.7 model and approximately $0.010 for MAI-Image-2.7 Flash. [[mai-image-2-7-microsoft-ai-image-generator-and-editor-7d6eaf21]]

## Disputes

## Open questions

- [ ] MAI-Image-2.7's AA-Image-Editing v2.1 #1 placement (~Elo 1215) needs a fresh citable snapshot; the AA editing board URL is already ingested/immutable.
- [ ] Microsoft Foundry (Azure) native pricing and commercial-use/licensing terms for shipping generated assets in a game are unconfirmed.

## See also

- [[generative-media-models]]
- [[gpt-image]]
