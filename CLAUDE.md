# CLAUDE.md — Wikipilot wiki schema

You are maintaining a personal research wiki at `wiki/`, inspired by [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). This file is the single source of truth for **how** the wiki is structured and **what conventions** every routine, subagent, and skill must respect. Read it at the start of every routine run.

## The three layers

1. **Raw sources** — every URL the system has read is captured as one markdown file in `wiki/sources/<slug>.md`, with frontmatter (`url`, `sha256`, `fetched_at`, `topic`, `image_count`) and verbatim `>` excerpts. Source pages are append-only after creation; never edit them after they're committed.
2. **The wiki** — the LLM-generated synthesis layer: topic landing pages (`wiki/topics/<id>/index.md`), concept pages (`wiki/concepts/`), entity pages (`wiki/entities/`), comparison pages (`wiki/comparisons/`), answer pages (`wiki/answers/`), reports (`wiki/reports/`). The LLM owns this layer and keeps it consistent with the raw sources.
3. **The schema** — this file (`CLAUDE.md`) plus per-topic `wiki/topics/<id>/purpose.md` files. Human-owned; the LLM reads but never writes them.

### Three-tier framing (from the gist comment thread)

The same three layers framed by intent rather than by directory:

- **Facts** — `purpose.md` per topic + `topics.yaml` + this file. Immutable user guidance; the LLM consults these but cannot edit them.
- **Working memory** — `wiki/sources/`. Raw ingest snapshots (URL + verbatim excerpts + assets); append-only, never re-edited after commit.
- **Wisdom** — `wiki/topics/`, `wiki/concepts/`, `wiki/entities/`, `wiki/comparisons/`, `wiki/answers/`. Curated synthesis that distills the working memory through the lens of the facts.

## Cross-cutting relevance criteria

The `topic-researcher` agent and the `query-answerer` agent both consult these criteria *together with* the topic's `purpose.md` (which narrows further with topic-specific in-scope/out-of-scope). A candidate source is worth ingesting when **any one** of the following is true:

1. **Highly relevant** to the topic's charter (in-scope per `purpose.md`).
2. **Highly innovative** — novel technique, approach, or capability worth knowing about even if adjacent to the strict charter.
3. **Directly impacts or improves any aspect of agentic workflow OR video game development** — these are the user's two anchor domains, intentionally cross-cutting. A `frontier-models` source that materially helps an agentic-coding workflow still qualifies; an `ai-in-game-dev` paper that improves an agentic content pipeline still qualifies.

**Inclusion bias: when on the fence, include rather than exclude.** Better to ingest a slightly-too-broad source the user can prune later than to silently drop a genuinely interesting one. Tightening happens via charter and rubric edits over time, observed from the daily run reports — not via numeric quotas.

`topics.yaml` per-topic `max_sources_per_run` (default 20) is a **safety cap, not a quality lever**. With these criteria the realistic flow is 5–12 sources per topic per busy day; hitting 20 is a runaway-day signal that should trip the auto-merge gate so a human reviews the run (see "Tuning auto-merge thresholds" in [`docs/runbook.md`](docs/runbook.md)).

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
- `wiki/comparisons/**` — N-way comparison tables (Phase 9 Pattern A)

When a human edits a mixed file, they should bump `last_verified` manually. The wiki-merger respects existing `## Disputes` and `## Open questions` content (append-only there — never delete an entry, only mark it resolved).

### Personal scratch convention (`_*.md`, human-only)

Any markdown file whose name starts with `_` is **personal scratch**: `wiki/_dashboard.md`, `wiki/_inbox.md`, `wiki/concepts/_local-notes.md`, etc. These files are:

- **Exempt from the schema lint** — no frontmatter required, no citation density, no orphan check (`_is_lint_exempt` in `wikipilot.lint`).
- **Exempt from the cross-page sweep** — agents do not read, link to, or modify them.
- **Treated as human-only by the auto-merge gate** — any `claude/*` PR that touches a `_*.md` file is blocked the same way it is for `CLAUDE.md` or `topics.yaml`.

Use them for dashboards (Dataview-driven status pages), reading inboxes, personal notes, or anything else that lives in the vault but isn't part of the wiki's canonical knowledge layer. The Obsidian setup ships with `wiki/_dashboard.md` as a starter; see [`docs/obsidian-setup.md`](docs/obsidian-setup.md) for the workflow that uses it.

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
Comparison pages additionally carry: `comparison_of` (list of ≥ 2 entity slugs) and `compare_fields` (list of ≥ 1 frontmatter field name to aggregate).
Entity pages MAY carry: `aliases` (list of strings) — Obsidian-native aliases that resolve in `[[wikilinks]]` so `[[GPT-4]]`, `[[GPT 4]]`, `[[gpt4]]` all resolve to the same entity page when the entity declares them.

