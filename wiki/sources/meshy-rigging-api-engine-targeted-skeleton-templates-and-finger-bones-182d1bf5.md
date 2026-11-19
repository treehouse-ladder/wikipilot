---
fetched_at: &id001 2026-11-19
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 182d1bf549874109bf7b05579c7c3fe0a3e1462a623a70b1848dd5a259890f2c
sources: []
title: Meshy Rigging API — engine-targeted skeleton templates and finger bones
topic: ai-in-game-dev
url: https://docs.meshy.ai/en/api/rigging
---

## Excerpts

> The skeleton_template parameter accepts meshyrig, mixamo, ue5_mannequin, max_biped, unity_humanoid, and maya_human_ik. v1 Rigging defaults to meshyrig, as before, and v2 Rigging defaults to mixamo.

> The template sets its bone names and hierarchy; a few end bones, such as headfront, keep their original names. With a value other than meshyrig, or with include_fingers set to true, the files are in meters and use that skeleton's bones, instead of the default 24-bone meshyrig files.

> include_fingers adds finger bones to the hands, but works only with a biped rig. With the meshyrig template, the finger bones use Mixamo names, such as LeftHandThumb1. Invalid combinations return an error, and Meshy doesn't charge for them.

> The input must be a textured humanoid model, a GLB file of at most 400 MB from an http or https URL (or 100 MB as a data URI), with at most 380,000 triangles. If a model can't be rigged on the chosen skeleton, the task fails; retry with meshyrig and include_fingers set to false.