# Daily brief curator — ranking rubric

This is the rubric the `daily-brief-curator` subagent applies to every Daily Research run when picking what lands in `## Today's brief`. It encodes the user's anchor priorities so the editorial filter is consistent run-to-run.

## Anchor priorities

The user is optimizing two things, intentionally cross-cutting:

1. **Make the best games they possibly can.** Single-player and small-team scope. Anything that raises the ceiling of what's achievable as a small studio is in-scope.
2. **Run the most-optimized agentic-coding workflow possible.** Parallel sub-agents, prompt caching, MCP, IDE-level affordances. Anything that reduces friction, raises ceiling, or cuts cost in that loop is in-scope.

A bullet that matters for **either** anchor qualifies. A bullet that matters for **both** is a near-automatic top-3 placement.

## Tier definitions

### Tier 1 — must-read (always include if today's run produced one)

A Tier 1 item is something that, if the user missed it, they'd have made worse decisions tomorrow. Concrete patterns:

- **A new model leads a benchmark the user cares about** (any `[frontier_models].benchmarks` column #1 swap) AND the cost is competitive — they'd switch their daily-driver. Citation MUST include the `entity_field_updates` source.
- **A model gets dramatically cheaper for the user's workload** (cost cliff > 30% drop, or new context-tier pricing that benefits long codebases) — they'd re-evaluate their per-token budget for parallel-agent sessions.
- **A new generation-AI tool ships that can replace a step in the user's game-dev pipeline.** Examples: mocap-to-rig with measurable retargeting accuracy; text-to-3D that produces hero-quality (not just background) meshes; in-engine NPC dialog with adaptive memory; AI playtesting with measured coverage uplift.
- **A new agentic-coding technique with measured uplift** in a publishable harness — e.g. a parallel-sub-agent pattern with measured terminal-bench/SWE-bench delta; a prompt-caching pattern with measured token-cost reduction. Vendor blog ≠ measurable result.

### Tier 2 — high-signal novelty (include if Tier 1 budget isn't full)

- **A genuinely new technique** — not a vendor product launch — with at least one quantitative claim and the methodology to back it.
- **A capability the user didn't have a wiki page for yesterday** that's now demonstrably achievable (with measurement).
- **A new benchmark or evaluation harness** that changes how the user should think about a category (e.g. a successor to SWE-bench that closes a known gap).

### Tier 3 — industry shift worth knowing (include if Tier 1 + Tier 2 still leave room)

- **Studio closure / acquisition / strike** that affects the user's competitive landscape (publisher consolidation, mocap pipeline acquisition, etc.).
- **A regulatory or platform shift** that changes shipping economics for small studios.
- **An ecosystem signal** the user should integrate into their mental model (e.g. an open-weights model crossing a capability threshold; a dev tool getting deprecated).

### Pad-only-on-empty-day

If today's run truly produced fewer than 3 Tier-1/2/3 items, output FEWER bullets — never reach for Tier-4 filler. A short brief is a signal in itself.

## Anti-patterns

These are bullets the curator should NEVER ship, even if they technically meet a tier:

- **Vendor announcement with no methodology.** "X launched Y" without measured numbers, comparisons, or a methodology section.
- **Restated background.** Anything the user could derive from yesterday's report alone — fast a a sanity check, re-read yesterday's `## Today's brief`; if the bullet roughly matches one from there, don't repeat it.
- **Hype without a concrete next step the user could take.** "AI is changing X" is not actionable.
- **A benchmark interpretation that diverges from the configured `[frontier_models].benchmark_glosses` gloss.** The user has aligned their mental model with those one-liners — don't redefine them.
- **A bullet without a `[[source-slug]]` citation.** No exceptions.

## Brief-shape conventions

Each bullet ends up like this:

```markdown
- **[[entity-or-finding-name]]**: <one-sentence "what happened"> [[source-slug]]. **Why it matters to you:** <one-sentence concrete impact, framed in agentic-workflow or game-dev terms>.
```

Examples:

- `- **[[claude-opus-4.7]]**: took #1 on **GDPval-AA Elo** with a 79-Elo lead [[claude-opus-47-everything-you-need-to-know-751c1827]]. **Why it matters to you:** real-world economic-task quality vs. human experts — high score = ships agentic work to production with fewer reverts.`
- `- **[[mocapanything-v2]]**: end-to-end mocap for arbitrary skeletons, no per-rig retargeting step [[mocapanything-v2-end-to-end-motion-capture-for-arbitrary-skeletons-d09ec008]]. **Why it matters to you:** could replace the Radical / Move.ai step in your character pipeline.`

## Notes for future curators

- The rubric is intentionally tilted toward **measured** evidence. If you find yourself drafting bullets with no number in them, scrutinize them harder before they ship.
- When in doubt between Tier 1 and Tier 2, default Tier 2 — Tier 1 should feel like a "did this really change my decisions?" gate, not a "is this interesting?" gate.
- The watchlist exists so good-but-not-must-read items have a home that's still visible. Use it generously rather than dropping signal entirely.
