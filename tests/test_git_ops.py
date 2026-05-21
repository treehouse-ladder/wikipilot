"""Tests for ``wikipilot.git_ops`` (mocked git/gh subprocess)."""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass, field
from datetime import date

import pytest

from wikipilot.config import (
    AutomergeCommon,
    AutomergeRoute,
    BranchesConfig,
    ImagesConfig,
    PRWatcherConfig,
    WikipilotConfig,
)
from wikipilot.git_ops import (
    DEFAULT_GATE_DEDUPE_KEY,
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
    disable_automerge,
    enable_automerge,
    evaluate_gate,
    infer_route_from_branch,
    push_branch,
    render_pr_body_daily,
    render_pr_body_health,
    render_pr_body_query,
    stage_and_commit,
    view_pr,
    wait_for_ci,
)


@dataclass
class FakeRunner:
    """Records every subprocess call and replays canned responses.

    Accepts ``**kwargs`` so callers that pass ``timeout=...`` (e.g.
    :func:`wait_for_ci`) don't error out. The ``raises`` mapping lets a test
    say "raise this exception on the next call whose prefix matches" — used
    by the timeout/error-path tests.
    """

    responses: dict[str, subprocess.CompletedProcess[str]]
    calls: list[list[str]]
    raises: dict[str, BaseException] = field(default_factory=dict)

    def __call__(self, args, **kwargs):
        self.calls.append(list(args))
        key = " ".join(args[:3])
        if key in self.raises:
            raise self.raises[key]
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
    branches: BranchesConfig | None = None,
    pr_watcher: PRWatcherConfig | None = None,
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
        pr_watcher=pr_watcher or PRWatcherConfig(),
        images=ImagesConfig(),
        branches=branches or BranchesConfig(),
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


# ---------------------------------------------------------------------------
# PR Watcher additions (Phase: PR Watcher routine)
# ---------------------------------------------------------------------------


class TestInferRouteFromBranch:
    def test_daily_branch_maps_to_daily_research(self) -> None:
        assert (
            infer_route_from_branch("claude/daily-2026-05-21/ai-agents", _config())
            == ROUTE_DAILY_RESEARCH
        )

    def test_query_branch_maps_to_wiki_query(self) -> None:
        assert (
            infer_route_from_branch("claude/query-2026-05-21-what-is-qmd", _config())
            == ROUTE_WIKI_QUERY
        )

    def test_health_branch_maps_to_weekly_health(self) -> None:
        assert infer_route_from_branch("claude/health-2026-05-21", _config()) == ROUTE_WEEKLY_HEALTH

    @pytest.mark.parametrize(
        "branch",
        [
            "fix/some-branch",
            "main",
            "claude/random-branch",
            "",
            "feature/claude-impostor",
        ],
    )
    def test_non_matching_branches_return_none(self, branch: str) -> None:
        assert infer_route_from_branch(branch, _config()) is None

    def test_config_none_uses_defaults(self) -> None:
        """Calling without a config falls back to the BranchesConfig defaults."""
        assert infer_route_from_branch("claude/daily-2026-05-21/foo") == ROUTE_DAILY_RESEARCH
        assert infer_route_from_branch("claude/health-2026-05-21") == ROUTE_WEEKLY_HEALTH

    def test_custom_template_is_honoured(self) -> None:
        """Overriding [branches].daily_template moves the prefix accordingly."""
        custom = BranchesConfig(
            daily_template="bot/research-{date}/{topic_id}",
            query_template="bot/ask-{date}-{slug}",
            health_template="bot/sweep-{date}",
        )
        cfg = _config(branches=custom)
        assert infer_route_from_branch("bot/research-2026-05-21/x", cfg) == ROUTE_DAILY_RESEARCH
        assert infer_route_from_branch("bot/ask-2026-05-21-q", cfg) == ROUTE_WIKI_QUERY
        assert infer_route_from_branch("bot/sweep-2026-05-21", cfg) == ROUTE_WEEKLY_HEALTH
        # The old claude/* prefixes no longer match under the custom config.
        assert infer_route_from_branch("claude/daily-2026-05-21/x", cfg) is None

    def test_topic_id_with_slash_still_matches(self) -> None:
        """A topic-id containing a slash shouldn't break prefix matching."""
        assert (
            infer_route_from_branch("claude/daily-2026-05-21/games/of-note", _config())
            == ROUTE_DAILY_RESEARCH
        )

    def test_case_sensitive_prefix(self) -> None:
        """Branch matching is case-sensitive (GitHub refs are case-sensitive)."""
        assert infer_route_from_branch("CLAUDE/daily-2026-05-21/x", _config()) is None


