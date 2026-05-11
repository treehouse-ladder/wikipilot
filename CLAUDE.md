# CLAUDE.md — Wikipilot wiki schema

You are maintaining a personal research wiki at `wiki/`, inspired by [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). This file is the single source of truth for **how** the wiki is structured and **what conventions** every routine, subagent, and skill must respect. Read it at the start of every routine run.

## The three layers

1. **Raw sources** — every URL the system has read is captured as one markdown file in `wiki/sources/<slug>.md`, with frontmatter (`url`, `sha256`, `fetched_at`, `topic`, `image_count`) and verbatim `>` excerpts. Source pages are append-only after creation; never edit them after they're committed.
2. **The wiki** — the LLM-generated synthesis layer: topic landing pages (`wiki/topics/<id>/index.md`), concept pages (`wiki/concepts/`), entity pages (`wiki/entities/`), answer pages (`wiki/answers/`), reports (`wiki/reports/`). The LLM owns this layer and keeps it consistent with the raw sources.
3. **The schema** — this file (`CLAUDE.md`) plus per-topic `wiki/topics/<id>/purpose.md` files. Human-owned; the LLM reads but never writes them.

## File ownership matrix

The wiki only stays maintainable if it's clear who owns each file. The Python lint enforces this; routines respect it.

### Human-only (LLM never modifies)

- `topics.yaml` — the list of topics being researched
- `CLAUDE.md`, `AGENTS.md` — the schema
- `wikipilot.toml` — operational config (auto-merge thresholds, image policy)
- `prompts/**` — versioned routine prompts
- `wiki/topics/<id>/purpose.md` — what each topic is/isn't
- `README.md`, `LICENSE`
- `.claude/agents/**`, `.claude/skills/**` — agent and skill definitions
- `docs/**` — all human-authored documentation

If a Claude branch (`claude/*`) modifies any of these files, the auto-merge gate **must block** and require human review.

### LLM-only (humans read, don't edit)

- `wiki/index.md` — the catalog
- `wiki/log.md` — chronological append-only journal
- `wiki/sources/**` — one file per ingested URL
- `wiki/reports/**` — daily run reports + weekly health reports
- `wiki/answers/**` — Wiki Query answer pages
- `wiki/decks/**` — Marp decks (`wikipilot deck` output)
- `wiki/assets/**` — downloaded images

### Mixed (LLM-write, human-edit allowed)

- `wiki/topics/<id>/index.md` — topic synthesis pages
- `wiki/concepts/**` — cross-topic concept pages
- `wiki/entities/**` — people, projects, orgs

When a human edits a mixed file, they should bump `last_verified` manually. The wiki-merger respects existing `## Disputes` and `## Open questions` content (append-only there — never delete an entry, only mark it resolved).

## Frontmatter contract

Every wiki page **except** `log.md` and `index.md` carries this frontmatter:

```yaml
---
title: "Concise human-readable title"
kind: topic | concept | entity | source | answer | report
sources: ["[[source-slug-1]]", "[[source-slug-2]]"]   # backrefs to source pages cited on this page
last_updated: 2026-05-11                              # set on every write
last_verified: 2026-05-11                             # set only when a researcher confirms claims still hold
freshness_window_days: 30                             # lint flags pages where now - last_verified > this
---
```

Source pages additionally carry: `url`, `sha256`, `fetched_at`, `topic`, `image_count`.
Answer pages additionally carry: `question`, `issue_url` (optional, when triggered by GitHub), `run_id`.
Report pages additionally carry: `run_id`, `routine` (`daily_research` | `wiki_query` | `weekly_health`).

## Standard page sections

Concept, entity, topic, and answer pages all share the same structure:

- `## Summary` — synthesis prose. **Every non-trivial claim must include an inline `[[source-slug]]` wikilink.** For each source cited at least once on a page, include one `>` quote block from the source as evidence.
- `## Disputes` — append-only. Each entry: `[[source-A]] claims X; [[source-B]] claims not-X. Status: unresolved | resolved-toward-A | resolved-toward-B`. Visible in Obsidian's graph view; researchers read these at the start of each run.
- `## Open questions` — append-only. Each entry: `- [ ] question text`. Researchers pull these into the next run's agenda.
- `## See also` — outbound `[[wikilinks]]` to related pages. The `query-back-fill` skill writes here when filing answer pages back into the wiki.

