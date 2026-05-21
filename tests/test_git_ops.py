"""Tests for ``wikipilot.git_ops`` (mocked git/gh subprocess)."""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from datetime import date

import pytest

from wikipilot.config import (
    AutomergeCommon,
    AutomergeRoute,
    BranchesConfig,
    ImagesConfig,
    WikipilotConfig,
)
from wikipilot.git_ops import (
    ROUTE_DAILY_RESEARCH,
    ROUTE_WEEKLY_HEALTH,
    ROUTE_WIKI_QUERY,
    PRView,
    apply_gate,
    branch_for_daily,
    branch_for_health,
    branch_for_query,
    checkout_new_branch,
    comment_pr,
    create_pr,
    enable_automerge,
    evaluate_gate,
    push_branch,
    render_pr_body_daily,
    render_pr_body_health,
    render_pr_body_query,
    stage_and_commit,
    view_pr,
)


@dataclass
class FakeRunner:
    """Records every subprocess call and replays canned responses."""

    responses: dict[str, subprocess.CompletedProcess[str]]
    calls: list[list[str]]

    def __call__(self, args, capture_output=True, text=True, check=False):
        self.calls.append(list(args))
        key = " ".join(args[:3])
        return self.responses.get(key, subprocess.CompletedProcess(args, 0, "", ""))


def _ok(
    stdout: str = "", stderr: str = "", returncode: int = 0
) -> subprocess.CompletedProcess[str]:
    return subprocess.CompletedProcess([], returncode, stdout, stderr)


@pytest.fixture
def runner() -> FakeRunner:
    return FakeRunner(responses={}, calls=[])


def _config(
    *,
    daily: AutomergeRoute | None = None,
    query: AutomergeRoute | None = None,
    weekly: AutomergeRoute | None = None,
    block_human: bool = True,
    require_checks: bool = True,
) -> WikipilotConfig:
    return WikipilotConfig(
        automerge_common=AutomergeCommon(
            require_lint_green=require_checks,
            require_tests_green=require_checks,
            block_human_only_file_changes=block_human,
        ),
        daily_research=daily
        or AutomergeRoute(max_files_changed_per_topic=40, max_total_diff_lines_per_topic=1500),
        wiki_query=query or AutomergeRoute(max_files_changed=8, max_total_diff_lines=400),
        weekly_health=weekly or AutomergeRoute(max_files_changed=60, max_total_diff_lines=2000),
        images=ImagesConfig(),
        branches=BranchesConfig(),
    )


class TestBranchHelpers:
    def test_daily_template(self) -> None:
        assert (
            branch_for_daily("ai-agents", today=date(2026, 5, 11))
            == "claude/daily-2026-05-11/ai-agents"
        )

    def test_query_template_slugs_question(self) -> None:
        name = branch_for_query("What is qmd?", today=date(2026, 5, 11))
        assert name == "claude/query-2026-05-11-what-is-qmd"

    def test_query_template_truncates_long_questions(self) -> None:
        long_q = "A" * 200
        name = branch_for_query(long_q, today=date(2026, 5, 11))
        # The slug portion (after the `claude/query-YYYY-MM-DD-` prefix) is capped at 48 chars.
        prefix = "claude/query-2026-05-11-"
        assert name.startswith(prefix)
        slug = name[len(prefix) :]
        assert 0 < len(slug) <= 48

    def test_query_template_falls_back_for_unslugifiable(self) -> None:
        name = branch_for_query("???", today=date(2026, 5, 11))
        assert name.endswith("untitled") or "untitled" in name

    def test_health_template(self) -> None:
        assert branch_for_health(today=date(2026, 5, 17)) == "claude/health-2026-05-17"


class TestCheckoutNewBranch:
    def test_calls_git_fetch_and_checkout(self, runner: FakeRunner) -> None:
        runner.responses = {"git fetch origin": _ok(), "git checkout -B": _ok()}
        checkout_new_branch("claude/daily-2026-05-11/ai-agents", base="main", runner=runner)
        # Should have invoked git fetch and git checkout -B at least once each.
        joined = [" ".join(c[:2]) for c in runner.calls]
        assert "git fetch" in joined
        assert "git checkout" in joined

    def test_falls_back_when_origin_missing(self, runner: FakeRunner) -> None:
        # First fetch + checkout from origin both fail; fallback `checkout -B name` succeeds.
        # We use the response key `git checkout -B` shared by both.
        def _runner(args, **kwargs):
            runner.calls.append(list(args))
            if args[:2] == ["git", "fetch"]:
                return _ok(returncode=1, stderr="no origin")
            if args[:3] == ["git", "checkout", "-B"] and len(args) > 4:
                return _ok(returncode=1, stderr="origin/main not found")
            return _ok()

        checkout_new_branch("claude/daily-2026-05-11/ai-agents", runner=_runner)
        # The fallback (4-arg) checkout should have been called.
        assert any(c[:3] == ["git", "checkout", "-B"] and len(c) == 4 for c in runner.calls)


