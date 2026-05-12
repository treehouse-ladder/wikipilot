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


def test_daily_runner_renders_pr_body_via_helper() -> None:
    """Step 4 should call render_pr_body_daily — never hand-write the body."""
    body = _read("daily_runner")
    assert "render_pr_body_daily" in body, (
        "daily_runner.md must use render_pr_body_daily so PR shape stays canonical"
    )


def test_query_answerer_renders_pr_body_via_helper() -> None:
    body = _read("query_answerer")
    assert "render_pr_body_query" in body, (
        "query_answerer.md must use render_pr_body_query so PR shape stays canonical"
    )


def test_weekly_health_renders_pr_body_via_helper() -> None:
    body = _read("weekly_health")
    assert "render_pr_body_health" in body, (
        "weekly_health.md must use render_pr_body_health so PR shape stays canonical"
    )


def test_daily_runner_enforces_citation_discipline() -> None:
    body = _read("daily_runner").lower()
    assert "cite or refuse" in body or "[[source-slug]]" in body, (
        "daily_runner.md must repeat the citation discipline as a hard rule"
    )


def test_weekly_health_forbids_bumping_last_verified() -> None:
    body = _read("weekly_health").lower()
    assert "last_updated" in body and "last_verified" in body
    assert "never" in body or "not" in body, (
        "weekly_health.md must explicitly forbid bumping last_verified"
    )


# ---------------------------------------------------------------------------
# Phase 9 invariants: cross-cutting criteria + divergence discipline
# ---------------------------------------------------------------------------

AGENTS_DIR = REPO_ROOT / ".claude" / "agents"
CLAUDE_MD = REPO_ROOT / "CLAUDE.md"


def _read_agent(name: str) -> str:
    path = AGENTS_DIR / f"{name}.md"
    assert path.exists(), f"agent file missing: {path}"
    return path.read_text(encoding="utf-8")


def test_topic_researcher_states_three_criteria_verbatim() -> None:
    body = _read_agent("topic-researcher").lower()
    assert "highly relevant" in body
    assert "highly innovative" in body
    assert "agentic workflow" in body
    assert "video game development" in body or "game development" in body


def test_topic_researcher_states_inclusion_bias() -> None:
    body = _read_agent("topic-researcher").lower()
    assert "when on the fence, include" in body, (
        "topic-researcher.md must state the inclusion bias literally"
    )


def test_topic_researcher_documents_cross_topic_flag() -> None:
    body = _read_agent("topic-researcher")
    assert "also_relevant_to" in body, (
        "topic-researcher.md must document the cross-topic flag in the Proposal schema"
    )


def test_claude_md_has_cross_cutting_criteria_section() -> None:
    body = CLAUDE_MD.read_text(encoding="utf-8")
    assert "Cross-cutting relevance criteria" in body, (
        "CLAUDE.md must contain the 'Cross-cutting relevance criteria' section "
        "(meta-charter — drift guard between agent prompt and human-owned charter)"
    )
    lower = body.lower()
    assert "highly relevant" in lower
    assert "highly innovative" in lower
    assert "agentic workflow" in lower
    assert "video game development" in lower or "game development" in lower


@pytest.mark.parametrize("agent", ["topic-researcher", "wiki-merger", "query-answerer"])
def test_synthesis_agents_mention_divergence_discipline(agent: str) -> None:
    body = _read_agent(agent).lower()
    assert "divergence-discipline" in body or "divergence discipline" in body, (
        f"{agent}.md must mandate divergence-discipline (counter-argument or sentinel)"
    )


@pytest.mark.parametrize("prompt", ["daily_runner", "query_answerer"])
def test_orchestrator_prompts_mention_divergence_discipline(prompt: str) -> None:
    body = _read(prompt).lower()
    assert "divergence-discipline" in body or "divergence discipline" in body, (
        f"{prompt}.md must mandate divergence-discipline as a hard rule"
    )