## Citation discipline (mandatory for `topic-researcher` and `query-answerer`)

- Every claim that isn't background context **must** have an inline `[[source-slug]]` wikilink.
- For each source cited at least once on a page, include one `>` quote block from the source as evidence.
- If no source supports a claim, file it under `## Open questions` instead of asserting it.
- If a candidate finding contradicts an existing claim, file the disagreement under the affected page's `## Disputes` rather than overwriting.

This addresses the recurring "lossy compression" critique — the wiki must be a faithful synthesis of its sources, not a paraphrase that drifts.

## Cross-page sweep (mandatory for `wiki-merger`)

When applying a proposal that touches concept X:

1. Update the topic landing page that owns X.
2. Update **every** concept/entity page that backlinks X (use Grep on `[[X]]` or the page's slug).
3. Update `wiki/index.md` for any new pages.
4. Bump `last_updated` and `last_verified` on every page modified.

Karpathy's "10–15 wiki pages per source" expectation is normal, not a red flag — the per-topic auto-merge gate is sized for it.

## Log format

`wiki/log.md` is chronological and append-only. Every entry uses this exact prefix so the log is parseable with `grep "^## \[" wiki/log.md`:

```markdown
## [YYYY-MM-DD] kind | subject

One-line summary.
```

Where `kind` is one of: `daily`, `query`, `health`, `manual`. Examples:

```markdown
## [2026-05-11] daily | ai-agents — 3 sources, 12 pages
## [2026-05-11] query | what is qmd? — answers/2026-05-11-what-is-qmd.md
## [2026-05-12] health | weekly sweep — 2 disputes filed
```

## Per-run report

After every routine run, the orchestrator writes `wiki/reports/YYYY-MM-DD.md` (or `health-YYYY-MM-DD.md` for the weekly routine). Required fields:

- Topics processed (ids), sources added (count + links), pages touched (count + paths)
- Runtime, model used per agent, token usage by tier
- Links to every PR opened (auto-merged or left open)
- Disputes newly raised, Open questions newly added

## Model selection (per-agent, set in `.claude/agents/*.md` frontmatter)

| Layer | Model | Rationale |
|---|---|---|
| Daily Research orchestrator | Sonnet | tool-use + control flow |
| Wiki Query orchestrator | Sonnet | tool-use + control flow |
| Weekly Health orchestrator | Sonnet | tool-use + control flow |
| `topic-researcher` | **Opus 4.7** | judgment-heavy synthesis at every ingest entry point |
| `wiki-merger` | Sonnet | mostly mechanical edits + cross-page sweep |
| `wiki-linter` | **Haiku** | Python linter does the analysis; agent only applies mechanical fixes |
| `query-answerer` | **Opus 4.7** | user-facing synthesis on demand |
| `wiki-disputes-scanner` | Sonnet | judgment task, but cost-sensitive (many pages × candidate sets); never auto-resolves disputes |

Routine-UI model picker only sets the orchestrator model; subagents pin their own model via YAML frontmatter.

## Daily run workflow (for `daily_runner.md` orchestrator)

1. Run `python scripts/preflight.py` — fail fast if env broken.
2. Read `CLAUDE.md`, `topics.yaml`, `wiki/index.md`, last 50 lines of `wiki/log.md`, every `wiki/topics/<id>/purpose.md`. This becomes the cache-warming prefix shared across parallel subagents.
3. Set `CLAUDE_CODE_FORK_SUBAGENT=1` and dispatch `topic-researcher` **in parallel** via the Task tool, one per enabled topic.
4. For each topic, in series: branch `claude/daily-YYYY-MM-DD/<topic-id>`, dispatch `wiki-merger`, dispatch `wiki-linter`, run `pytest` + `wikipilot lint wiki/`, append per-topic log entry, commit, push, `gh pr create`, `python scripts/maybe_automerge.py --pr <num>`.
5. After all topics: write `wiki/reports/YYYY-MM-DD.md`.

## Out of scope (intentionally)

- Sigma-guard structural contradiction detection (research-grade overkill)
- Embedding-based semantic sweep (the LLM-judge sweep handles practical cases; embeddings stay deferred)
- Hosted public-facing UI (Obsidian is the UI)

## Editing this file

This file co-evolves with the system. When you discover a new convention, add it here in the appropriate section. The Python lint and the agent system prompts both reference these conventions, so keep them tight and unambiguous.
