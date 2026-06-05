---
fetched_at: &id001 2026-06-05
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 711104a69c062f83e462f75cea128a2ef1a52ba6ac4c099079aa4939ed97ed82
sources: []
title: 'TRELLIS.2: Native and Compact Structured Latents for 3D Generation'
topic: ai-in-game-dev
url: https://microsoft.github.io/TRELLIS.2/
---

## Excerpts

> TRELLIS.2 is trained to generate fully textured assets at up to 1536 cubed resolution. It utilizes a Sparse 3D VAE with 16x spatial downsampling, encoding a 1024 cubed asset into only ~9.6K latent tokens with negligible perceptual degradation. The model supports full PBR attributes (Base Color, Metallic, Roughness, Alpha) to accurately model rich surface materials. At 512 cubed it generates a fully textured asset in approximately 3 seconds (2s shape + 1s material); at 1024 cubed in approximately 17 seconds; at 1536 cubed in approximately 60 seconds. Released under MIT license for commercial use.