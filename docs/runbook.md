# Runbook

Day-to-day operations for Wikipilot. This file grows phase by phase; today (Phase 0) it has only the local-dev setup. Phases 1+ add lint workflows, topic management, query workflows, and troubleshooting.

## First-fork checklist

The starter repo ships with the maintainer's live `wiki/` content (sources, concepts, entities, answers, reports, and the seeded topic folders). Before your first Daily Research run, wipe it back to the empty skeleton so the routine starts on your content, not the maintainer's reading:

```bash
uv run wikipilot reset-vault
```

The command prints a dry-run summary first (what would be deleted, what survives) and asks you to confirm by typing the vault directory's basename (`wiki`). It:

- **Deletes** every `*.md` under `wiki/sources/`, `wiki/concepts/`, `wiki/entities/`, `wiki/comparisons/`, `wiki/answers/`, `wiki/reports/`, `wiki/decks/`; every per-source asset folder under `wiki/assets/`; every topic folder under `wiki/topics/`.
- **Resets** `wiki/index.md`, `wiki/log.md`, and `topics.yaml` to empty stubs (the documented header comments at the top of `topics.yaml` are preserved verbatim).
- **Preserves** `wiki/.obsidian/` (the pre-configured reader setup), every `_*.md` personal-scratch file (such as `wiki/_dashboard.md`), and every `.gitkeep`.

Flags:

- `--yes` skips the typed-basename confirmation (for scripted setup or CI).
- `--keep-topics` preserves the entire `wiki/topics/` tree and leaves `topics.yaml` untouched. Use this when you want to inherit the maintainer's topic charters as a starting point.
- `--topics-file path/to/topics.yaml` overrides the default `topics.yaml` location.

The command is idempotent — running it on an already-empty vault is a no-op.

## Local development setup

