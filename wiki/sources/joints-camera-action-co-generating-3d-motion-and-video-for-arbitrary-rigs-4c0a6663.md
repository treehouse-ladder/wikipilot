---
fetched_at: &id001 2026-10-26
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 4c0a6663d9fda1aa943d6f595a046b2812487ea9cd3bb0651966b7bff5fcb03d
sources: []
title: Joints, Camera, Action! Co-Generating 3D Motion and Video for Arbitrary Rigs
topic: ai-in-game-dev
url: https://research.nvidia.com/labs/par/projects/jca/
---

## Excerpts

> Joints, Camera, Action! (JCA) generates a video and a matching 3D motion for a rig from a text prompt, and the rig can have any skeleton structure.

> A separate motion model treats the skeleton as a graph and connects to a pretrained video generator through cross-attention layers. The motion model is pretrained on motion-only data, including retargeted motions on randomized skeletons.

> A joint-localization head predicts where each 3D joint appears in the video frames, which lets the system fit a camera that places the motion in the generated scene.

> The model converts in both directions, from rig motion to video and from video to rig motion, and the authors report nearly 200K training pairs combining human and robot video.