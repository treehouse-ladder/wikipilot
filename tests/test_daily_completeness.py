"""Tests for ``wikipilot.daily_completeness`` (sentinel for incomplete runs)."""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass, field
from datetime import date
from typing import Any

from wikipilot.config import BranchesConfig, TopicConfig
from wikipilot.daily_completeness import (
    DEFAULT_LABEL,
    CompletenessReport,
    TopicStatus,
    build_completeness_report,
    daily_topics,
    ensure_label,
    expected_report_branch,
    expected_topic_branches,
    find_existing_issue,
    open_or_update_issue,
    render_issue_body,
    render_issue_title,
)


@dataclass
class FakeRunner:
    """Records every subprocess call and replays canned responses keyed by prefix."""

    responses: dict[str, subprocess.CompletedProcess[str]] = field(default_factory=dict)
    calls: list[list[str]] = field(default_factory=list)

    def __call__(self, args, **kwargs):
        self.calls.append(list(args))
        key3 = " ".join(args[:3])
        key4 = " ".join(args[:4])
        if key4 in self.responses:
            return self.responses[key4]
        if key3 in self.responses:
            return self.responses[key3]
        return subprocess.CompletedProcess(args, 0, "[]", "")


def _ok(stdout: str = "", returncode: int = 0) -> subprocess.CompletedProcess[str]:
    return subprocess.CompletedProcess([], returncode, stdout, "")


def _topic(topic_id: str, *, frequency: str = "daily") -> TopicConfig:
    return TopicConfig(
        id=topic_id,
        display_name=topic_id,
        purpose="(unused in this test)",
        frequency=frequency,
    )


def _five_daily_topics() -> list[TopicConfig]:
    return [
        _topic("agentic-coding"),
        _topic("frontier-models"),
        _topic("ai-in-game-dev"),
        _topic("games-of-note"),
        _topic("game-music"),
    ]


_TODAY = date(2026, 5, 25)


# ---------------------------------------------------------------------------
# Pure helpers (no GH calls)
# ---------------------------------------------------------------------------


class TestDailyTopics:
    def test_filters_to_daily_frequency(self) -> None:
        topics = [
            _topic("daily-1", frequency="daily"),
            _topic("weekly-1", frequency="weekly"),
            _topic("daily-2", frequency="daily"),
        ]
        result = daily_topics(topics)
        assert [t.id for t in result] == ["daily-1", "daily-2"]


class TestExpectedBranches:
    def test_topic_branches_use_template(self) -> None:
        topics = _five_daily_topics()
        branches = expected_topic_branches(topics, today=_TODAY)
        assert branches["frontier-models"] == "claude/daily-2026-05-25/frontier-models"
        assert set(branches.keys()) == {t.id for t in topics}

    def test_report_branch_uses_underscore_report_slug(self) -> None:
        assert expected_report_branch(today=_TODAY) == "claude/daily-2026-05-25/_report"

    def test_custom_template_is_honored(self) -> None:
        cfg = BranchesConfig(daily_template="bot/daily-{date}/{topic_id}")
        branches = expected_topic_branches([_topic("x")], today=_TODAY, branches=cfg)
        assert branches["x"] == "bot/daily-2026-05-25/x"
        assert expected_report_branch(today=_TODAY, branches=cfg) == "bot/daily-2026-05-25/_report"


# ---------------------------------------------------------------------------
# build_completeness_report
# ---------------------------------------------------------------------------


def _merged_pr(
    *,
    number: int,
    branch: str,
    url: str | None = None,
) -> dict[str, Any]:
    return {
        "number": number,
        "headRefName": branch,
        "mergedAt": "2026-05-25T09:00:00Z",
        "url": url or f"https://github.com/x/wikipilot/pull/{number}",
    }


def _open_pr(*, number: int, branch: str) -> dict[str, Any]:
    return {
        "number": number,
        "headRefName": branch,
        "url": f"https://github.com/x/wikipilot/pull/{number}",
    }