class TestWaitForCi:
    def test_green_when_gh_exits_zero(self, runner: FakeRunner) -> None:
        runner.responses = {"gh pr checks": _ok()}
        assert wait_for_ci(7, runner=runner) is True

    def test_red_when_gh_exits_nonzero(self, runner: FakeRunner) -> None:
        runner.responses = {"gh pr checks": _ok(returncode=1, stderr="fail")}
        assert wait_for_ci(7, runner=runner) is False

    def test_timeout_returns_false_no_crash(self, runner: FakeRunner) -> None:
        runner.raises = {"gh pr checks": subprocess.TimeoutExpired(cmd="gh", timeout=1)}
        assert wait_for_ci(7, timeout_sec=1, runner=runner) is False

    def test_passes_interval_to_gh_args(self, runner: FakeRunner) -> None:
        runner.responses = {"gh pr checks": _ok()}
        wait_for_ci(99, interval_sec=15, runner=runner)
        call = runner.calls[0]
        assert "--watch" in call
        assert "--interval" in call
        assert call[call.index("--interval") + 1] == "15"
        assert "99" in call

    def test_timeout_forwarded_as_kwarg(self) -> None:
        """The hard timeout passes through to the runner's ``timeout`` kwarg."""
        captured: dict[str, object] = {}

        def fake_run(args, **kwargs):
            captured.update(kwargs)
            return subprocess.CompletedProcess(args, 0, "", "")

        wait_for_ci(7, timeout_sec=900, runner=fake_run)
        assert captured.get("timeout") == 900


def _gh_pr_view_payload(
    *,
    files: list[str] | None = None,
    additions: int = 5,
    deletions: int = 0,
    conclusion: str = "SUCCESS",
    state: str = "OPEN",
    is_draft: bool = False,
    number: int = 1,
) -> str:
    return json.dumps(
        {
            "number": number,
            "state": state,
            "files": [{"path": p} for p in (files or ["wiki/concepts/x.md"])],
            "additions": additions,
            "deletions": deletions,
            "isDraft": is_draft,
            "statusCheckRollup": [{"conclusion": conclusion}],
        }
    )


def _gh_comments_payload(comments: list[dict]) -> str:
    return json.dumps({"comments": comments})


class TestApplyGateModes:
    def test_read_only_pass_only_comments(self, runner: FakeRunner) -> None:
        runner.responses = {
            "gh pr view": _ok(stdout=_gh_pr_view_payload()),
        }
        decision = apply_gate(
            1, route=ROUTE_DAILY_RESEARCH, config=_config(), mode="read_only", runner=runner
        )
        assert decision.automerge is True
        assert any(c[:3] == ["gh", "pr", "comment"] for c in runner.calls)
        assert not any(c[:3] == ["gh", "pr", "merge"] for c in runner.calls)

    def test_read_only_block_only_comments(self, runner: FakeRunner) -> None:
        runner.responses = {
            "gh pr view": _ok(stdout=_gh_pr_view_payload(files=["CLAUDE.md"])),
        }
        decision = apply_gate(
            1, route=ROUTE_DAILY_RESEARCH, config=_config(), mode="read_only", runner=runner
        )
        assert decision.automerge is False
        assert any(c[:3] == ["gh", "pr", "comment"] for c in runner.calls)
        assert not any(c[:3] == ["gh", "pr", "merge"] for c in runner.calls)

    def test_enforce_pass_enables_automerge(self, runner: FakeRunner) -> None:
        runner.responses = {
            "gh pr view": _ok(stdout=_gh_pr_view_payload()),
        }
        decision = apply_gate(
            1, route=ROUTE_DAILY_RESEARCH, config=_config(), mode="enforce", runner=runner
        )
        assert decision.automerge is True
        merges = [c for c in runner.calls if c[:3] == ["gh", "pr", "merge"]]
        assert merges, "enforce mode + pass must call gh pr merge"
        assert "--squash" in merges[0]
        assert "--auto" in merges[0]

    def test_enforce_red_ci_disables_automerge_and_comments(self, runner: FakeRunner) -> None:
        runner.responses = {
            "gh pr view": _ok(stdout=_gh_pr_view_payload(conclusion="FAILURE")),
        }
        decision = apply_gate(
            1, route=ROUTE_DAILY_RESEARCH, config=_config(), mode="enforce", runner=runner
        )
        assert decision.automerge is False
        merges = [c for c in runner.calls if c[:3] == ["gh", "pr", "merge"]]
        assert merges, "enforce mode + red CI must call gh pr merge --disable-auto"
        assert "--disable-auto" in merges[0]
        assert any(c[:3] == ["gh", "pr", "comment"] for c in runner.calls)

    def test_enforce_red_ci_uses_allow_fail_on_disable_auto(self, runner: FakeRunner) -> None:
        """Calling --disable-auto on a PR with no queued auto-merge must not raise."""
        runner.responses = {
            "gh pr view": _ok(stdout=_gh_pr_view_payload(conclusion="FAILURE")),
            "gh pr merge": _ok(returncode=1, stderr="no auto-merge to disable"),
        }
        decision = apply_gate(
            1, route=ROUTE_DAILY_RESEARCH, config=_config(), mode="enforce", runner=runner
        )
        assert decision.automerge is False