class TestStageAndCommit:
    def test_stages_all_paths_by_default(self, runner: FakeRunner) -> None:
        runner.responses = {"git rev-parse HEAD": _ok(stdout="abc123\n")}
        sha = stage_and_commit("test commit", runner=runner)
        assert sha == "abc123"
        cmds = [c[:2] for c in runner.calls]
        assert ["git", "add"] in cmds
        assert ["git", "commit"] in cmds

    def test_stages_specific_paths(self, runner: FakeRunner) -> None:
        runner.responses = {"git rev-parse HEAD": _ok(stdout="def456\n")}
        stage_and_commit("test", paths=["wiki/foo.md", "wiki/bar.md"], runner=runner)
        adds = [c for c in runner.calls if c[:2] == ["git", "add"]]
        assert any("wiki/foo.md" in c for c in adds)


class TestPushBranch:
    def test_push_with_upstream(self, runner: FakeRunner) -> None:
        push_branch("claude/daily-2026-05-11/ai-agents", runner=runner)
        assert runner.calls[0] == [
            "git",
            "push",
            "-u",
            "origin",
            "claude/daily-2026-05-11/ai-agents",
        ]


class TestCreatePr:
    def test_returns_pr_ref(self, runner: FakeRunner) -> None:
        runner.responses = {"gh pr create": _ok(stdout="https://github.com/x/y/pull/42\n")}
        ref = create_pr(title="t", body="b", runner=runner)
        assert ref.number == 42
        assert ref.url == "https://github.com/x/y/pull/42"

    def test_args_include_base_and_title(self, runner: FakeRunner) -> None:
        runner.responses = {"gh pr create": _ok(stdout="https://github.com/x/y/pull/1\n")}
        create_pr(title="My PR", body="body", base="main", runner=runner)
        call = runner.calls[0]
        assert "--title" in call and call[call.index("--title") + 1] == "My PR"
        assert "--base" in call and call[call.index("--base") + 1] == "main"


class TestViewPr:
    def test_parses_gh_json(self, runner: FakeRunner) -> None:
        payload = json.dumps(
            {
                "number": 7,
                "state": "OPEN",
                "files": [{"path": "wiki/concepts/x.md"}, {"path": "wiki/concepts/y.md"}],
                "additions": 50,
                "deletions": 5,
                "isDraft": False,
                "statusCheckRollup": [{"conclusion": "SUCCESS"}],
            }
        )
        runner.responses = {"gh pr view": _ok(stdout=payload)}
        view = view_pr(7, runner=runner)
        assert view.number == 7
        assert view.files == ["wiki/concepts/x.md", "wiki/concepts/y.md"]
        assert view.additions == 50
        assert view.checks_passing is True

    def test_failing_checks_detected(self, runner: FakeRunner) -> None:
        payload = json.dumps(
            {
                "number": 7,
                "state": "OPEN",
                "files": [],
                "additions": 0,
                "deletions": 0,
                "isDraft": False,
                "statusCheckRollup": [{"conclusion": "FAILURE"}, {"conclusion": "SUCCESS"}],
            }
        )
        runner.responses = {"gh pr view": _ok(stdout=payload)}
        view = view_pr(7, runner=runner)
        assert view.checks_passing is False


