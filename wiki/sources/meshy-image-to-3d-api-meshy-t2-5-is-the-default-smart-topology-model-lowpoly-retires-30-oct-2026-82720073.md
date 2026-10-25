---
fetched_at: &id001 2026-10-25
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 82720073e36a19d5cba4eca32d3241807503265cd1294939bbb61cab32c894d4
sources: []
title: Meshy Image to 3D API — meshy-t2.5 is the default Smart Topology model; lowpoly
  retires 30 Oct 2026
topic: ai-in-game-dev
url: https://docs.meshy.ai/en/api/image-to-3d
---

Meshy's Image to 3D and Text to 3D API reference, as updated in the October 2026 developer changelog. Documents a new model id, meshy-t2.5, added on 15 October 2026 for Smart Topology output and now the default when model_type smart-topology is set without an explicit ai_model; it targets sharper detail for game assets, spans a 100-30,000 target_polycount range (default 15,000) and is priced the same as meshy-t2 (Multi-Image to 3D excepted). The legacy lowpoly model_type is scheduled to retire on 30 October 2026, after which model_type: lowpoly returns an error and users are directed to smart-topology with meshy-t2.5. Separately, the API changelog retired meshy-5 on 10 October 2026 (now a 400 error; replacement meshy-6-lite at the same credit cost) and switched USDZ exports to metres on 12 October 2026.

## Excerpts

> meshy-t2.5 (default): sharper detail for game assets.

> Meshy retires lowpoly on October 30, 2026. After that date, a request with model_type: "lowpoly" returns an error; the recommended replacement is smart-topology with meshy-t2.5.

> ai_model "meshy-t2.5" is available for Image to 3D and Text to 3D with a target_polycount range of 100 to 30,000 (default 15,000), priced the same as meshy-t2; omitting ai_model under smart-topology now selects t2.5. Multi-Image to 3D does not accept t2.5.