class TestCommentDedupe:
    def test_no_dedupe_posts_new_comment(self, runner: FakeRunner) -> None:
        comment_pr(7, "hello", runner=runner)
        assert runner.calls[0][:3] == ["gh", "pr", "comment"]
        assert "hello" in runner.calls[0]

    def test_dedupe_with_no_existing_comment_posts_new(self, runner: FakeRunner) -> None:
        runner.responses = {"gh pr view": _ok(stdout=_gh_comments_payload([]))}
        comment_pr(7, "hello", runner=runner, dedupe_key=DEFAULT_GATE_DEDUPE_KEY)
        # First call inspects existing comments; second posts a new one.
        posts = [c for c in runner.calls if c[:3] == ["gh", "pr", "comment"]]
        assert posts, "must fall through to gh pr comment when no marker found"
        body = posts[0][posts[0].index("--body") + 1]
        assert f"<!-- {DEFAULT_GATE_DEDUPE_KEY} -->" in body
        assert "hello" in body

    def test_dedupe_with_existing_marker_edits_via_api(self, runner: FakeRunner) -> None:
        marker = f"<!-- {DEFAULT_GATE_DEDUPE_KEY} -->"
        existing = [{"id": 999, "body": f"{marker}\nold body"}]
        runner.responses = {
            "gh pr view": _ok(stdout=_gh_comments_payload(existing)),
            "gh repo view": _ok(stdout=json.dumps({"nameWithOwner": "owner/repo"})),
        }
        comment_pr(7, "fresh body", runner=runner, dedupe_key=DEFAULT_GATE_DEDUPE_KEY)
        api_calls = [c for c in runner.calls if c[:2] == ["gh", "api"]]
        posts = [c for c in runner.calls if c[:3] == ["gh", "pr", "comment"]]
        assert api_calls, "expected an edit via gh api"
        assert not posts, "must NOT post a new comment when an existing one was edited"
        edit_call = api_calls[0]
        assert "PATCH" in edit_call
        assert any("issues/comments/999" in arg for arg in edit_call)

    def test_dedupe_falls_back_when_owner_repo_unknown(self, runner: FakeRunner) -> None:
        """If gh repo view fails we must still post a new comment (no silent loss)."""
        marker = f"<!-- {DEFAULT_GATE_DEDUPE_KEY} -->"
        existing = [{"id": 999, "body": f"{marker}\nold body"}]
        runner.responses = {
            "gh pr view": _ok(stdout=_gh_comments_payload(existing)),
            "gh repo view": _ok(returncode=1, stderr="not a git repo"),
        }
        comment_pr(7, "fresh body", runner=runner, dedupe_key=DEFAULT_GATE_DEDUPE_KEY)
        posts = [c for c in runner.calls if c[:3] == ["gh", "pr", "comment"]]
        assert posts, "expected a fallback gh pr comment when repo view fails"

    def test_dedupe_marker_anchored_to_wikipilot_key(self, runner: FakeRunner) -> None:
        """A comment containing an unrelated HTML comment must NOT be matched."""
        existing = [{"id": 42, "body": "<!-- some-other-tool -->\nold body"}]
        runner.responses = {
            "gh pr view": _ok(stdout=_gh_comments_payload(existing)),
        }
        comment_pr(7, "fresh body", runner=runner, dedupe_key=DEFAULT_GATE_DEDUPE_KEY)
        api_calls = [c for c in runner.calls if c[:2] == ["gh", "api"]]
        posts = [c for c in runner.calls if c[:3] == ["gh", "pr", "comment"]]
        assert not api_calls
        assert posts, "must post a new comment when no matching wikipilot marker found"

    def test_dedupe_with_empty_comments_payload(self, runner: FakeRunner) -> None:
        """Malformed/empty gh pr view output must fall back to posting a new comment."""
        runner.responses = {"gh pr view": _ok(stdout="")}
        comment_pr(7, "hello", runner=runner, dedupe_key=DEFAULT_GATE_DEDUPE_KEY)
        posts = [c for c in runner.calls if c[:3] == ["gh", "pr", "comment"]]
        assert posts


class TestDisableAutomerge:
    def test_disable_args(self, runner: FakeRunner) -> None:
        disable_automerge(7, runner=runner)
        assert runner.calls[0][:3] == ["gh", "pr", "merge"]
        assert "--disable-auto" in runner.calls[0]
        assert "7" in runner.calls[0]

    def test_swallows_no_queued_automerge_error(self, runner: FakeRunner) -> None:
        runner.responses = {"gh pr merge": _ok(returncode=1, stderr="not enabled")}
        # Must not raise.
        disable_automerge(7, runner=runner)
