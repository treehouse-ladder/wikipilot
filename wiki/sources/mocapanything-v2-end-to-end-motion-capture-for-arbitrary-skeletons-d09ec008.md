---
fetched_at: &id001 2026-05-22
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: d09ec008b0e27db21fde1b87abe41c27d0d4d24251fec4fe415a96e9361cf032
sources: []
title: 'MoCapAnything V2: End-to-End Motion Capture for Arbitrary Skeletons'
topic: ai-in-game-dev
url: https://arxiv.org/abs/2604.28130
---

## Excerpts

> MoCapAnything V2 presents the first fully end-to-end framework in which both Video-to-Pose and Pose-to-Rotation are learnable and jointly optimized.

> The previous design is inherently limited, since joint positions do not fully determine rotations and leave degrees of freedom such as bone-axis twist ambiguous, and the non-differentiable IK stage prevents the system from adapting to noisy predictions or optimizing for the final animation objective.

> Experiments on Truebones Zoo and Objaverse show that the method reduces rotation error from ~17 degrees to ~10 degrees, and to 6.54 degrees on unseen skeletons, while achieving ~20x faster inference than mesh-based pipelines.

> both stages share a skeleton-aware Global-Local Graph-guided Multi-Head Attention (GL-GMHA) module for joint-level local reasoning and global coordination.