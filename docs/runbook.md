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

## Phase progress

- **Phase 0 (current)**: bootstrap repo, docs spine, empty Obsidian vault, page conventions in CLAUDE.md.
- **Phase 1**: Wiki primitives, source registry, freshness-aware lint, full CLI surface.
- **Phase 2**: Subagent definitions, skill manifests, dry-run dispatcher.
- **Phase 3**: Per-route git ops, auto-merge gate, CI workflow.
- **Phase 4**: Daily Research routine prompt + qmd MCP + cloud setup.
- **Phase 5**: Image download pipeline.
- **Phase 6**: Wiki Query routine + API client + GitHub-issue trigger.
- **Phase 7**: Weekly Health routine + LLM-judge sweep + disputes scanner.
- **Phase 8**: Live smoke test of all three routines.