## Standard page sections

Concept, entity, topic, and answer pages all share the same structure:

- `## Summary` — synthesis prose. **Every non-trivial claim must include an inline `[[source-slug]]` wikilink.** For each source cited at least once on a page, include one `>` quote block from the source as evidence.
- `## Disputes` — append-only. Each entry: `[[source-A]] claims X; [[source-B]] claims not-X. Status: unresolved | resolved-toward-A | resolved-toward-B`. Visible in Obsidian's graph view; researchers read these at the start of each run.
- `## Open questions` — append-only. Each entry: `- [ ] question text`. Researchers pull these into the next run's agenda.
- `## See also` — outbound `[[wikilinks]]` to related pages. The `query-back-fill` skill writes here when filing answer pages back into the wiki.

### Divergence-check sentinel

Every synthesis page (`topic`, `concept`, `entity`, `answer`) MUST end up with at least one of (a) a `## Disputes` entry, (b) a `## Open questions` entry, or (c) the literal sentinel below somewhere in the body:

```markdown
_no contradictions or gaps known yet (last reviewed: YYYY-MM-DD)_
```

The `divergence-discipline` lint warns when none of the three are present. Easy to satisfy with the one-line sentinel; the point is to force the author to actively look for counter-arguments before claiming there are none. Comparison pages are excluded — they're tables aggregated from entity pages, not prose synthesis.

## Citation discipline (mandatory for `topic-researcher` and `query-answerer`)

- Every claim that isn't background context **must** have an inline `[[source-slug]]` wikilink.
- For each source cited at least once on a page, include one `>` quote block from the source as evidence.
- If no source supports a claim, file it under `## Open questions` instead of asserting it.
- If a candidate finding contradicts an existing claim, file the disagreement under the affected page's `## Disputes` rather than overwriting.

This addresses the recurring "lossy compression" critique — the wiki must be a faithful synthesis of its sources, not a paraphrase that drifts.

## Comparison pages

Phase 9 introduces `comparison` as a first-class wiki kind alongside `concept` / `entity`. A comparison page surfaces N-way data (or N-way disagreement) for a set of related entities — e.g. `cost-comparison` reads `cost_per_mtoken` from each frontier-model entity, `agentic-ide-comparison` reads parallel-subagent / prompt-caching / MCP support from each agentic-IDE entity.

