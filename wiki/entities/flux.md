---
title: "FLUX 3 Image"
kind: entity
aliases: ["FLUX", "FLUX 3 Image", "FLUX 3 Image Klein", "flux-3-image", "flux-3-image-klein", "BFL FLUX"]
sources:
  - "[[flux-3-image-maximum-control-over-every-pixel-37948658]]"
  - "[[flux-3-image-klein-open-weights-5-6b-parameters-155c7b54]]"
last_updated: 2026-10-26
last_verified: 2026-10-26
freshness_window_days: 30
profile: tool
modality: image
tasks: ["text-to-image", "image-editing", "inpainting", "outpainting"]
vendor: "Black Forest Labs"
model_ids: ["flux-3-image", "flux-3-image-klein"]
access: ["api", "open-weights"]
open_weights_license: unknown
hardware_floor: unknown
pricing: "flux-3-image-klein from $0.009/1K images via BFL API (2026-10-26); full FLUX 3 Image per-call price unknown"
pricing_source: "[[flux-3-image-klein-open-weights-5-6b-parameters-155c7b54]]"
commercial_use: unknown
commercial_use_source: null
status: active
status_source: "[[flux-3-image-maximum-control-over-every-pixel-37948658]]"
last_release: unknown
arena_rank: []
arena_rank_source: []
---

# FLUX 3 Image

## Summary

FLUX 3 Image is Black Forest Labs' image generation and editing model, reached through a single BFL API endpoint `/v1/flux-3-image` that both generates and edits, accepts up to ten reference images, supports in-prompt bounding-box layout control, and outputs up to 4K [[flux-3-image-maximum-control-over-every-pixel-37948658]]. An open-weights distilled variant, FLUX 3 Image Klein (5.6B parameters), is served on the BFL API as `flux-3-image-klein` from $0.009 per 1K images [[flux-3-image-klein-open-weights-5-6b-parameters-155c7b54]].

> FLUX 3 Image generates and edits images through one endpoint, /v1/flux-3-image. Send a prompt to generate, or add up to ten reference images to edit, restyle, or combine them. Bounding boxes in the prompt place each element. Output goes up to 4K. [[flux-3-image-maximum-control-over-every-pixel-37948658]]

> BFL API: the distilled model is available as flux-3-image-klein ... Pricing starts at $0.009 per 1K image. FLUX 3 Image Klein is an open weights image generation and editing model with 5.6B parameters. [[flux-3-image-klein-open-weights-5-6b-parameters-155c7b54]]

## Disputes

_no contradictions or gaps known yet (last reviewed: 2026-10-26)_

## Open questions

- [ ] What is the full (non-Klein) FLUX 3 Image per-call price, and under what license are the Klein open weights released (SPDX/name) with what hardware floor?
- [ ] What are the commercial-use terms for shipping FLUX 3 Image / Klein outputs in a commercial game?

## See also

- [[generative-media-models]]
- [[image-tools]]