class TestEvaluateGate:
    def _view(self, **overrides) -> PRView:
        defaults = {
            "number": 1,
            "state": "OPEN",
            "files": ["wiki/concepts/x.md"],
            "additions": 10,
            "deletions": 1,
            "checks_passing": True,
            "is_draft": False,
        }
        defaults.update(overrides)
        return PRView(**defaults)

    def test_clean_pr_passes_daily(self) -> None:
        d = evaluate_gate(self._view(), route=ROUTE_DAILY_RESEARCH, config=_config())
        assert d.automerge is True
        assert d.reasons == []

    def test_too_many_files_fails(self) -> None:
        files = [f"wiki/concepts/x{i}.md" for i in range(50)]
        d = evaluate_gate(self._view(files=files), route=ROUTE_DAILY_RESEARCH, config=_config())
        assert d.automerge is False
        assert any("touches" in r and "files" in r for r in d.reasons)

    def test_too_many_lines_fails(self) -> None:
        d = evaluate_gate(self._view(additions=2000), route=ROUTE_DAILY_RESEARCH, config=_config())
        assert d.automerge is False
        assert any("lines" in r for r in d.reasons)

    def test_phase9_busy_day_passes_with_bumped_thresholds(self) -> None:
        # Phase 9 raised daily thresholds from 40/1500 to 80/3000 so a
        # busy-but-legitimate day (6-8 sources × 10-15 page touches) lands
        # cleanly. 75 files / 2800 lines should pass under the new gate.
        bumped = AutomergeRoute(max_files_changed_per_topic=80, max_total_diff_lines_per_topic=3000)
        files = [f"wiki/concepts/x{i}.md" for i in range(75)]
        d = evaluate_gate(
            self._view(files=files, additions=2700, deletions=100),
            route=ROUTE_DAILY_RESEARCH,
            config=_config(daily=bumped),
        )
        assert d.automerge is True, d.reasons

    def test_phase9_safety_cap_day_blocks_for_human_review(self) -> None:
        # A topic that hits the 20-source safety cap will commonly produce
        # 90+ files / 3200+ diff lines — that's MEANT to trip the gate so a
        # human reviews. 90 files at 80 max -> blocked.
        bumped = AutomergeRoute(max_files_changed_per_topic=80, max_total_diff_lines_per_topic=3000)
        files = [f"wiki/concepts/x{i}.md" for i in range(90)]
        d = evaluate_gate(
            self._view(files=files, additions=3200, deletions=100),
            route=ROUTE_DAILY_RESEARCH,
            config=_config(daily=bumped),
        )
        assert d.automerge is False
        assert any("touches" in r and "files" in r for r in d.reasons)
        assert any("lines" in r for r in d.reasons)

    def test_failing_checks_fails(self) -> None:
        d = evaluate_gate(
            self._view(checks_passing=False), route=ROUTE_DAILY_RESEARCH, config=_config()
        )
        assert d.automerge is False
        assert any("CI checks" in r for r in d.reasons)

    def test_draft_blocks(self) -> None:
        d = evaluate_gate(self._view(is_draft=True), route=ROUTE_DAILY_RESEARCH, config=_config())
        assert d.automerge is False
        assert any("draft" in r for r in d.reasons)

    def test_human_only_change_blocks(self) -> None:
        d = evaluate_gate(
            self._view(files=["CLAUDE.md", "wiki/concepts/x.md"]),
            route=ROUTE_DAILY_RESEARCH,
            config=_config(),
        )
        assert d.automerge is False
        assert "CLAUDE.md" in d.blocked_paths

    def test_human_only_topics_yaml_blocks(self) -> None:
        d = evaluate_gate(
            self._view(files=["topics.yaml"]), route=ROUTE_DAILY_RESEARCH, config=_config()
        )
        assert "topics.yaml" in d.blocked_paths

    def test_human_only_purpose_md_blocks(self) -> None:
        d = evaluate_gate(
            self._view(files=["wiki/topics/ai-agents/purpose.md"]),
            route=ROUTE_DAILY_RESEARCH,
            config=_config(),
        )
        assert any("purpose.md" in p for p in d.blocked_paths)

    def test_human_only_underscore_scratch_blocks(self) -> None:
        """``wiki/_*.md`` is the personal-scratch convention; LLM PRs must not touch it."""
        d = evaluate_gate(
            self._view(
                files=[
                    "wiki/_dashboard.md",
                    "wiki/concepts/_scratch.md",
                    "wiki/concepts/transformer-attention.md",
                ]
            ),
            route=ROUTE_DAILY_RESEARCH,
            config=_config(),
        )
        assert any("_dashboard.md" in p for p in d.blocked_paths)
        assert any("_scratch.md" in p for p in d.blocked_paths)
        assert "wiki/concepts/transformer-attention.md" not in d.blocked_paths

    def test_block_human_disabled(self) -> None:
        d = evaluate_gate(
            self._view(files=["CLAUDE.md"]),
            route=ROUTE_DAILY_RESEARCH,
            config=_config(block_human=False),
        )
        assert d.blocked_paths == []
        assert d.automerge is True

    def test_query_route_uses_smaller_thresholds(self) -> None:
        # 9 files exceeds the wiki_query gate (max 8) but is fine for daily (max 40).
        files = [f"wiki/concepts/x{i}.md" for i in range(9)]
        d_query = evaluate_gate(self._view(files=files), route=ROUTE_WIKI_QUERY, config=_config())
        d_daily = evaluate_gate(
            self._view(files=files), route=ROUTE_DAILY_RESEARCH, config=_config()
        )
        assert d_query.automerge is False
        assert d_daily.automerge is True

    def test_weekly_route_permissive(self) -> None:
        files = [f"wiki/concepts/x{i}.md" for i in range(50)]
        d = evaluate_gate(self._view(files=files), route=ROUTE_WEEKLY_HEALTH, config=_config())
        assert d.automerge is True

    def test_review_checklist_renders(self) -> None:
        d = evaluate_gate(
            self._view(files=["CLAUDE.md"], checks_passing=False),
            route=ROUTE_DAILY_RESEARCH,
            config=_config(),
        )
        out = d.render_review_checklist()
        assert "Auto-merge gate did not pass" in out
        assert "CLAUDE.md" in out

    def test_unknown_route_raises(self) -> None:
        with pytest.raises(ValueError, match="Unknown route"):
            evaluate_gate(self._view(), route="not-a-route", config=_config())


