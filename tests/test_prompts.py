"""Tests for routine prompt files in ``prompts/``.

These are structural sanity checks: every prompt file must mention the
required workflow steps (preflight, cache-warming, parallel dispatch,
per-route gate) so accidental prompt regressions are caught at PR time.
"""

from __future__ import annotations

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
PROMPTS_DIR = REPO_ROOT / "prompts"


def _read(name: str) -> str:
    path = PROMPTS_DIR / f"{name}.md"
    assert path.exists(), f"prompt file missing: {path}"
    return path.read_text(encoding="utf-8")


def test_daily_runner_prompt_exists() -> None:
    body = _read("daily_runner")
    assert body.strip(), "daily_runner.md must not be empty"


@pytest.mark.parametrize(
    "required",
    [
        "preflight.py",
        "CLAUDE_CODE_FORK_SUBAGENT",
        "topic-researcher",
        "wiki-merger",
        "wiki-linter",
        "claude/daily-",
        "maybe_automerge.py --pr",
        "wiki/reports/",
        "human-only",
    ],
)
def test_daily_runner_mentions_each_required_step(required: str) -> None:
    body = _read("daily_runner")
    assert required in body, (
        f"daily_runner.md must mention {required!r} so the routine follows the documented workflow"
    )


def test_daily_runner_uses_correct_branch_template() -> None:
    body = _read("daily_runner")
    # Branch template: claude/daily-<date>/<topic-id>
    assert "claude/daily-${DATE}/${TOPIC_ID}" in body or "claude/daily-{date}/{topic_id}" in body


def test_daily_runner_dispatches_topic_researcher_in_parallel() -> None:
    body = _read("daily_runner").lower()
    assert "in parallel" in body
    assert "fork_subagent" in body or "fork-subagent" in body


def test_query_answerer_prompt_exists() -> None:
    body = _read("query_answerer")
    assert body.strip(), "query_answerer.md must not be empty"


@pytest.mark.parametrize(
    "required",
    [
        "preflight.py",
        "query-answerer",
        "query-back-fill",
        "claude/query-",
        "wiki/answers/",
        "ingest-source",
        "maybe_automerge.py --pr",
        "wiki_query",
        "gh issue comment",
        "qmd-search",
    ],
)
def test_query_answerer_mentions_each_required_step(required: str) -> None:
    body = _read("query_answerer")
    assert required in body, f"query_answerer.md must mention {required!r}"


def test_query_answerer_handles_both_triggers() -> None:
    body = _read("query_answerer").lower()
    assert "github-triggered" in body or "github trigger" in body or "issue.opened" in body
    assert "api-triggered" in body or "/fire" in body


def test_weekly_health_prompt_exists() -> None:
    body = _read("weekly_health")
    assert body.strip(), "weekly_health.md must not be empty"


@pytest.mark.parametrize(
    "required",
    [
        "preflight.py",
        "disputes_seed.py",
        "wiki-disputes-scanner",
        "CLAUDE_CODE_FORK_SUBAGENT",
        "claude/health-",
        "wiki/reports/health-",
        "maybe_automerge.py --pr",
        "weekly_health",
        "append-only",
        "Status: unresolved",
    ],
)
def test_weekly_health_mentions_each_required_step(required: str) -> None:
    body = _read("weekly_health")
    assert required in body, f"weekly_health.md must mention {required!r}"


def test_weekly_health_dispatches_in_parallel() -> None:
    body = _read("weekly_health").lower()
    assert "in parallel" in body
    assert "fork_subagent" in body or "fork-subagent" in body
