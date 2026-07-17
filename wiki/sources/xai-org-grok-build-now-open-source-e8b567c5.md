---
fetched_at: &id001 2026-07-17
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: e8b567c5b8942a1cbde2d43e02ff2159f5044900037406ad5be123d8b07efe74
sources: []
title: xai-org/grok-build, now open source
topic: agentic-coding
url: https://simonwillison.net/2026/Jul/15/grok-build/
---

## Excerpts

> Grok Build contains 844,530 lines of Rust (calculated using SLOCCount tool, which excludes whitespace and comments) of which only around 3% appears to be vendored. The repo has just a single commit releasing the code, so sadly we don't get any insight into how the codebase developed over time.

> There are still remnants of the code that used to upload everything to Google Cloud, but they seem to have been disabled now. xai-grok-shell/src/upload/gcs.rs has code for uploading to a GCS bucket, and upload/trace.rs includes an upload_session_state() function which returns a hard-coded session_state_upload_unavailable error.

> In response to the backlash, with all retained data deleted, retention default off, and an open-source harness, they are offering complete user privacy.