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

## Asking an ad-hoc query

Once Phase 6 ships:

```bash
uv run wikipilot query "what is the fastest way to dispatch parallel subagents?"
```

This fires the Wiki Query routine via the `/fire` API. The answer appears as a new page under `wiki/answers/`, with back-fill into related concept pages, within ~1 minute. Alternatively, open a GitHub issue with the `query` label — the routine reads the issue body as the question and posts the answer back as an issue comment.

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

## Phase progress

- **Phase 0**: bootstrap repo, docs spine, empty Obsidian vault, page conventions in CLAUDE.md.
- **Phase 1**: Wiki primitives, source registry, freshness-aware lint, full CLI surface.
- **Phase 2**: 5 subagents (topic-researcher, wiki-merger, wiki-linter, query-answerer, wiki-disputes-scanner), 8 skills, dry-run dispatcher.
- **Phase 3 (current)**: per-route git ops (`git_ops.py`), `maybe_automerge.py` per-route gate, `wikipilot.toml` thresholds, `.github/workflows/ci.yml`.
- **Phase 2**: Subagent definitions, skill manifests, dry-run dispatcher.
- **Phase 3**: Per-route git ops, auto-merge gate, CI workflow.
- **Phase 4**: Daily Research routine prompt + qmd MCP + cloud setup.
- **Phase 5**: Image download pipeline.
- **Phase 6**: Wiki Query routine + API client + GitHub-issue trigger.
- **Phase 7**: Weekly Health routine + LLM-judge sweep + disputes scanner.
- **Phase 8**: Live smoke test of all three routines.
