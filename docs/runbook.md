# Runbook

Day-to-day operations for Wikipilot. This file grows phase by phase; today (Phase 0) it has only the local-dev setup. Phases 1+ add lint workflows, topic management, query workflows, and troubleshooting.

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
uv run wikipilot dry-run --topic ai-agents

# Rehearse Wiki Query for one question.
uv run wikipilot dry-run --query "what is attention?"
```

Both commands synthesize a fake proposal/answer (with a citation, a contradiction, an open question, and an image URL on the proposal) and exercise the Python helpers the wiki-merger and query-answerer agents call at runtime. They write to your real `wiki/` directory — typically you'd run them in a scratch checkout or a temp vault to avoid polluting the canonical wiki. The dry-run is what CI uses to verify the cross-page sweep, the back-fill, and the index update.

When you have a real Claude Code routine prompt to test (Phase 4+), use the local `claude` CLI:

```bash
claude --routine prompts/daily_runner.md --topic ai-agents
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

Auto-merge thresholds live in `wikipilot.toml`. The defaults are sized for Karpathy's "10–15 pages per source" reality:

```toml
[automerge.daily_research]
max_files_changed_per_topic = 40
max_total_diff_lines_per_topic = 1500

[automerge.wiki_query]
max_files_changed = 8
max_total_diff_lines = 400

[automerge.weekly_health]
max_files_changed = 60
max_total_diff_lines = 2000
```

If your topics are small enough that Daily Research consistently auto-merges trivial PRs, reduce `max_files_changed_per_topic` so larger / riskier PRs require human review. If Wiki Query frequently spawns answers that touch many related pages, raise `max_files_changed` for `wiki_query`.

The gate also reads `[automerge.common]`:

- `require_lint_green = true` — block on any lint error.
- `require_tests_green = true` — block on any failing CI check.
- `block_human_only_file_changes = true` — block any PR that modifies a human-only path (`topics.yaml`, `CLAUDE.md`, `wikipilot.toml`, `prompts/`, `wiki/topics/<id>/purpose.md`, etc.).

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
uv run wikipilot research --topic ai-agents

# Fire Wiki Query.
uv run wikipilot query "what is the fastest way to dispatch parallel subagents?"
```

These POST to the routines' `/fire` endpoints with the bearer token from `~/.config/wikipilot/credentials.toml` (see [`docs/runbook.md`](runbook.md) "Storing the API tokens" — Phase 6).

## Ingesting a source manually

The `topic-researcher` and `query-answerer` agents normally call this for you, but you can drive it directly when seeding the wiki or testing a fixture:

```bash
uv run wikipilot ingest \
  --url "https://example.com/papers/attention.pdf" \
  --topic "ai-agents" \
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

## Phase progress

- **Phase 0**: bootstrap repo, docs spine, empty Obsidian vault, page conventions in CLAUDE.md.
- **Phase 1**: Wiki primitives, source registry, freshness-aware lint, full CLI surface.
- **Phase 2**: 5 subagents (topic-researcher, wiki-merger, wiki-linter, query-answerer, wiki-disputes-scanner), 8 skills, dry-run dispatcher.
- **Phase 3**: per-route git ops (`git_ops.py`), `maybe_automerge.py` per-route gate, `wikipilot.toml` thresholds, `.github/workflows/ci.yml`.
- **Phase 4**: Daily Research routine prompt, `scripts/preflight.py`, qmd MCP setup, three setup docs.
- **Phase 5**: Image download pipeline (`wikipilot ingest`, `download-source-images` skill, `broken-image-ref` lint rule).
- **Phase 6**: Wiki Query routine prompt, real `api_client.py` (HTTP + 429 retry), wired `wikipilot research`/`query` CLI, GitHub-issue trigger setup.
- **Phase 7 (current)**: Weekly Health routine prompt, `scripts/disputes_seed.py` overlap heuristics, health-report reader docs, dispute-resolution guidance.
- **Phase 8**: Live smoke test of all three routines.