class TestApplyGate:
    def test_passes_calls_automerge(self, runner: FakeRunner) -> None:
        payload = json.dumps(
            {
                "number": 1,
                "state": "OPEN",
                "files": [{"path": "wiki/concepts/x.md"}],
                "additions": 5,
                "deletions": 0,
                "isDraft": False,
                "statusCheckRollup": [{"conclusion": "SUCCESS"}],
            }
        )
        runner.responses = {"gh pr view": _ok(stdout=payload), "gh pr merge": _ok()}
        decision = apply_gate(1, route=ROUTE_DAILY_RESEARCH, config=_config(), runner=runner)
        assert decision.automerge is True
        assert any(c[:3] == ["gh", "pr", "merge"] for c in runner.calls)
        assert not any(c[:3] == ["gh", "pr", "comment"] for c in runner.calls)

    def test_fails_calls_comment(self, runner: FakeRunner) -> None:
        payload = json.dumps(
            {
                "number": 1,
                "state": "OPEN",
                "files": [{"path": "CLAUDE.md"}],  # human-only -> block
                "additions": 5,
                "deletions": 0,
                "isDraft": False,
                "statusCheckRollup": [{"conclusion": "SUCCESS"}],
            }
        )
        runner.responses = {"gh pr view": _ok(stdout=payload), "gh pr comment": _ok()}
        decision = apply_gate(1, route=ROUTE_DAILY_RESEARCH, config=_config(), runner=runner)
        assert decision.automerge is False
        assert any(c[:3] == ["gh", "pr", "comment"] for c in runner.calls)
        assert not any(c[:3] == ["gh", "pr", "merge"] for c in runner.calls)


class TestEnableAutomergeAndComment:
    def test_enable_automerge_args(self, runner: FakeRunner) -> None:
        enable_automerge(7, runner=runner)
        assert runner.calls[0] == ["gh", "pr", "merge", "7", "--squash", "--auto"]

    def test_comment_args(self, runner: FakeRunner) -> None:
        comment_pr(7, "hello", runner=runner)
        assert runner.calls[0][:3] == ["gh", "pr", "comment"]
        assert "hello" in runner.calls[0]


class TestPRBodyTemplates:
    def test_daily_body_includes_sections(self) -> None:
        body = render_pr_body_daily(
            topic_id="ai-agents",
            today=date(2026, 5, 11),
            sources_added=["[[example-1]]"],
            pages_touched=["wiki/concepts/x.md"],
            new_disputes=["[[A]] vs [[B]]"],
            new_open_questions=["question?"],
            report_path="wiki/reports/2026-05-11.md",
        )
        for section in ("Sources added", "Pages touched", "New disputes", "Run report"):
            assert section in body
        assert "ai-agents" in body

    def test_query_body_includes_sections(self) -> None:
        body = render_pr_body_query(
            question="what is X?",
            answer_slug="2026-05-11-what-is-x",
            sources_added=["[[src-1]]"],
            backfilled_pages=["wiki/concepts/y.md"],
            issue_url="https://github.com/x/y/issues/42",
        )
        assert "what is X?" in body
        assert "2026-05-11-what-is-x" in body
        assert "issues/42" in body

    def test_health_body_includes_sections(self) -> None:
        body = render_pr_body_health(
            today=date(2026, 5, 17),
            disputes_filed=["[[concept-x]]: paraphrase contradiction"],
            stale_pages=["wiki/concepts/old.md"],
            lint_summary="0 errors, 3 warnings",
            report_path="wiki/reports/health-2026-05-17.md",
        )
        for section in ("Disputes newly filed", "Stale pages", "Lint summary", "Health report"):
            assert section in body
