---
title: "Running Python code in a sandbox with MicroPython and WASM"
kind: source
url: "https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/"
sha256: "e5fd9595ea4e9d6179bde03a31f929bcab1aa56f3dad50384efb02406ba6e2c2"
fetched_at: "2026-06-09"
topic: "agentic-coding"
image_count: 0
sources: []
last_updated: 2026-06-09
last_verified: 2026-06-09
freshness_window_days: 365
---

## Excerpts

> I want Datasette Agent to be able to generate and execute Python code safely. I've been experimenting with different approaches to running code in a sandbox for a few years, and I've now released an alpha package called micropython-wasm which I'm using for a code execution sandbox plugin for Datasette Agent called datasette-agent-micropython.

> The alpha bundles a lightly customized WASM build of MicroPython with a wrapper to execute code in it via wasmtime. The sandbox provides no host filesystem access unless an explicit read-only directory is preopened, no network capability, and configurable WebAssembly memory, fuel, and wall-clock controls.

> The trickiest piece to solve was persistent interpreter state — the WASM build exposes a single entry point which starts the interpreter, runs code and stops it at the end, which works for one-off scripts but for Datasette Agent I wanted variables and functions to stay resident in memory for reuse across multiple code execution calls. GPT-5.5 has so far failed to break out of the sandbox.