- **Location**: `wiki/comparisons/<slug>.md`.
- **Frontmatter**: standard fields plus `comparison_of: [entity-slug-1, entity-slug-2, ...]` (≥ 2 entries) and `compare_fields: [field-name-1, ...]` (≥ 1 entry).
- **Body**: a generated markdown table; one row per entity, one column per field. Cells render as `_unknown_` when the entity page omits the field — that's the explicit signal to backfill the value on the entity, not the comparison.
- **Lifecycle**: create with `wikipilot compare new <slug> --of <e1,e2> --fields <f1,f2> --title "..."`; regenerate with `wikipilot compare regen <slug>`. Regeneration re-reads frontmatter and rewrites the body; idempotent (`last_updated` bumps to today, `last_verified` is left alone).
- **Lint exclusions**: comparison pages are NOT subject to `citation-density` (the table is the synthesis; cited claims live on the entity pages) or `orphan-page` (comparisons are referenced from topic indices, but a missing backlink shouldn't block).

## Entity aliases

Obsidian-native `aliases:` frontmatter (Phase 9 Pattern C). Lets `[[GPT-4]]`, `[[GPT 4]]`, `[[gpt4]]` all resolve to the same entity page when the entity declares them. The lint's `broken-wikilink` and `orphan-page` rules both consult aliases when resolving links.

```yaml
---
title: "GPT-4"
kind: entity
aliases: ["GPT 4", "gpt4", "OpenAI GPT-4"]
sources: ["[[some-source-deadbeef]]"]
last_updated: 2026-05-12
last_verified: 2026-05-12
freshness_window_days: 60
---
```

Recommended for entity pages with multiple common names: model versions (e.g. `claude-opus-4.7` / `Claude Opus 4.7` / `Opus 4.7`), products with hyphen/space variants (e.g. `claude-code` / `Claude Code`), and legacy names that get retconned.

## Divergence check

Phase 9 Pattern B. The `divergence-discipline` lint warns when a synthesis page (`topic`, `concept`, `entity`, `answer`) has empty `## Disputes`, empty `## Open questions`, AND no sentinel anywhere in the body. The sentinel format is verbatim:

```markdown
_no contradictions or gaps known yet (last reviewed: YYYY-MM-DD)_
```

Severity is warning (not error) — a fresh page can land without blocking auto-merge, but the `topic-researcher`, `wiki-merger`, and `query-answerer` agents are all instructed to satisfy the rule on every page they create or modify. The intent (from the gist comment thread) is to force the author to actively look for counter-arguments before claiming there are none.

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
| PR Watcher orchestrator | Sonnet | tool-use + control flow; no synthesis (re-runs the deterministic gate after CI) |
| `topic-researcher` | **Opus 4.7** | judgment-heavy synthesis at every ingest entry point |
| `wiki-merger` | Sonnet | mostly mechanical edits + cross-page sweep |
| `wiki-linter` | **Haiku** | Python linter does the analysis; agent only applies mechanical fixes (also dispatched by PR Watcher for self-heal) |
| `query-answerer` | **Opus 4.7** | user-facing synthesis on demand |
| `wiki-disputes-scanner` | Sonnet | judgment task, but cost-sensitive (many pages × candidate sets); never auto-resolves disputes |

Routine-UI model picker only sets the orchestrator model; subagents pin their own model via YAML frontmatter.

## Daily run workflow (for `daily_runner.md` orchestrator)

The canonical prompt lives at [`prompts/daily_runner.md`](prompts/daily_runner.md). The cloud routine setup is documented in [`docs/routines-setup.md`](docs/routines-setup.md).

1. Run `python scripts/preflight.py` — fail fast if env broken.
2. Read `CLAUDE.md`, `topics.yaml`, `wiki/index.md`, last 50 lines of `wiki/log.md`, every `wiki/topics/<id>/purpose.md`. This becomes the cache-warming prefix shared across parallel subagents.
3. Set `CLAUDE_CODE_FORK_SUBAGENT=1` and dispatch `topic-researcher` **in parallel** via the Task tool, one per enabled topic. Each returns a structured `Proposal` (schema below).
4. For each topic, in series: branch `claude/daily-YYYY-MM-DD/<topic-id>`, dispatch `wiki-merger`, dispatch `wiki-linter`, run `pytest` + `wikipilot lint wiki/`, append per-topic log entry, commit, push, `gh pr create`, `python scripts/maybe_automerge.py --pr <num> --route daily_research`.
5. After all topics: write `wiki/reports/YYYY-MM-DD.md`.

## Query workflow (for `query_answerer.md` orchestrator)

The canonical prompt lives at [`prompts/query_answerer.md`](prompts/query_answerer.md). The cloud routine setup (including the GitHub-issue trigger) is documented in [`docs/routines-setup.md`](docs/routines-setup.md#wiki-query-routine).

1. Run `python scripts/preflight.py`.
2. Read `CLAUDE.md`, `wiki/index.md`, recent `wiki/log.md` (cache-warming prefix).
3. Parse the question from the GitHub issue body (if triggered by `issue.opened` with the `query` label) or the API `question` field.
4. Dispatch `query-answerer` (Opus 4.7) with the question — qmd-search first, WebSearch only as fallback.
5. Apply the `Answer` to a fresh branch `claude/query-YYYY-MM-DD-<slug>`, run lint+tests.
6. Call `query-back-fill` to add `[[answer-slug]]` references to related concept/entity pages.
7. `gh pr create`; `python scripts/maybe_automerge.py --pr <num> --route wiki_query`.
8. If GitHub-triggered, `gh issue comment` on the originating issue with the answer summary + page link + PR link.

## Weekly health workflow (for `weekly_health.md` orchestrator)

The canonical prompt lives at [`prompts/weekly_health.md`](prompts/weekly_health.md). The cloud routine setup is documented in [`docs/routines-setup.md`](docs/routines-setup.md#weekly-health-routine).

1. Run `python scripts/preflight.py`.
2. Read `CLAUDE.md`, `wiki/index.md`, last 200 lines of `wiki/log.md` (broader cache prefix because the sweep is wiki-wide).
3. Run `python scripts/disputes_seed.py --json` to produce candidate sets.
4. Dispatch `wiki-disputes-scanner` **per candidate set in parallel** with `CLAUDE_CODE_FORK_SUBAGENT=1`.
5. Apply all dispute proposals to a single branch `claude/health-YYYY-MM-DD` (append-only edits to `## Disputes` sections; never resolves anything).
6. Run `wikipilot freshness-report` and `wikipilot lint wiki/`; append summaries to the health report.
7. Write `wiki/reports/health-YYYY-MM-DD.md`.
8. `gh pr create`; `python scripts/maybe_automerge.py --pr <num> --route weekly_health` (permissive gate).

## Per-PR workflow (for `pr_watcher.md` orchestrator)

The canonical prompt lives at [`prompts/pr_watcher.md`](prompts/pr_watcher.md). The cloud routine setup is documented in [`docs/routines-setup.md`](docs/routines-setup.md#pr-watcher-routine).

Unlike the three content-producing routines, the PR Watcher **does not write to the wiki**. It exists to close the race condition where each content routine calls `scripts/maybe_automerge.py` immediately after `gh pr create` — *before* CI populates the rollup — so an empty `statusCheckRollup` is treated as green and `gh pr merge --squash --auto` is queued without ever knowing whether the lint/test signal the gate requires actually passed. It also rescues PRs that never had `maybe_automerge.py` run at all (manual pushes to `claude/*`, content-routine sessions that crashed mid-loop, etc.).

1. Triggered by GitHub webhook on `pull_request.opened` and `pull_request.synchronize`, filtered to `base=main`, `is_draft=false`, `is_merged=false`.
2. Run `python scripts/preflight.py` (no `wikipilot index-wiki` — the watcher never searches the vault).
3. Read `CLAUDE.md`, `wikipilot.toml` (gate thresholds and `[automerge.pr_watcher]`), last 30 lines of `wiki/log.md`.
4. Parse the PR number and head ref from the trigger payload; defensively re-check `gh pr view --json state,isDraft,baseRefName`. Exit if any guardrail fails.
5. Invoke `python scripts/pr_watcher_gate.py --pr <num>` which:
   a. Calls `wikipilot.git_ops.infer_route_from_branch(head, config)` to map the head to `daily_research` / `wiki_query` / `weekly_health` / `None`.
   b. **Trust check.** Even when (a) returns a route, the script re-checks the PR author via `gh pr view --json isCrossRepository,author` plus `gh api repos/<owner>/<repo>/pulls/<n>` (the REST API exposes `author_association`, the CLI does not). The PR is treated as enforce-eligible only when `isCrossRepository=false` AND the author's `author_association` is in `[automerge.pr_watcher].trusted_associations` (default `OWNER,MEMBER,COLLABORATOR`) OR the author's login is in `trusted_authors`. Untrusted PRs are demoted to `read_only` mode regardless of how the branch name is shaped. Fail-closed: any gh failure during the check (network blip, missing scope, ambiguous owner/repo) is treated as untrusted. This is what stops a fork PR with a synthetic `claude/daily-…` head ref from coercing the watcher into queueing auto-merge.
   c. Waits up to `[automerge.pr_watcher].ci_wait_timeout_sec` (default 1200s) for `gh pr checks --watch`.
   d. Calls `apply_gate(..., mode="enforce")` for trusted `claude/*` PRs or `mode="read_only"` for human / non-routine / untrusted heads. Uses dedupe key `wikipilot:gate` so re-runs *edit* the existing comment instead of spamming.
   e. On enforce + red CI, calls `gh pr merge --disable-auto` to undo any prior premature queue from the in-routine `maybe_automerge.py` call.
6. If the gate script prints `HEAL_NEEDED pr=<n> next_attempt=<m>` (CI is red on `claude/*` and attempts < `self_heal_max_attempts`): add label `wikipilot:heal-attempt-<m>`, dispatch `wiki-linter` (Haiku) for mechanical fixes, commit `fix(wiki): wiki-linter mechanical fixes (attempt <m>)`, push. The push fires `pull_request.synchronize` and a fresh watcher session runs the cycle again.
7. If the gate script prints `HEAL_CAPPED pr=<n> attempt=<m> max=<k>`: do nothing further. The script has already posted a `## Self-heal cap reached` comment under the `wikipilot:heal-cap` dedupe key.
8. Only append a `manual` entry to `wiki/log.md` when something noteworthy happened (heal commit, cap reached, unusual gate outcome). Routine pass/fail comments stay on the GitHub PR thread.

Manual recovery: `wikipilot recover-prs` enumerates every open `claude/*` PR to `main` and runs `apply_gate` on each, inferring the route per PR. Use it when the watcher misfires or to clear a backlog of stranded PRs from before the watcher was wired up. The trust check above lives in the PR Watcher only; `recover-prs` assumes the operator is already vetting which PRs they want gated.

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

## Commit policy

Each routine produces one PR with conventional commits and per-route branch names. The auto-merge gate (Phase 3) decides whether the PR self-merges or stays open for human review.

### Branch naming (set in `wikipilot.toml [branches]`)

| Routine | Template | Example |
|---|---|---|
| Daily Research | `claude/daily-{date}/{topic_id}` | `claude/daily-2026-05-11/ai-agents` |
| Wiki Query | `claude/query-{date}-{slug}` | `claude/query-2026-05-11-what-is-qmd` |
| Weekly Health | `claude/health-{date}` | `claude/health-2026-05-17` |

The `claude/` prefix is required by Claude Code Cloud Routines (cloud routines can only push to `claude/*` branches by default).

### Commit messages

Conventional commits, one staged commit per branch:

| Routine | Commit message format |
|---|---|
| Daily Research | `feat(wiki/<topic-id>): daily research <YYYY-MM-DD> — N sources, M pages` |
| Wiki Query | `feat(wiki/answers): <slug> — answer for "<question>"` |
| Weekly Health | `feat(wiki/reports): weekly health <YYYY-MM-DD> — N disputes filed` |

### PR titles

| Routine | PR title format |
|---|---|
| Daily Research | `wiki(<topic-id>): daily YYYY-MM-DD` |
| Wiki Query | `wiki(answers): "<question>"` |
| Weekly Health | `wiki(health): weekly sweep YYYY-MM-DD` |

### PR body (templated by `wikipilot.git_ops.render_pr_body_*`)

- Daily: topic, sources added (URLs), pages touched, new disputes, new open questions, link to `wiki/reports/YYYY-MM-DD.md`.
- Query: question, answer page path, sources added, back-filled pages, originating issue URL (if any).
- Health: disputes newly filed, stale pages, lint summary, link to `wiki/reports/health-YYYY-MM-DD.md`.

### Auto-merge gate

Per `wikipilot.toml [automerge.*]`, the gate evaluates:

1. **Common (`[automerge.common]`)**: CI checks green (`require_lint_green`, `require_tests_green`); block any PR touching a human-only path (`block_human_only_file_changes`).
2. **Per-route**: file count and total diff lines under thresholds — daily uses `*_per_topic` (sized for ~15 page touches per source), wiki_query uses smaller per-question sizes, weekly_health is permissive.

If every criterion passes: `gh pr merge --squash --auto`. Otherwise: `gh pr comment` with a structured review checklist explaining which criteria tripped.

The gate logic lives in `wikipilot.git_ops.evaluate_gate` (pure function, fully unit-tested with mocked `gh`); the `scripts/maybe_automerge.py` shim wires it to a CLI the orchestrators call.

## Wiki schema (canonical, enforced by `wikipilot lint`)

The Phase 1 Python lint is the gatekeeper for everything in this section. Run `uv run wikipilot lint wiki/` locally; the same command runs in CI (Phase 3) and gates auto-merge.

### Frontmatter (required keys)

`title`, `kind`, `sources` (list), `last_updated`, `last_verified`, `freshness_window_days`. All required on every wiki page except `wiki/log.md`, `wiki/index.md`, and `wiki/topics/<id>/purpose.md`.

`kind` must be one of: `topic`, `concept`, `entity`, `source`, `answer`, `report`.

`last_updated` and `last_verified` are ISO dates (`YYYY-MM-DD`). The merger must bump `last_updated` on every write; researchers must bump `last_verified` only when they have re-confirmed the page's claims hold.

### Source pages

Source pages live in `wiki/sources/<slug>.md`, where `<slug>` is `<title-slugified>-<sha-prefix-8>`. Dedupe is by SHA-256 of the *normalized* URL (lowercased scheme/host, sorted query params, fragment stripped, trailing slash stripped) — re-ingesting the same URL is a no-op rather than a duplicate. Required source frontmatter: `url`, `sha256`, `fetched_at`, `topic`, `image_count`, plus the standard frontmatter (with `freshness_window_days: 365` since sources don't go stale the way synthesis pages do). Body must include a `## Excerpts` section with at least one `>` quote block per cited claim — this is the evidence layer the citation discipline rule depends on.

#### Source images (Phase 5)

Source pages must be **self-contained**: every image referenced from a source page lives under `wiki/assets/<source-slug>/` so the wiki survives the original URLs disappearing. The `download-source-images` skill (driven by `wikipilot ingest`) handles this:

- **Storage**: `wiki/assets/<source-slug>/<sha256_8>-<basename>.<ext>`. The SHA prefix prevents collisions when two URLs share a basename; the basename keeps filenames recognizable in Obsidian.
- **Allowed MIMEs** (defaults, override in `wikipilot.toml [images]`): `image/png`, `image/jpeg`, `image/gif`, `image/webp`, `image/svg+xml`. Both the response `Content-Type` header **and** a first-bytes magic-number sniff must point at an allowed MIME before the file is written. A mismatch (e.g. server returns `text/html` but bytes look like PNG) is skipped with reason `mime-mismatch`.
- **Size cap** (default 5 MB): enforced both via `Content-Length` header and a streaming hard-stop so partial downloads don't survive.
- **Reference rewriting**: every `![alt](remote-url)` and `<img alt="..." src="remote-url">` becomes `![alt](../assets/<slug>/<file>)` / `<img alt="..." src="../assets/<slug>/<file>">`. Alt text is preserved verbatim.
- **Orphan cleanup**: when `[images] cleanup_orphans = true` (default), files in `wiki/assets/<slug>/` that aren't in the post-rewrite mapping are removed at ingest time.
- **Disabling**: set `[images] enabled = false` in `wikipilot.toml`. Source pages then keep their original remote image URLs.
- **Lint**: `broken-image-ref` is an error — any local image ref that doesn't resolve to a file fails the lint and blocks auto-merge.

The image step runs **only on first ingest** of a URL (idempotency: re-ingesting an existing source returns the existing slug with no work done). If the image pipeline must be re-run for an existing source, delete the source page and re-ingest.

### `log.md` format

Every entry: `## [YYYY-MM-DD] kind | subject` followed by a one-line summary. `kind` in `{daily, query, health, manual}`. The lint rejects any `## ` heading in `log.md` outside a fenced code block that doesn't match this schema. Greppable with `grep "^## \[" wiki/log.md` (Karpathy's idiom).

### Lint rules (`wikipilot lint wiki/`)

| Rule | Severity | What it checks |
|---|---|---|
| `frontmatter` | error | required keys present, kind valid, dates parse, types match; comparison pages additionally require `comparison_of` (≥ 2) and `compare_fields` (≥ 1); `aliases` (when present) must be a list of strings |
| `log-format` | error | every `## ` heading in `log.md` matches the schema (code blocks excluded) |
| `broken-wikilink` | error | every `[[link]]` resolves to a known page slug, alias slug, or entity-declared alias |
| `broken-image-ref` | error | every local `![](path)` / `<img src="path">` resolves to an existing file |
| `orphan-page` | warning | synthesis pages with zero inbound links (aliases counted) |
| `stale-page` | warning | `now - last_verified > freshness_window_days` (page-level override; default 30) |
| `citation-density` | warning | `## Summary` paragraphs without any `[[wikilink]]` (default min: 1 per paragraph). Comparison pages exempt. |
| `disputes-format` | warning | `## Disputes` entries that aren't `- ... claims ... Status: ...` bullets |
| `open-questions-format` | warning | `## Open questions` entries that aren't `- [ ] ...` checkboxes |
| `divergence-discipline` | warning | synthesis page has empty `## Disputes`, empty `## Open questions`, AND no `_no contradictions or gaps known yet (last reviewed: YYYY-MM-DD)_` sentinel anywhere in the body |
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
| `ingest --url ... --topic ... --title ... [--excerpt ...]` | write a source page and download its images |
| `research [--topic id]` | trigger Daily Research routine via the `/fire` API |
| `query "<question>"` | trigger Wiki Query routine via the `/fire` API |
| `dry-run --topic <id> \| --query "<q>" \| --weekly-health` | exercise the apply path locally (no Anthropic call) |
| `compare new <slug> --of e1,e2,... --fields f1,f2,... --title "..."` | create a new comparison page reading frontmatter fields from each entity |
| `compare regen <slug>` | regenerate the body of an existing comparison page from current entity frontmatter |
| `recover-prs [--dry-run] [--base main]` | enumerate every open `claude/*` PR to `main` and re-run `apply_gate` per PR (escape hatch when the PR Watcher misfires or for a backlog of stranded PRs) |

## Editing this file

This file co-evolves with the system. When you discover a new convention, add it here in the appropriate section. The Python lint and the agent system prompts both reference these conventions, so keep them tight and unambiguous.