Prerequisites: Python 3.12+, [uv](https://docs.astral.sh/uv/), git.

```bash
# Clone the repo
git clone https://github.com/<your>/wikipilot.git
cd wikipilot

# Install everything (uv reads pyproject.toml + creates .venv)
uv sync --extra dev

# Run the test suite
uv run pytest

# Lint and format
uv run ruff check .
uv run ruff format --check .
```

## Linting locally

```bash
uv run wikipilot lint wiki/
```

Exit code is 1 on any error, 0 otherwise. Warnings (orphans, staleness, citation density) are reported but don't fail the lint — they're advisory and the daily routine can ignore them. The `--branch <name> --changed-path <path>` flags add the ownership-violation check (see [`CLAUDE.md`](../CLAUDE.md) lint table); CI passes them automatically when run on a `claude/*` branch.

## Adding a topic

1. Add the entry to [`topics.yaml`](../topics.yaml) following the documented schema. `purpose` is required and free-text — be specific about what's IN scope and what's OUT, since `topic-researcher` reads it before deciding whether to ingest a candidate source.
2. Create `wiki/topics/<id>/purpose.md` with a longer-form scope statement. Preflight (Phase 4) blocks routine runs until this file exists.
3. Validate the topics file:
   ```bash
   uv run wikipilot validate-topics
   ```
4. Commit. The next Daily Research run will pick the topic up automatically.

## Reading freshness reports

```bash
uv run wikipilot freshness-report wiki/
```

Pages are listed most-stale first, with age in days, the page's `freshness_window_days` window, and an `!` marker on pages exceeding the window. Use this to prioritize manual re-verification or to spot pages that the Daily Research routine isn't touching.

## Generating a Marp deck

```bash
uv run wikipilot deck <topic-id>
```

Writes `wiki/decks/<topic-id>.md` (Marp markdown) using the topic's `index.md` content. Open in Obsidian with the Marp plugin enabled to render. Pass `--out path` to write elsewhere, or `--theme name` to switch Marp themes.

## Testing the routine prompt locally

Before Phase 8's live smoke test, you can rehearse the entire merge path without spending tokens on Anthropic API calls.

```bash
# Rehearse Daily Research for one topic.
uv run wikipilot dry-run --topic agentic-coding

# Rehearse Wiki Query for one question.
uv run wikipilot dry-run --query "what is attention?"
```

Both commands synthesize a fake proposal/answer (with a citation, a contradiction, an open question, and an image URL on the proposal) and exercise the Python helpers the wiki-merger and query-answerer agents call at runtime. They write to your real `wiki/` directory — typically you'd run them in a scratch checkout or a temp vault to avoid polluting the canonical wiki. The dry-run is what CI uses to verify the cross-page sweep, the back-fill, and the index update.

When you have a real Claude Code routine prompt to test (Phase 4+), use the local `claude` CLI:

```bash
claude --routine prompts/daily_runner.md --topic agentic-coding
```

This runs the full agent stack against your local repo using your local Anthropic credentials, without going through the cloud routines API.

## Writing a topic purpose.md

`wiki/topics/<id>/purpose.md` is the single most important file for off-topic-rejection quality. The `topic-researcher` reads it before deciding whether to ingest each candidate source. Be specific about what's IN scope and what's OUT.

Recommended structure:

```markdown
# Purpose: <Topic display name>

## In scope

- Specific topic 1 with a few example sub-areas.
- Specific topic 2 with concrete keywords or paper titles.

## Out of scope

- Adjacent area that frequently produces noise.
- Marketing posts, industry news, anything not first-party engineering.

## Source quality bar

- Prefer: arxiv preprints, primary research blogs, official docs.
- Reject: aggregator posts, hot-takes, unsourced opinion.
```

After writing, validate the topic file:

```bash
uv run wikipilot validate-topics
```

## Asking the wiki a question

There are two equivalent ways to ask the Wiki Query routine a question. Both end up filing one PR per question, with the answer page under `wiki/answers/` and the related concept/entity pages back-filled to point at it.

### From the CLI

```bash
uv run wikipilot query "what is the fastest way to dispatch parallel subagents?"
```

`wikipilot query` POSTs the question to the Wiki Query routine's `/fire` endpoint with the bearer token from your credentials file (see "Storing the API tokens" below). The CLI prints the routine's `run_id` so you can correlate logs in claude.ai/code/routines.

### Via a GitHub issue

1. Open a new issue in this repo.
2. Apply the `query` label.
3. Put the question in the issue body — the first non-empty line is the question; the rest is optional context.

The routine fires within seconds, files the answer page, opens a PR, and comments back on the issue with a 2-3 sentence summary plus a link to the answer page and a link to the PR. Setup details live in [`routines-setup.md`](routines-setup.md#github-issue-trigger-for-wiki-query).

## Storing the API tokens

Both `wikipilot research` and `wikipilot query` POST to the routines' `/fire` endpoints with a bearer token. They look up the URL and token in:

- Linux/macOS: `~/.config/wikipilot/credentials.toml`
- Windows: `%APPDATA%\wikipilot\credentials.toml`

Override the path with the `WIKIPILOT_CREDENTIALS_FILE` env var (CI uses this so tokens don't leak from the user's home directory).

```toml
[research]
fire_url = "https://api.anthropic.com/v1/routines/<routine-id>/fire"
token    = "<bearer token>"

[query]
fire_url = "https://api.anthropic.com/v1/routines/<routine-id>/fire"
token    = "<bearer token>"
```

Get each routine's `fire_url` and `token` from the routine UI in claude.ai/code/routines (Triggers → API trigger → "Show URL & token"). Store the file with restrictive permissions:

```bash
chmod 600 ~/.config/wikipilot/credentials.toml   # *nix
icacls "%APPDATA%\wikipilot\credentials.toml" /inheritance:r /grant:r "%USERNAME%:F"   # Windows
```

The CLI surfaces a clear error if the file is missing, the section is missing, or the token is blank. On HTTP 429 (rate-limited), the client retries up to 3 times honoring the `Retry-After` header.

## Reviewing or reverting a per-topic PR

The Daily Research routine opens **one PR per topic per day** on `claude/daily-YYYY-MM-DD/<topic-id>`. Each PR is independent — you can review/merge/revert any single topic without touching the others.

### To review

```bash
gh pr list --label daily
gh pr view <pr-number>
gh pr diff <pr-number>
```

The PR body lists every source added, every page touched, new disputes, new open questions, and a link to the per-run report under `wiki/reports/`.

### To revert

If a PR was auto-merged but introduced bad content:

```bash
gh pr revert <pr-number>
```

Or for a single-file undo without reverting the whole topic:

```bash
git checkout main
git diff main~1 main -- wiki/concepts/<page>.md | git apply -R
git commit -am "revert: bad content from <pr-number>"
git push
```

The next Daily Research run for that topic will re-evaluate the affected page.

## Tuning auto-merge thresholds

Auto-merge thresholds live in `wikipilot.toml`. The defaults are sized for Phase 9's permissive-inclusion researcher: 6–8 high-quality sources × 10–15 pages per source per topic per day:

```toml
[automerge.daily_research]
max_files_changed_per_topic = 80
max_total_diff_lines_per_topic = 3000

[automerge.wiki_query]
max_files_changed = 8
max_total_diff_lines = 400

[automerge.weekly_health]
max_files_changed = 60
max_total_diff_lines = 2000
```

The `daily_research` thresholds are calibrated to absorb a busy day under the inclusion-bias rubric (`CLAUDE.md` "Cross-cutting relevance criteria") and to **trip on a safety-cap day**. With `max_sources_per_run: 20` per topic and 10–15 pages per source, a topic that hits the cap could push 200–300 files; the gate refusing to auto-merge that PR is the *signal* a human should eyeball the run report — see "When a topic hits the safety cap" below.

If your topics are small enough that Daily Research consistently auto-merges trivial PRs, reduce `max_files_changed_per_topic` so larger / riskier PRs require human review. If Wiki Query frequently spawns answers that touch many related pages, raise `max_files_changed` for `wiki_query`.

The gate also reads `[automerge.common]`:

- `require_lint_green = true` — block on any lint error.
- `require_tests_green = true` — block on any failing CI check.
- `block_human_only_file_changes = true` — block any PR that modifies a human-only path (`topics.yaml`, `CLAUDE.md`, `wikipilot.toml`, `prompts/`, `wiki/topics/<id>/purpose.md`, etc.).

## Recovering stranded PRs

When a Daily Research session crashes mid-loop (orchestrator OOMs, networking blip, the cloud env terminates the session before the per-topic merge series completes, etc.), the topic PRs that already landed are left **open with no auto-merge queued and no gate-blocked comment** — because `scripts/maybe_automerge.py` never ran on them. The Conflict Resolver routine doesn't fix this case (it only triggers on push to `main`, and these PRs never landed); use `recover-prs` to retry the gate:

```bash
# Default: enumerates every open claude/* PR to main and runs apply_gate
# (full gate, including CI) in enforce mode, inferring the route from
# the branch template per PR.
uv run wikipilot recover-prs

# Preview first without enabling auto-merge / posting comments.
uv run wikipilot recover-prs --dry-run

# Restrict to a non-default base branch.
uv run wikipilot recover-prs --base release-2026-05
```

For each PR, the command prints `pr_number | route | decision | reasons` so you can see at a glance which ones auto-merged and which got a checklist comment. Re-runnable: the gate is idempotent, so a stuck-on-comment PR can be retried after pushing a fix. The centralized trust check applies here too — `apply_gate` will refuse to queue `--auto` on an untrusted PR even if every other criterion passes.

If a PR is stranded *and* `recover-prs` won't unblock it (e.g. you want to skip the CI check because the static gate is what failed), fall back to the per-PR shim — it calls `apply_static_gate`, which mirrors what `maybe_automerge.py` does in-routine:

```bash
python scripts/maybe_automerge.py --pr <num> --route daily_research
```

## Conflict Resolver cost budget

The Conflict Resolver fires one Sonnet orchestrator session per push to `main` matching the trigger filter (`branch=main`). With the current vault:

| Source | Push events per day (typical) | Orchestrator fires |
|---|---|---|
| Daily Research per-topic PRs landing | 5–8 | 5–8 (most resolve to empty scan) |
| Daily Research report PR landing | 1 | 1 |
| Wiki Query PRs landing | 0–3 | 0–3 |
| Weekly Health PR landing | ~1/7 day | ~0 |
| Human pushes to `main` | 0–5 | 0–5 |
| **Total Sonnet sessions per day** | **6–17** | **6–17** |
| Opus subagent dispatches per day | 0–3 (only when scan returns non-empty) | |

Comfortably below Max (15/day) and Team/Enterprise (25/day) caps in normal operation. 90%+ of orchestrator fires scan to empty and exit in <10s, burning minimal Sonnet tokens; Opus only fires on actual conflict work.

If you're consistently exceeding caps:

1. Check `gh pr list --state open --base main --head 'claude/*' --json title,mergeStateStatus` for PRs stuck in `DIRTY` / `BEHIND` — if the same PR is dispatched on every push because the resolver can't unblock it, look at the `conflict-resolver` subagent's reported `reason` to decide whether to merge by hand or close the PR.
2. Add a routine-UI Author filter excluding bots if a third-party bot is pushing unrelated commits to `main`.

## What to do when human-only file changes block auto-merge

The auto-merge gate refuses to land any `claude/*` PR that touches a human-only file. When this fires:

1. Check the PR comment posted by `scripts/maybe_automerge.py` — it lists every blocked path.
2. Decide whether the change is legitimate. Almost always: no, the agent strayed.
3. If the change is wrong, drop the offending edit:
   ```bash
   gh pr checkout <pr-number>
   git checkout HEAD~1 -- CLAUDE.md   # or whichever path
   git commit --amend --no-edit
   git push -f origin HEAD
   ```
4. If the change is genuinely needed (you've decided to update `topics.yaml` based on what the routine found), apply it manually as a separate PR from `main`. Never let an LLM-authored PR own a human file.
5. Iterate on the agent prompt (`prompts/<routine>.md` or `.claude/agents/<agent>.md`) so future runs don't make the same mistake.

## Updating a routine prompt

Routine prompts (`prompts/daily_runner.md`, `prompts/query_answerer.md`, `prompts/weekly_health.md`) are versioned in this repo. Cloud routines aren't yet API-managed, so to update a routine:

1. Edit the prompt file in `prompts/`.
2. Open the routine in claude.ai/code/routines.
3. Copy-paste the updated prompt into the routine UI.
4. Save.

The routine's next run uses the new prompt. We don't auto-sync because there's no public API for that yet.

## Triggering a routine via API

Once the API trigger is configured (see [`docs/routines-setup.md`](routines-setup.md) "Daily Research routine"):

```bash
# Fire Daily Research for one topic.
uv run wikipilot research --topic agentic-coding

# Fire Wiki Query.
uv run wikipilot query "what is the fastest way to dispatch parallel subagents?"
```

These POST to the routines' `/fire` endpoints with the bearer token from `~/.config/wikipilot/credentials.toml` (see [`docs/runbook.md`](runbook.md) "Storing the API tokens" — Phase 6).

## Ingesting a source manually

The `topic-researcher` and `query-answerer` agents normally call this for you, but you can drive it directly when seeding the wiki or testing a fixture:

```bash
uv run wikipilot ingest \
  --url "https://example.com/papers/attention.pdf" \
  --topic "frontier-models" \
  --title "An example paper on attention" \
  --excerpt "Attention is a weighted sum of value vectors." \
  --excerpt "Anthropic builds Claude and publishes on safety alignment."
```

The CLI dedupes by SHA-256 of the normalized URL, writes `wiki/sources/<title>-<sha8>.md` with the documented frontmatter, then runs the Phase 5 image pipeline (configurable via `wikipilot.toml [images]`). Re-ingesting the same URL is a no-op.

## Disabling image downloads

The Phase 5 image pipeline is on by default. To turn it off for a routine run, edit `wikipilot.toml`:

```toml
[images]
enabled = false
```

When disabled:

- `wikipilot ingest` writes the source page but skips the fetch/store/rewrite step entirely.
- Source pages keep their original remote image URLs in the body.
- The `broken-image-ref` lint rule still fires on local refs that don't resolve, so a previously-downloaded source remains valid.

Other knobs:

- `max_image_bytes` (default `5_242_880` = 5 MB) — larger images are skipped with reason `oversize`.
- `allowed_mimes` — restrict the accepted MIME list. The default covers PNG, JPEG, GIF, WebP, SVG.
- `cleanup_orphans` (default `true`) — at ingest time, remove files in `wiki/assets/<slug>/` that aren't referenced by the post-rewrite source page. Disable if you have side-channel assets you want to keep.

Bytes that pass `Content-Length` but fail the streaming size cap are stopped mid-download and never written to disk.

## Reading a weekly health report

Each Weekly Health PR adds one `wiki/reports/health-YYYY-MM-DD.md` page summarizing the wiki's current state. Skim it in this order:

1. **Summary** — counts: stale pages, citation-density failures, new disputes, orphans, broken wikilinks. If everything is zero except disputes, the wiki is healthy.
2. **New disputes** — each entry links to the affected `[[page]]`. These are *candidates* the LLM-judge sweep flagged; the scanner files them as `Status: unresolved` and never decides on its own. Walk through them and resolve on the page itself (see "Resolving a dispute" below).
3. **Stale pages** — pages whose `last_verified` is older than `freshness_window_days`. The Daily Research routine bumps `last_verified` whenever a researcher re-confirms claims. If a page stays stale across multiple weeks, either the topic isn't producing enough fresh sources or the page has drifted from the topic — consider editing the topic's `purpose.md`.
4. **Citation-density failures** — synthesis paragraphs without any `[[wikilink]]`. Often these are introductory paragraphs that *don't* need a citation; the lint surfaces them so you can decide.
5. **Orphans / broken wikilinks** — usually small. Broken wikilinks are an *error*-severity lint that blocks auto-merge, so by the time you see this you already know.

The PR auto-merges by default (the `weekly_health` gate is permissive: 60 files / 2000 lines) — review afterward if the report flagged anything you want to act on.

## Resolving a dispute

When the scanner files a dispute it appends one bullet under `## Disputes` on the affected page:

```markdown
- [[source-A]] claims X; [[source-B]] claims not-X. Status: unresolved (confidence: medium; sweep: 2026-05-17)
```

To resolve:

1. Read both source pages and the surrounding context on the affected synthesis page.
2. Decide which side is correct (or whether both can be true with caveats).
3. **Edit the bullet in place** to change `Status: unresolved` to one of:
   - `Status: resolved-toward-A` (or `-B`)
   - `Status: both-can-be-true: <one-line note>`
   - `Status: superseded: <link to newer source>`
4. **Do not delete the bullet.** The dispute history is the audit trail; future researchers should be able to see what was contested and why it was decided.
5. If the resolution invalidates a synthesis claim, edit the `## Summary` accordingly and bump `last_verified`.

If you can't decide quickly, leave the dispute open. The scanner won't re-file the same dispute (it's a per-sweep idempotent append), so leaving it alone has zero ongoing cost.

## Tuning the disputes seed

`scripts/disputes_seed.py` runs at the top of every Weekly Health routine and selects candidate sets via overlap heuristics. Defaults: K=10 per per-source set, K=10 in the stale set, 7-day lookback. Tune by editing `prompts/weekly_health.md` to pass:

- `--top-k <N>` to widen/narrow the per-source overlap candidate sets
- `--stale-k <N>` to control how many staleness-only candidates land in the sweep
- `--lookback-days <D>` to adjust which sources count as "recent"

Larger K = more candidate sets dispatched in parallel = more scanner cost. The defaults are sized for hundreds of pages; if your wiki grows past ~500 pages, drop K or move the routine to bi-weekly.

## Smoke-test checklist (Phase 8)

This is the manual verification you run **once**, after creating all three routines in claude.ai/code/routines per [`routines-setup.md`](routines-setup.md). It covers the live integrations the dry-run can't exercise (cloud routine fan-out, real Anthropic API calls, GitHub triggers, auto-merge, image downloads from the live web, Obsidian rendering).

The repo ships seeded with five starter topics (`agentic-coding`, `frontier-models`, `ai-in-game-dev`, `games-of-note`, `game-music`); their `purpose.md` files are at `wiki/topics/<id>/purpose.md`. **If you've already run `wikipilot reset-vault`** (the recommended first-fork step — see "First-fork checklist" above) those topics are gone; add your own in `topics.yaml` and create the matching `wiki/topics/<id>/purpose.md` before smoke-testing. **If you haven't reset yet**, edit `topics.yaml` to swap or remove topics before the smoke run.

### Prep

- [ ] All three routines exist in claude.ai/code/routines (Daily Research, Wiki Query, Weekly Health).
- [ ] `~/.config/wikipilot/credentials.toml` (or `%APPDATA%\wikipilot\credentials.toml`) holds `[research]` and `[query]` `fire_url` + `token`.
- [ ] Local `wikipilot lint wiki/` is clean (`0 error(s), 0 warning(s)`).
- [ ] Local `wikipilot validate-topics` shows the topic count you expect.
- [ ] `wikipilot dry-run --topic agentic-coding`, `--query "..."`, and `--weekly-health` all complete without error against a scratch vault.

### Daily Research smoke test

1. Click **Run now** on the Daily Research routine (does NOT count against the daily cap).
2. Within ~3 minutes, check `gh pr list --label daily` — you should see one PR per `daily` topic on `claude/daily-YYYY-MM-DD/<topic-id>`.
3. For each PR, verify:
   - [ ] CI green (lint + tests).
   - [ ] Auto-merge fired (or didn't, per the `[automerge.daily_research]` gate — both outcomes are valid; only failed gates are bugs).
   - [ ] Every new synthesis page has `last_updated`, `last_verified`, `sources[]` frontmatter.
   - [ ] Every non-trivial summary paragraph has at least one `[[source-slug]]` wikilink and a `>` quote from that source.
   - [ ] Cross-page sweep happened: any concept mentioned in a page diff that's also mentioned by another existing page → that other page got `last_updated` bumped.
   - [ ] Images downloaded under `wiki/assets/<source-slug>/` and source pages reference local paths (`../assets/...`).
   - [ ] `wiki/reports/YYYY-MM-DD.md` written with the full audit (sources added, pages touched, runtime, token usage, PR links).
   - [ ] `topics.yaml`, `CLAUDE.md`, `wikipilot.toml`, and `wiki/topics/<id>/purpose.md` are unchanged (ownership matrix preserved — if any of these changed, the gate should have blocked auto-merge).

### Wiki Query smoke test

1. **GitHub-issue path**: Open a new issue with the label `query`, body `What is the fastest way to dispatch parallel subagents?` (or any real question).
2. **CLI path**: `uv run wikipilot query "what evaluation methodologies replicate?"` from the same machine.
3. Within ~1 minute, verify (for each):
   - [ ] One PR opens on `claude/query-YYYY-MM-DD-<slug>`.
   - [ ] `wiki/answers/YYYY-MM-DD-<slug>.md` exists with citations + quotes.
   - [ ] Back-fill: every related concept/entity page gained a `[[<answer-slug>]]` line under `## See also`.
   - [ ] CI green; auto-merge fires (or doesn't, per `[automerge.wiki_query]`).
   - [ ] For the GitHub-triggered question: a comment was posted on the originating issue with answer summary + page link + PR link.

### Weekly Health smoke test

1. Click **Run now** on the Weekly Health routine (don't wait a week).
2. Within ~5 minutes, verify:
   - [ ] One PR on `claude/health-YYYY-MM-DD`.
   - [ ] If candidate sets were generated: dispute proposals filed under `## Disputes` on affected pages with `Status: unresolved (confidence: ...; sweep: <date>)`.
   - [ ] No disputes were auto-resolved (check the diff: every `Status:` line says `unresolved`).
   - [ ] `wiki/reports/health-YYYY-MM-DD.md` written with the lint/freshness summary.
   - [ ] PR auto-merged per the permissive `[automerge.weekly_health]` gate.

### Obsidian / Marp / Dataview spot-checks

After at least one Daily Research run has landed real content:

- [ ] Open `wiki/` in Obsidian (`docs/obsidian-setup.md` for setup); the graph view shows the new topic, concept, source, and answer pages with their cross-links.
- [ ] The three example Dataview queries in `docs/obsidian-setup.md` render: recently-touched pages, stale pages, and open questions across the wiki.
- [ ] `uv run wikipilot deck agentic-coding` writes `wiki/decks/agentic-coding.md`; the Obsidian Marp plugin opens it cleanly.

### Iterating on the prompts

If any verification step failed, the fix is almost always a prompt edit, not a code change. Edit one of:

- `prompts/daily_runner.md` — for fan-out / cross-page sweep / report issues
- `prompts/query_answerer.md` — for back-fill / issue-comment / answer-quality issues
- `prompts/weekly_health.md` — for candidate seeding / dispute filing / report issues
- `.claude/agents/<agent>.md` — for per-agent system prompt and model issues

Then follow "Updating a routine prompt" above to push the change to claude.ai/code/routines. Re-run the smoke test for the affected routine.

## Generating a comparison page

Comparison pages (Phase 9 Pattern A; see `CLAUDE.md` "Comparison pages") aggregate frontmatter fields across N entity pages into a single markdown table. Use them when you have ≥ 2 entity pages with parallel frontmatter and want a single-glance N-way view.

To create a new comparison page from the CLI:

```bash
uv run wikipilot compare new cost-comparison \
  --of claude-opus-4.7,gpt-5.5,gemini-2.5-pro \
  --fields cost_per_mtoken_in,cost_per_mtoken_out,context_window \
  --title "Frontier model cost comparison"
```

This writes `wiki/comparisons/cost-comparison.md` with `kind: comparison`, the `comparison_of` and `compare_fields` lists in frontmatter, and a table whose cells render `_unknown_` for any entity that doesn't carry the field. The `_unknown_` cells are an explicit prompt to backfill the value on the entity page (then re-run `regen` below) — comparison cells are never edited by hand.

To regenerate the body after entity frontmatter changes:

```bash
uv run wikipilot compare regen cost-comparison
```

Idempotent: re-reads the comparison page's own `comparison_of` / `compare_fields`, queries each entity, rewrites the table. `last_updated` bumps to today; `last_verified` is left alone (regen is mechanical, not a re-verification of the underlying claims).

Both commands write to `wiki/comparisons/<slug>.md`. Prefer slugs that read as comparison nouns (`cost-comparison`, `agentic-ide-comparison`, `text-to-3d-comparison`) over verbs.

## Resolving a divergence-check warning

Phase 9 Pattern B introduces the `divergence-discipline` lint warning (`CLAUDE.md` "Divergence check"). It fires on synthesis pages (`topic`, `concept`, `entity`, `answer`) that have an empty `## Disputes` section, an empty `## Open questions` section, AND no `_no contradictions or gaps known yet (last reviewed: YYYY-MM-DD)_` sentinel anywhere in the body.

Severity is warning, so it doesn't block auto-merge — but the agents are mandated to satisfy it on every page they create. When you see the warning on a page you're editing manually, pick one of three remediation paths:

1. **Found a counter-argument** — add a bullet to `## Disputes`:
   ```markdown
   - [[source-A]] claims the cap is 200k tokens; [[source-B]] reports the cap is 500k tokens. Status: unresolved (confidence: medium; sweep: 2026-05-12)
   ```
2. **Found a data gap** — add a checkbox to `## Open questions`:
   ```markdown
   - [ ] No public benchmark for this model on SWE-bench yet — re-check after the v2 release.
   ```
3. **Searched and genuinely found nothing** — add the sentinel verbatim somewhere in the body (convention: at the end, after `## See also`):
   ```markdown
   _no contradictions or gaps known yet (last reviewed: 2026-05-12)_
   ```

The intent (per the gist comment thread the rule absorbed) is to force the author to actively look for divergence before claiming none — the sentinel is a deliberate, dated assertion, not a placeholder. Refresh the date when re-verifying the page.

## Adding an entity alias

Phase 9 Pattern C (`CLAUDE.md` "Entity aliases"). Add `aliases:` to entity frontmatter when an entity has multiple common names — version stylings (`Claude Opus 4.7` / `claude-opus-4.7` / `Opus 4.7`), hyphen-vs-space variants (`GPT 4` / `GPT-4`), legacy names that get retconned, or product-vs-CLI splits (`claude-code` / `Claude Code`). Once declared, `[[any alias]]` resolves to this page and the lint stops flagging it as a broken wikilink or as an orphan if pages link via the alias slug.

Edit the entity page's frontmatter:

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

Aliases are slugified before resolution, so `"GPT 4"` matches `[[GPT 4]]`, `[[gpt-4]]`, and `[[gpt 4]]`. After adding aliases, re-run `uv run wikipilot lint wiki/` to confirm previously broken `[[gpt4]]` references now resolve. Don't list the entity's own slug as an alias — it's already resolvable.

## When a topic hits the safety cap

`max_sources_per_run: 20` is uniform across all 5 Phase 9 topics (`CLAUDE.md` "Cross-cutting relevance criteria"). It is a runaway guard, not a quality lever — under the inclusion-bias rubric a busy day should land 6–12 sources per topic, and 20 means something unusual happened.

Detection signal: the daily_research auto-merge gate refuses to merge a per-topic PR (the gate thresholds — `max_files_changed_per_topic = 80`, `max_total_diff_lines_per_topic = 3000` — are calibrated to busy-day flow and trip on a safety-cap day). The PR comment from `scripts/maybe_automerge.py` will say `diff too large`.

Remediation path:

1. Read the per-run report at `wiki/reports/YYYY-MM-DD.md` for the affected topic. Skim the source list — are these all genuinely on-topic, or is the agent over-ingesting adjacent material?
2. Decide which lever to pull:
   - **Topic-specific drift**: tighten `wiki/topics/<id>/purpose.md` "Out of scope" with the specific noise pattern you saw (the most common case).
   - **Cross-cutting drift**: tighten `CLAUDE.md` "Cross-cutting relevance criteria" if the over-ingest cuts across multiple topics (rare; the criteria are deliberately permissive).
   - **Genuine busy day**: if the sources are all legitimate (a major model release, a Game Awards day, a Unity AI announcement), accept the PR by manually merging. No prompt change needed; the safety cap did its job.
3. Spot-check the next 1–2 daily runs for the topic to confirm the rubric edit took effect — the cap should drop back to typical 6–12 sources.

The cap is intentionally not raised in response to busy days — the auto-merge gate trip is the manual-review prompt, not a sign the cap is too low.

### Local CLI

- **`wikipilot: command not found`** — the project venv isn't on PATH. Use `uv run wikipilot ...` (always works) or activate the venv (`source .venv/bin/activate` / `.venv\Scripts\Activate.ps1`).
- **`uv: command not found`** — install uv (`curl -LsSf https://astral.sh/uv/install.sh | sh` or `pip install --user uv`); on Windows PowerShell, add `$env:APPDATA\Python\Python312\Scripts` to PATH for the current session.
- **`tomllib` import error** — your interpreter is < Python 3.11. Use Python 3.12 (`uv python install 3.12`).
- **`No such option: --topic` from `wikipilot dry-run`** — you're on an old commit. Pull `main`; the `--topic` / `--query` / `--weekly-health` flags landed in Phase 2 / Phase 7 respectively.
- **`wikipilot lint` reports `disputes-format` on a placeholder line** — the lint requires bullets in `## Disputes` to start with `- ` and contain the literal substrings `claims` and `Status:`. Either delete the placeholder paragraph or convert it to `_(none yet — populated by the Weekly Health routine.)_` on a single line (lines starting with `_` are ignored).
- **`wikipilot lint` reports `broken-wikilink` for `[[source-slug]]`** — the lint parses every `[[...]]` even inside backticks. Use prose like "the source-page slug appears in double square brackets" instead of the literal placeholder.

### Cloud routine setup

- **Routine fails immediately with `preflight: missing topic purpose.md`** — you added a topic to `topics.yaml` without writing `wiki/topics/<id>/purpose.md`. Create it (template in "Writing a topic purpose.md" above), commit, push, retry.
- **Routine fails with `qmd index missing`** — the setup script didn't run, or the `wikipilot index-wiki` command failed. Re-trigger the routine; the `uv sync` cache will let the setup script complete in seconds the second time.
- **`fire_url` returns 401** — the bearer token in `credentials.toml` is wrong or expired. Re-copy from the routine UI (Triggers → API trigger → "Show URL & token") and `chmod 600` the file again.
- **`fire_url` returns 429** — you've hit the routine cap (Pro 5/day, Max 15/day, Team/Enterprise 25/day per Anthropic docs). The `api_client` retries up to 3× honoring `Retry-After`; beyond that you wait. Scheduled runs and API-triggered runs share the cap.
- **GitHub-issue trigger doesn't fire** — verify the Claude GitHub App is installed on the repo (settings → Integrations → GitHub Apps), the routine's GitHub trigger is set to `issue.opened` filtered by `Labels include: query`, and the issue actually carries the `query` label.

### Per-routine PR / auto-merge

- **PR opens but auto-merge never fires** — read the comment posted by `scripts/maybe_automerge.py`. It lists the gate verdict (`pass`/`fail`) and the failure reason. Common reasons:
  - `lint failed` — fix the lint error on the branch and push.
  - `tests failed` — see CI logs.
  - `human-only file modified` — see "What to do when human-only file changes block auto-merge" above.
  - `diff too large` — either the routine actually shouldn't have touched that many files (revisit the prompt), or the gate is too tight for your wiki size; tune `wikipilot.toml [automerge.<route>]`.
- **Auto-merge fired but the PR is wrong** — `gh pr revert <N>`, then iterate on the prompt before the next run.

### Daily Research

- **Topic researcher ingests an off-topic source** — `wiki/topics/<id>/purpose.md` isn't specific enough. Tighten the in-scope / out-of-scope sections; preflight reads it, the agent reads it. Re-trigger.
- **No cross-page sweep happened** — the `wiki-merger` agent or the `update-index` skill didn't run. Re-read `prompts/daily_runner.md` Step 6 with the agent — usually the orchestrator skipped a step.
- **Images didn't download** — check `wikipilot.toml [images]`: `enabled = true`? Check the source page body for `wiki/assets/...` paths; if the body still has remote URLs, the `download-source-images` skill didn't fire. The Phase 5 skill is wired into `wikipilot ingest`; if the agent didn't call `wikipilot ingest`, the images don't download. Look for `Skipped image download` in the run report.
- **Hallucinated cross-link / `broken-wikilink` lint error** — the synthesizer named a page that doesn't exist. The auto-merge gate catches this. Iterate on the wiki-merger prompt: stress that *every* `[[link]]` must be either an existing slug or a slug created in this same proposal.

### Wiki Query

- **Answer page has no citations** — the `query-answerer` agent skipped or hallucinated. Re-read the agent's system prompt at `.claude/agents/query-answerer.md`; it MUST cite or refuse. Tighten the rule.
- **Issue comment never posted** — the routine ran but the final `gh issue comment` step failed. Check the routine logs in claude.ai/code/routines for the actual `gh` exit code; usually the GitHub token in the routine env is missing.
- **Back-fill didn't happen** — the `query-back-fill` skill wasn't called. The orchestrator must call it after the answer page is written. Re-read `prompts/query_answerer.md` Step 6.

### Weekly Health

- **No candidate sets generated** — `disputes_seed.py` produced an empty result. Most common reasons: no sources ingested in the last 7 days (default lookback), and/or no synthesis pages exist yet. Either wait until the Daily Research routine has populated the wiki, or run `python scripts/disputes_seed.py --lookback-days 30` to widen the window.
- **Scanner filed a dispute that's actually correct** — false positive. The scanner's job is to file every plausible candidate; humans decide. Mark it `Status: both-can-be-true: ...` and move on. If false positives flood, tighten `.claude/agents/wiki-disputes-scanner.md`'s "what counts as a dispute" rules.
- **Scanner auto-resolved a dispute** — bug. The scanner's mandate (and prompt) say it MUST file `Status: unresolved` only. Check the agent file at `.claude/agents/wiki-disputes-scanner.md` and the orchestrator at `prompts/weekly_health.md`; both stress this constraint.
- **Health PR has 0 disputes but lots of `last_updated` bumps** — that's correct: the orchestrator runs `wikipilot freshness-report` and `wikipilot lint wiki/` and writes the report regardless of whether disputes were filed. The bumps come from the report being a new file and the log entry, not from page edits.

### Obsidian / Marp / Dataview

- **Graph view doesn't show new pages** — Obsidian needs a vault re-index. Press `Ctrl/Cmd-P` → "Force re-index vault".
- **Marp deck doesn't render** — install the Marp Obsidian plugin (`docs/obsidian-setup.md`); confirm the deck's frontmatter has `marp: true`.
- **Dataview queries empty** — install Dataview plugin; the example queries in `docs/obsidian-setup.md` need it. Make sure pages have `last_updated`/`last_verified` as proper date values (not strings) — the Phase 1 wiki primitives write them as `date`, but a hand-edited page might have them as `"2026-05-11"` (string).

## Phase progress

- **Phase 0**: bootstrap repo, docs spine, empty Obsidian vault, page conventions in CLAUDE.md.
- **Phase 1**: Wiki primitives, source registry, freshness-aware lint, full CLI surface.
- **Phase 2**: 5 subagents (topic-researcher, wiki-merger, wiki-linter, query-answerer, wiki-disputes-scanner), 8 skills, dry-run dispatcher.
- **Phase 3**: per-route git ops (`git_ops.py`), `maybe_automerge.py` per-route gate, `wikipilot.toml` thresholds, `.github/workflows/ci.yml`.
- **Phase 4**: Daily Research routine prompt, `scripts/preflight.py`, qmd MCP setup, three setup docs.
- **Phase 5**: Image download pipeline (`wikipilot ingest`, `download-source-images` skill, `broken-image-ref` lint rule).
- **Phase 6**: Wiki Query routine prompt, real `api_client.py` (HTTP + 429 retry), wired `wikipilot research`/`query` CLI, GitHub-issue trigger setup.
- **Phase 7**: Weekly Health routine prompt, `scripts/disputes_seed.py` overlap heuristics, health-report reader docs, dispute-resolution guidance.
- **Phase 8**: Two starter topics seeded (`ai-agents`, `llm-evals`) with real `purpose.md`, smoke-test checklist + Troubleshooting section, CI dry-run extended to weekly health.
- **Phase 9 (current)**: Five focused topics replace the seeded two (`agentic-coding`, `frontier-models`, `ai-in-game-dev`, `games-of-note`, `game-music`); three structural patterns absorbed from Karpathy's gist — comparison pages as a first-class wiki kind (`wikipilot compare new` / `regen`), `divergence-discipline` lint, entity `aliases:`. Source-ingestion shifted from numeric per-topic caps to qualitative "Cross-cutting relevance criteria" + inclusion bias in `CLAUDE.md` and `topic-researcher.md`; uniform `max_sources_per_run: 20` reframed as a runaway safety cap; `daily_research` auto-merge thresholds bumped to 80 files / 3000 lines so the gate trips on safety-cap days.
