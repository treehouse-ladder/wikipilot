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
3. Set `CLAUDE_CODE_FORK_SUBAGENT=1` and dispatch `topic-researcher` **in parallel** via the Task tool, one per enabled topic. Each returns a structured `Proposal` (schema below).
4. For each topic, in series: branch `claude/daily-YYYY-MM-DD/<topic-id>`, dispatch `wiki-merger`, dispatch `wiki-linter`, run `pytest` + `wikipilot lint wiki/`, append per-topic log entry, commit, push, `gh pr create`, `python scripts/maybe_automerge.py --pr <num>`.
5. After all topics: write `wiki/reports/YYYY-MM-DD.md`.

## Query workflow (for `query_answerer.md` orchestrator — Phase 6)

1. Run `python scripts/preflight.py`.
2. Read `CLAUDE.md`, `wiki/index.md`, recent `wiki/log.md` (cache-warming prefix).
3. Parse the question from the GitHub issue body (if triggered by `issue.opened` with the `query` label) or the API `text` field.
4. Dispatch `query-answerer` (Opus 4.7) with the question — qmd-search first, WebSearch only as fallback.
5. Apply the `Answer` to a fresh branch `claude/query-YYYY-MM-DD-<slug>`, run lint+tests.
6. Call `query-back-fill` to add `[[answer-slug]]` references to related concept/entity pages.
7. `gh pr create`; `python scripts/maybe_automerge.py --pr <num>` with the `wiki_query` gate.
8. If GitHub-triggered, `gh issue comment` on the originating issue with the answer summary + page link + PR link.

## Weekly health workflow (for `weekly_health.md` orchestrator — Phase 7)

1. Run `python scripts/preflight.py`.
2. Read `CLAUDE.md`, `wiki/index.md`, last 200 lines of `wiki/log.md` (broader cache prefix because the sweep is wiki-wide).
3. Run `python scripts/disputes_seed.py` to produce candidate sets.
4. Dispatch `wiki-disputes-scanner` **per candidate set in parallel** with `CLAUDE_CODE_FORK_SUBAGENT=1`.
5. Apply all dispute proposals to a single branch `claude/health-YYYY-MM-DD` (append-only edits to `## Disputes` sections; never resolves anything).
6. Run `wikipilot freshness-report` and `wikipilot lint wiki/`; append summaries to the health report.
7. Write `wiki/reports/health-YYYY-MM-DD.md`.
8. `gh pr create`; auto-merge per the permissive `weekly_health` gate.

## Schemas

### Proposal (returned by `topic-researcher`)

```json
{
  "topic_id": "<id from topics.yaml>",
  "sources": [
    {
      "url": "https://...",
      "title": "Source title",
      "excerpt": "Verbatim quote(s) for the > evidence block(s).",
      "image_urls": ["https://...", "..."]
    }
  ],
  "page_diffs": [
    {
      "path": "topics/<id>/index.md | concepts/<slug>.md | entities/<slug>.md",
      "kind": "topic | concept | entity",
      "summary_addition": "Prose with [[source-slug]] inline citations and a > quote block.",
      "new_disputes": ["[[A]] claims X; [[B]] claims not-X. Status: unresolved"],
      "new_open_questions": ["What about under FP8?"]
    }
  ],
  "new_disputes": ["..."],
  "new_open_questions": ["..."]
}
```

### Answer (returned by `query-answerer`)

```json
{
  "question": "<verbatim user question>",
  "answer_slug": "YYYY-MM-DD-<slug>",
  "summary": "## Summary\n\n... [[source-slug]] ... \n\n> quote ...\n\n## See also\n- [[related]]",
  "sources": [{"url": "...", "title": "...", "excerpt": "..."}],
  "related_pages": ["concept-slug-1", "entity-slug-2"],
  "issue_url": "https://github.com/.../issues/N",
  "run_id": "..."
}
```

### Disputes-candidate (returned by `wiki-disputes-scanner`)

```json
{
  "trigger": "source_<slug> | stale_sweep",
  "disputes_filed": [
    {
      "page": "wiki/concepts/<slug>.md",
      "confidence": "high | medium | low",
      "summary": "Short one-line description of the dispute.",
      "evidence_quotes": ["> quote A", "> quote B"]
    }
  ],
  "pages_examined": ["wiki/concepts/a.md", "wiki/concepts/b.md"]
}
```

