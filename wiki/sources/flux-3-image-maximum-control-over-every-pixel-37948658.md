---
fetched_at: &id001 2026-10-26
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 37948658fc64306e709ba3fb5fb8667c51f9bed27c74aa74ec92059c09a6683b
sources: []
title: 'FLUX 3 Image: Maximum control over every pixel'
topic: generative-media-models
url: https://bfl.ai/models/flux-3-image
---

## Excerpts

> FLUX 3 Image generates and edits images through one endpoint, /v1/flux-3-image.

> POST https://api.bfl.ai/v1/flux-3-image with your API key in the x-key header. Only prompt is required.

> Send a prompt to generate, or add up to ten reference images to edit, restyle, or combine them. Bounding boxes in the prompt place each element. Output goes up to 4K.

> Every box is [top, left, bottom, right] in integers from 0 to 1000, measured from the top-left corner.

> The endpoint rejects unknown fields with HTTP 422, so fields from other BFL endpoints, such as seed, width, and input_image, don't work here.