---
fetched_at: &id001 2026-10-11
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: b8768176a7631ecedfa1aed4837ac8804174c15a76f26b9bf50ff27696ff8ac1
sources: []
title: 'UniMate: One Unified Model to Animate Diverse Skeletons'
topic: ai-in-game-dev
url: https://huggingface.co/Linzhan/UniMate
---

## Excerpts

> Pretrained checkpoints of UniMate, a text-conditioned flow-matching model that generates motion for skeletons of any topology: animals, humanoids and rigged objects.

> Contact. No unified contact model: contact-rich motions can slide, drift, hover or penetrate the ground; foot locking or IK post-processing helps where contacts are well defined.

> Format. Fixed 60-frame (2 s) samples (longer motion via expansion); a skeleton must fit the model's joint limit; prompts should describe the motion only, as every training caption starts with "An object".

> Output: 60 frames at 30 fps; per joint: position (3), rotation relative to the T-pose (6), velocity (3).

> Checkpoints: CC BY-NC 4.0. Code: MIT.