## Out of scope (intentionally)

- Sigma-guard structural contradiction detection (research-grade overkill)
- Embedding-based semantic sweep (the LLM-judge sweep handles practical cases; embeddings stay deferred)
- Hosted public-facing UI (Obsidian is the UI)

## Wiki schema (canonical, enforced by `wikipilot lint`)

The Phase 1 Python lint is the gatekeeper for everything in this section. Run `uv run wikipilot lint wiki/` locally; the same command runs in CI (Phase 3) and gates auto-merge.

### Frontmatter (required keys)

`title`, `kind`, `sources` (list), `last_updated`, `last_verified`, `freshness_window_days`. All required on every wiki page except `wiki/log.md`, `wiki/index.md`, and `wiki/topics/<id>/purpose.md`.

`kind` must be one of: `topic`, `concept`, `entity`, `source`, `answer`, `report`.

`last_updated` and `last_verified` are ISO dates (`YYYY-MM-DD`). The merger must bump `last_updated` on every write; researchers must bump `last_verified` only when they have re-confirmed the page's claims hold.

### Source pages

Source pages live in `wiki/sources/<slug>.md`, where `<slug>` is `<title-slugified>-<sha-prefix-8>`. Dedupe is by SHA-256 of the *normalized* URL (lowercased scheme/host, sorted query params, fragment stripped, trailing slash stripped) — re-ingesting the same URL is a no-op rather than a duplicate. Required source frontmatter: `url`, `sha256`, `fetched_at`, `topic`, `image_count`, plus the standard frontmatter (with `freshness_window_days: 365` since sources don't go stale the way synthesis pages do). Body must include a `## Excerpts` section with at least one `>` quote block per cited claim — this is the evidence layer the citation discipline rule depends on.

### `log.md` format

Every entry: `## [YYYY-MM-DD] kind | subject` followed by a one-line summary. `kind` in `{daily, query, health, manual}`. The lint rejects any `## ` heading in `log.md` outside a fenced code block that doesn't match this schema. Greppable with `grep "^## \[" wiki/log.md` (Karpathy's idiom).

### Lint rules (`wikipilot lint wiki/`)

| Rule | Severity | What it checks |
|---|---|---|
| `frontmatter` | error | required keys present, kind valid, dates parse, types match |
| `log-format` | error | every `## ` heading in `log.md` matches the schema (code blocks excluded) |
| `broken-wikilink` | error | every `[[link]]` resolves to a known page slug or alias |
| `orphan-page` | warning | synthesis pages with zero inbound links |
| `stale-page` | warning | `now - last_verified > freshness_window_days` (page-level override; default 30) |
| `citation-density` | warning | `## Summary` paragraphs without any `[[wikilink]]` (default min: 1 per paragraph) |
| `disputes-format` | warning | `## Disputes` entries that aren't `- ... claims ... Status: ...` bullets |
| `open-questions-format` | warning | `## Open questions` entries that aren't `- [ ] ...` checkboxes |
| `ownership-violation` | error | only fires when `--branch claude/...` and `--changed-path ...` are passed; flags any human-only path being modified on a Claude branch |

Errors fail the lint (exit code 1); warnings are reported but don't fail. The auto-merge gate (Phase 3) blocks any PR where the lint reports errors *or* the changed paths trip the ownership-violation check.

### CLI surface (`wikipilot --help`)

| Subcommand | Purpose |
|---|---|
| `lint [vault] [--branch ... --changed-path ...]` | run all lint rules; exits 1 on any error |
| `init-vault [path]` | create the standard `wiki/{index.md, log.md, ...}` skeleton |
| `validate-topics [topics.yaml]` | parse + schema-check `topics.yaml` |
| `freshness-report [vault]` | list pages by ascending freshness (most stale first) |
| `deck <topic-id> [--out path] [--theme name]` | generate a Marp deck from `wiki/topics/<id>/index.md` |
| `index-wiki [vault] [--full]` | refresh the qmd index over the vault |
| `research [--topic id]` | trigger Daily Research routine via the `/fire` API (Phase 6) |
| `query "<question>"` | trigger Wiki Query routine via the `/fire` API (Phase 6) |

## Editing this file

This file co-evolves with the system. When you discover a new convention, add it here in the appropriate section. The Python lint and the agent system prompts both reference these conventions, so keep them tight and unambiguous.
