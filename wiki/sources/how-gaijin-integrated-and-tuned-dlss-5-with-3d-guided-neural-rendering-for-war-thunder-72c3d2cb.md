---
fetched_at: &id001 2026-11-21
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 72c3d2cb5f29fa39d79c18c6c7514d46dfbc9c1e1cb4182bbd6e74047e5a2c77
sources: []
title: How Gaijin Integrated and Tuned DLSS 5 With 3D-Guided Neural Rendering for
  War Thunder
topic: ai-in-game-dev
url: https://www.nvidia.com/en-us/geforce/news/war-thunder-dlss-5-3d-guided-neural-rendering-developer-interview/
---

## Excerpts

> War Thunder's Eagle's Shadow major update has gone live, adding DLSS 5 with 3D-Guided Neural Rendering, dozens of new planes, ships, and tanks, along with cluster bombs for planes.

> DLSS 5 does not completely change how War Thunder looks at first glance, and that's good, as players would like us to stick to our original visual style.

> The sheer number of subtle improvements is so significant that some members of the team initially thought we had changed the rendering engine itself.

> The main difficulty was color space: DLSS 5 works in sRGB, while the Dagor Engine renders in linear HDR. Gaijin made its color pipeline invertible so DLSS 5 could work on a semi-final image and its changes could be mapped back to linear HDR.

> The October 2026 neural rendering model that War Thunder launched with shrank DLSS 5's footprint by 24% to roughly 118 million parameters, and is 2X faster than the previous version, available for GeForce RTX 50 Series and RTX Spark systems.

> DLSS 5 With 3D-Guided Neural Rendering is a final stage in the graphics pipeline that uses the engine's rendered frame and motion vectors as its foundation to add lifelike lighting and material detail, with developers controlling where and how strongly it is applied.

> Advice to other developers: invest time in tuning it against your own art direction, as the results are well worth it.