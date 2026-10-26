---
compare_fields:
- access
- pricing
- commercial_use
- status
- arena_rank
comparison_of:
- kling
- seedance
- minimax-h3
- flux-3-max
- sora
freshness_window_days: 30
kind: comparison
last_updated: 2026-10-26
last_verified: 2026-10-25
sources: []
title: Video generation tools
---

# Video generation tools

## Summary

This comparison aggregates `access, pricing, commercial_use, status, arena_rank` across 5 entities. Cells marked _unknown_ are missing on the source entity page; backfill the value there and re-run `wikipilot compare regen video-tools` to refresh.

| Entity | access | pricing | commercial_use | status | arena_rank |
| --- | --- | --- | --- | --- | --- |
| [[kling]] | api, replicate | preview/not-yet-launched: 720p 1.0 unit/s (no video input), 1080p 1.5 units/s; video-input rates 0.6/0.9 unit/s (2026-10-26) | unknown | active | _none_ |
| [[seedance]] | api | AA-measured $9.07/min (Seedance 2.0 720p, audio I2V board) to $22.45/min (Seedance 2.0, AA-Video-I2V v1.1) (2026-10-26) | unknown | active | Artificial Analysis Image-to-Video (audio output, Seedance 2.0 720p): #1, Elo 1197 (2026-10-26) |
| [[minimax-h3]] | api, open-weights | AA-measured $34.12/min (768p image-to-video, AA-Video-I2V v1.1) (2026-10-26) | permitted with attribution for organizations below an annual-revenue threshold (figure illegible in source); open weights regionally restricted (2026-08-03) | active | Artificial Analysis Image-to-Video (AA-Video-I2V v1.1, 768p, no audio): #1, Elo 1140 (2026-10-26) |
| [[flux-3-max]] | api, fal | $0.085/s (all variants, via fal) (2026-10-26) | unknown | active | Artificial Analysis Image-to-Video (preliminary, vendor-reported): joint #1 tied with Seedance 2.5, Elo 1139 (2026-10-26) |
| [[sora]] | none | unknown | unknown | shutdown | _none_ |