@dataclass
class StateAwareRunner:
    """Runner that dispatches ``gh pr list`` calls by their ``--state`` value.

    The completeness module makes two distinct ``gh pr list`` calls per run
    (merged-on-today, then open-claude); a single keyed dict can't tell
    them apart. This runner inspects ``args`` and returns the merged or
    open payload accordingly. Other ``gh`` calls (e.g. ``gh issue list``)
    fall through to ``responses`` for the standard prefix match.
    """

    merged_payload: str = "[]"
    open_payload: str = "[]"
    responses: dict[str, subprocess.CompletedProcess[str]] = field(default_factory=dict)
    calls: list[list[str]] = field(default_factory=list)

    def __call__(self, args, **kwargs):
        self.calls.append(list(args))
        if args[:3] == ["gh", "pr", "list"]:
            # Locate the --state value; default to "open" if absent.
            state = "open"
            for i, arg in enumerate(args):
                if arg == "--state" and i + 1 < len(args):
                    state = args[i + 1]
                    break
            if state == "merged":
                return _ok(self.merged_payload)
            return _ok(self.open_payload)
        key3 = " ".join(args[:3])
        if key3 in self.responses:
            return self.responses[key3]
        return subprocess.CompletedProcess(args, 0, "[]", "")


def _fake_gh_runner(
    *,
    merged: list[dict] | None = None,
    open_: list[dict] | None = None,
) -> StateAwareRunner:
    return StateAwareRunner(
        merged_payload=json.dumps(merged or []),
        open_payload=json.dumps(open_ or []),
    )


class TestBuildCompletenessReport:
    def test_all_topics_merged_yields_no_gap(self) -> None:
        topics = _five_daily_topics()
        merged = [
            _merged_pr(
                number=100 + i,
                branch=f"claude/daily-2026-05-25/{t.id}",
            )
            for i, t in enumerate(topics)
        ]
        merged.append(_merged_pr(number=999, branch="claude/daily-2026-05-25/_report"))
        runner = _fake_gh_runner(merged=merged)
        report = build_completeness_report(topics=topics, today=_TODAY, runner=runner)
        assert {s.state for s in report.topic_results} == {"merged"}
        assert report.report_pr_state == "merged"
        assert report.has_gap() is False

    def test_three_topics_missing_pr_57_and_58_merged_matches_2026_05_25_incident(
        self,
    ) -> None:
        """The exact failure mode of 2026-05-25: 2 topics produced PRs and
        merged, 3 topics never produced PRs, no report PR."""
        topics = _five_daily_topics()
        merged = [
            _merged_pr(number=57, branch="claude/daily-2026-05-25/frontier-models"),
            _merged_pr(number=58, branch="claude/daily-2026-05-25/ai-in-game-dev"),
        ]
        runner = _fake_gh_runner(merged=merged)
        report = build_completeness_report(topics=topics, today=_TODAY, runner=runner)

        merged_ids = {s.topic_id for s in report.merged_topics}
        missing_ids = {s.topic_id for s in report.missing_topics}
        assert merged_ids == {"frontier-models", "ai-in-game-dev"}
        assert missing_ids == {"agentic-coding", "games-of-note", "game-music"}
        assert report.report_pr_state == "missing"
        assert report.has_gap() is True

    def test_open_topic_is_distinguished_from_missing(self) -> None:
        topics = [_topic("agentic-coding"), _topic("frontier-models")]
        merged = [
            _merged_pr(number=200, branch="claude/daily-2026-05-25/frontier-models"),
        ]
        open_prs = [
            _open_pr(number=201, branch="claude/daily-2026-05-25/agentic-coding"),
        ]
        runner = _fake_gh_runner(merged=merged, open_=open_prs)
        report = build_completeness_report(topics=topics, today=_TODAY, runner=runner)
        assert [s.state for s in report.topic_results] == ["open", "merged"]
        assert report.has_gap(flag_open_topics=False) is True  # report PR missing
        assert report.has_gap(flag_open_topics=True) is True

    def test_only_report_pr_open_still_files_an_issue(self) -> None:
        """Topics all merged but the report PR is still open — the
        sentinel should still flag a gap so a human can chase the
        report PR if it sits open overnight."""
        topics = [_topic("frontier-models")]
        merged = [
            _merged_pr(number=300, branch="claude/daily-2026-05-25/frontier-models"),
        ]
        open_prs = [
            _open_pr(number=301, branch="claude/daily-2026-05-25/_report"),
        ]
        runner = _fake_gh_runner(merged=merged, open_=open_prs)
        report = build_completeness_report(topics=topics, today=_TODAY, runner=runner)
        assert report.report_pr_state == "open"
        assert report.has_gap() is True

    def test_skips_weekly_topics(self) -> None:
        """Weekly Health topics are NOT expected to land daily; they
        should never be flagged as missing by the daily sentinel."""
        topics = [
            _topic("frontier-models", frequency="daily"),
            _topic("retired-topic", frequency="weekly"),
        ]
        merged = [
            _merged_pr(number=400, branch="claude/daily-2026-05-25/frontier-models"),
            _merged_pr(number=401, branch="claude/daily-2026-05-25/_report"),
        ]
        runner = _fake_gh_runner(merged=merged)
        report = build_completeness_report(topics=topics, today=_TODAY, runner=runner)
        assert report.expected_topic_ids == ["frontier-models"]
        assert report.has_gap() is False

    def test_gh_failure_yields_loud_missing_report(self) -> None:
        """A ``gh`` outage during the sentinel must NOT silently pass;
        it should look as bad as possible so the operator notices."""
        topics = _five_daily_topics()
        runner = FakeRunner(
            responses={
                "gh pr list": _ok(returncode=1, stdout=""),
            }
        )
        report = build_completeness_report(topics=topics, today=_TODAY, runner=runner)
        assert {s.state for s in report.topic_results} == {"missing"}
        assert report.report_pr_state == "missing"
        assert report.has_gap() is True


# ---------------------------------------------------------------------------
# render_issue_body
# ---------------------------------------------------------------------------


class TestRenderIssueBody:
    def test_title_includes_date(self) -> None:
        report = CompletenessReport(
            today=_TODAY,
            expected_topic_ids=[],
            topic_results=[],
            report_pr_state="missing",
        )
        title = render_issue_title(report)
        assert "2026-05-25" in title

    def test_body_lists_missing_topics_with_branch_names(self) -> None:
        report = CompletenessReport(
            today=_TODAY,
            expected_topic_ids=["a", "b", "c"],
            topic_results=[
                TopicStatus(
                    topic_id="a",
                    expected_branch="claude/daily-2026-05-25/a",
                    state="merged",
                    pr_number=10,
                    pr_url="https://example.com/10",
                ),
                TopicStatus(
                    topic_id="b",
                    expected_branch="claude/daily-2026-05-25/b",
                    state="missing",
                ),
                TopicStatus(
                    topic_id="c",
                    expected_branch="claude/daily-2026-05-25/c",
                    state="missing",
                ),
            ],
            report_pr_state="missing",
        )
        body = render_issue_body(report)
        assert "## Missing topics" in body
        assert "`b`" in body
        assert "`c`" in body
        assert "claude/daily-2026-05-25/b" in body
        assert "wikipilot research --topic b" in body
        assert "wikipilot research --topic c" in body

    def test_body_includes_recover_prs_hint_when_open_pr_exists(self) -> None:
        report = CompletenessReport(
            today=_TODAY,
            expected_topic_ids=["a"],
            topic_results=[
                TopicStatus(
                    topic_id="a",
                    expected_branch="claude/daily-2026-05-25/a",
                    state="open",
                    pr_number=42,
                    pr_url="https://example.com/42",
                ),
            ],
            report_pr_state="missing",
        )
        body = render_issue_body(report)
        assert "wikipilot recover-prs" in body

    def test_remediation_numbering_is_sequential_when_no_open_prs(self) -> None:
        """The remediation section numbers steps dynamically; today's
        2026-05-25 incident (3 missing topics, 0 open, no report PR)
        should number the steps 1. and 2., not 1. and 3."""
        report = CompletenessReport(
            today=_TODAY,
            expected_topic_ids=["a"],
            topic_results=[
                TopicStatus(
                    topic_id="a",
                    expected_branch="claude/daily-2026-05-25/a",
                    state="missing",
                ),
            ],
            report_pr_state="missing",
        )
        body = render_issue_body(report)
        assert "1. **Re-fire" in body
        assert "2. **Triage" in body
        assert "3. " not in body  # no orphaned third step

    def test_remediation_numbering_includes_recover_prs_step_when_relevant(
        self,
    ) -> None:
        report = CompletenessReport(
            today=_TODAY,
            expected_topic_ids=["a", "b"],
            topic_results=[
                TopicStatus(
                    topic_id="a",
                    expected_branch="claude/daily-2026-05-25/a",
                    state="missing",
                ),
                TopicStatus(
                    topic_id="b",
                    expected_branch="claude/daily-2026-05-25/b",
                    state="open",
                    pr_number=1,
                ),
            ],
            report_pr_state="missing",
        )
        body = render_issue_body(report)
        assert "1. **Re-fire" in body
        assert "2. **Unblock" in body
        assert "3. **Triage" in body


# ---------------------------------------------------------------------------
# find_existing_issue + open_or_update_issue
# ---------------------------------------------------------------------------


class TestExistingIssue:
    def test_finds_match_by_title_for_today(self) -> None:
        expected_title = render_issue_title(
            CompletenessReport(
                today=_TODAY,
                expected_topic_ids=[],
                topic_results=[],
                report_pr_state="missing",
            )
        )
        payload = json.dumps(
            [
                {"number": 99, "title": expected_title},
                {"number": 100, "title": "Some other thing"},
            ]
        )
        runner = FakeRunner(responses={"gh issue list": _ok(payload)})
        result = find_existing_issue(today=_TODAY, runner=runner)
        assert result == 99

    def test_no_match_returns_none(self) -> None:
        payload = json.dumps([{"number": 99, "title": "Unrelated"}])
        runner = FakeRunner(responses={"gh issue list": _ok(payload)})
        assert find_existing_issue(today=_TODAY, runner=runner) is None

    def test_gh_failure_returns_none(self) -> None:
        runner = FakeRunner(responses={"gh issue list": _ok(returncode=1, stdout="")})
        assert find_existing_issue(today=_TODAY, runner=runner) is None


class TestOpenOrUpdateIssue:
    def test_opens_new_issue_when_no_existing(self) -> None:
        runner = FakeRunner(
            responses={
                "gh issue list": _ok("[]"),
                "gh issue create": _ok(stdout="https://github.com/x/wikipilot/issues/77\n"),
            }
        )
        report = CompletenessReport(
            today=_TODAY,
            expected_topic_ids=["a"],
            topic_results=[
                TopicStatus(
                    topic_id="a",
                    expected_branch="claude/daily-2026-05-25/a",
                    state="missing",
                ),
            ],
            report_pr_state="missing",
        )
        result = open_or_update_issue(report, runner=runner)
        assert result == 77
        assert any(call[:3] == ["gh", "issue", "create"] for call in runner.calls)

    def test_edits_existing_issue_idempotently(self) -> None:
        expected_title = render_issue_title(
            CompletenessReport(
                today=_TODAY,
                expected_topic_ids=[],
                topic_results=[],
                report_pr_state="missing",
            )
        )
        list_payload = json.dumps([{"number": 88, "title": expected_title}])
        runner = FakeRunner(
            responses={
                "gh issue list": _ok(list_payload),
                "gh issue edit": _ok(stdout=""),
            }
        )
        report = CompletenessReport(
            today=_TODAY,
            expected_topic_ids=["a"],
            topic_results=[
                TopicStatus(
                    topic_id="a",
                    expected_branch="claude/daily-2026-05-25/a",
                    state="missing",
                ),
            ],
            report_pr_state="missing",
        )
        result = open_or_update_issue(report, runner=runner)
        assert result == 88
        # The runner saw `gh issue edit 88 ...`, NOT `gh issue create`.
        assert not any(call[:3] == ["gh", "issue", "create"] for call in runner.calls)
        assert any(call[:4] == ["gh", "issue", "edit", "88"] for call in runner.calls)

    def test_returns_none_on_gh_create_failure(self) -> None:
        runner = FakeRunner(
            responses={
                "gh issue list": _ok("[]"),
                "gh issue create": _ok(returncode=1, stdout=""),
            }
        )
        report = CompletenessReport(
            today=_TODAY,
            expected_topic_ids=["a"],
            topic_results=[
                TopicStatus(
                    topic_id="a",
                    expected_branch="claude/daily-2026-05-25/a",
                    state="missing",
                ),
            ],
            report_pr_state="missing",
        )
        assert open_or_update_issue(report, runner=runner) is None

    def test_ensures_label_before_filing_issue(self) -> None:
        """Regression for the 2026-05-25 first-fire failure.

        Before this fix, the workflow run #26416243188 detected the gap
        correctly (`2 merged, 0 open, 3 missing`) but exited 1 because
        ``gh issue create --label daily-incomplete`` failed against a
        repo where the label had never been created. ``open_or_update_issue``
        now calls ``gh label create --force`` first.
        """
        runner = FakeRunner(
            responses={
                "gh issue list": _ok("[]"),
                "gh issue create": _ok(stdout="https://github.com/x/wikipilot/issues/77\n"),
            }
        )
        report = CompletenessReport(
            today=_TODAY,
            expected_topic_ids=["a"],
            topic_results=[
                TopicStatus(
                    topic_id="a",
                    expected_branch="claude/daily-2026-05-25/a",
                    state="missing",
                ),
            ],
            report_pr_state="missing",
        )
        result = open_or_update_issue(report, runner=runner)
        assert result == 77
        label_calls = [call for call in runner.calls if call[:3] == ["gh", "label", "create"]]
        assert len(label_calls) == 1
        assert label_calls[0][3] == DEFAULT_LABEL
        assert "--force" in label_calls[0]

    def test_aborts_when_label_creation_fails(self) -> None:
        """When ``gh label create --force`` itself fails, fail closed.

        Returning ``None`` (instead of pressing on with ``gh issue create``)
        gives the CLI a clean exit-1 signal that something at the GitHub
        layer is wrong, rather than silently producing a labelless issue.
        """
        runner = FakeRunner(
            responses={
                "gh label create": _ok(returncode=1, stdout=""),
            }
        )
        report = CompletenessReport(
            today=_TODAY,
            expected_topic_ids=["a"],
            topic_results=[
                TopicStatus(
                    topic_id="a",
                    expected_branch="claude/daily-2026-05-25/a",
                    state="missing",
                ),
            ],
            report_pr_state="missing",
        )
        assert open_or_update_issue(report, runner=runner) is None
        assert not any(call[:3] == ["gh", "issue", "create"] for call in runner.calls)
        assert not any(call[:3] == ["gh", "issue", "edit"] for call in runner.calls)


class TestEnsureLabel:
    def test_calls_gh_label_create_with_force_and_metadata(self) -> None:
        runner = FakeRunner(responses={"gh label create": _ok(stdout="")})
        assert ensure_label(runner=runner) is True
        assert len(runner.calls) == 1
        call = runner.calls[0]
        assert call[:3] == ["gh", "label", "create"]
        assert call[3] == DEFAULT_LABEL
        assert "--color" in call
        assert "--description" in call
        assert "--force" in call

    def test_returns_false_on_gh_failure(self) -> None:
        runner = FakeRunner(responses={"gh label create": _ok(returncode=1, stdout="")})
        assert ensure_label(runner=runner) is False

    def test_returns_false_on_oserror(self) -> None:
        def raising_runner(*args: Any, **kwargs: Any) -> Any:
            raise OSError("gh missing")

        assert ensure_label(runner=raising_runner) is False
