"""Tests for ``scripts/disputes_seed.py`` overlap heuristics."""

from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

import disputes_seed
import pytest
from disputes_seed import (
    CandidateSet,
    SeedResult,
    seed_candidates,
)

from wikipilot.wiki import Vault


def _names(candidate: CandidateSet) -> set[str]:
    return {p for p in candidate.pages}


def _set_with_trigger(result: SeedResult, trigger: str) -> CandidateSet | None:
    for c in result.candidate_sets:
        if c.trigger == trigger:
            return c
    return None


class TestSeedCandidates:
    def test_returns_seed_result(self, sample_vault: Vault) -> None:
        result = seed_candidates(sample_vault, today=date(2026, 5, 11))
        assert isinstance(result, SeedResult)
        assert all(isinstance(c, CandidateSet) for c in result.candidate_sets)

    def test_per_source_set_for_recent_source(self, sample_vault: Vault) -> None:
        # The fixture has two sources fetched 2026-05-10; with today=2026-05-11
        # both fall in the default 7-day lookback. Each source is cited by at
        # least two synthesis pages, so a per-source set should be produced
        # for both.
        result = seed_candidates(sample_vault, today=date(2026, 5, 11))
        triggers = {c.trigger for c in result.candidate_sets}
        assert "source_example-paper-aabbccdd" in triggers
        # The example-paper set should include the pages that cite it AND
        # share other wikilinks (transformer-attention + stale-concept share
        # `[[ai-agents]]` via see-also).
        eg = _set_with_trigger(result, "source_example-paper-aabbccdd")
        assert eg is not None
        names = _names(eg)
        assert "concepts/transformer-attention.md" in names
        assert "concepts/stale-concept.md" in names

    def test_lookback_window_excludes_old_sources(self, sample_vault: Vault) -> None:
        # With today >> fetched_at + lookback, no per-source set should fire.
        result = seed_candidates(
            sample_vault,
            today=date(2026, 12, 31),
            lookback_days=7,
        )
        triggers = {c.trigger for c in result.candidate_sets}
        assert not any(t.startswith("source_") for t in triggers)

    def test_stale_sweep_picks_oldest_pages(self, sample_vault: Vault) -> None:
        result = seed_candidates(
            sample_vault,
            today=date(2026, 12, 31),
            lookback_days=7,
            stale_k=3,
        )
        stale = _set_with_trigger(result, "stale_sweep")
        assert stale is not None
        # The fixture's stale-concept (2024-01-01) must be in the sweep —
        # it's the oldest page by far.
        names = _names(stale)
        assert "concepts/stale-concept.md" in names

    def test_stale_sweep_excludes_pages_already_in_per_source_set(
        self, sample_vault: Vault
    ) -> None:
        result = seed_candidates(sample_vault, today=date(2026, 5, 11))
        per_source_pages: set[str] = set()
        for c in result.candidate_sets:
            if c.trigger.startswith("source_"):
                per_source_pages.update(c.pages)
        stale = _set_with_trigger(result, "stale_sweep")
        if stale is not None:
            assert per_source_pages.isdisjoint(set(stale.pages))

    def test_stale_sweep_skipped_with_too_few_candidates(self, sample_vault: Vault) -> None:
        # If we set stale_k=0, no stale_sweep set should be produced.
        result = seed_candidates(sample_vault, today=date(2026, 5, 11), stale_k=0)
        assert _set_with_trigger(result, "stale_sweep") is None

    def test_top_k_caps_per_source_set(self, sample_vault: Vault) -> None:
        # With top_k=1 on a source cited by multiple pages, the candidate
        # set should still produce at minimum 2 pages (a dispute needs two)
        # OR be skipped entirely. The implementation prefers to skip when
        # only one citer remains.
        result = seed_candidates(sample_vault, today=date(2026, 5, 11), top_k=1)
        for c in result.candidate_sets:
            if c.trigger.startswith("source_"):
                assert len(c.pages) >= 2 or len(c.pages) == 0

    def test_pages_are_relative_posix_paths(self, sample_vault: Vault) -> None:
        result = seed_candidates(sample_vault, today=date(2026, 5, 11))
        for c in result.candidate_sets:
            for p in c.pages:
                assert "\\" not in p
                # No absolute paths
                assert not p.startswith("/")


class TestSeedResultJsonRoundtrip:
    def test_json_shape(self, sample_vault: Vault) -> None:
        import json as _json

        result = seed_candidates(sample_vault, today=date(2026, 5, 11))
        payload = _json.loads(result.to_json())
        assert "candidate_sets" in payload
        assert isinstance(payload["candidate_sets"], list)
        for entry in payload["candidate_sets"]:
            assert set(entry.keys()) == {"trigger", "pages"}
            assert isinstance(entry["trigger"], str)
            assert isinstance(entry["pages"], list)
            for p in entry["pages"]:
                assert isinstance(p, str)


class TestSeedCandidatesEdgeCases:
    def test_empty_vault_no_sets(self, tmp_path: Path) -> None:
        from wikipilot.cli import _INDEX_SKELETON, _LOG_SKELETON

        empty = tmp_path / "wiki"
        empty.mkdir()
        for sub in ("topics", "concepts", "entities", "sources", "answers", "reports"):
            (empty / sub).mkdir()
        (empty / "index.md").write_text(_INDEX_SKELETON, encoding="utf-8")
        (empty / "log.md").write_text(_LOG_SKELETON.format(date="2026-05-11"), encoding="utf-8")
        result = seed_candidates(Vault.at(empty), today=date(2026, 5, 11))
        assert result.candidate_sets == ()

    def test_unreadable_page_skipped(
        self, sample_vault: Vault, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        # Drop a non-utf8 file in concepts/; seed_candidates should not crash.
        bad = sample_vault.dir_for("concepts") / "binary.md"
        bad.write_bytes(b"\x80\x81\x82\x83not utf 8")
        result = seed_candidates(sample_vault, today=date(2026, 5, 11))
        # Still produces some sets and didn't raise.
        assert result.candidate_sets


class TestRecentSourceWindowBoundary:
    def test_source_at_lookback_boundary_included(self, sample_vault: Vault) -> None:
        # Source fetched_at 2026-05-10; today = 2026-05-17 (7-day lookback).
        result = seed_candidates(
            sample_vault,
            today=date(2026, 5, 17),
            lookback_days=7,
        )
        triggers = {c.trigger for c in result.candidate_sets}
        assert any(t.startswith("source_") for t in triggers)

    def test_source_one_day_past_lookback_excluded(self, sample_vault: Vault) -> None:
        result = seed_candidates(
            sample_vault,
            today=date(2026, 5, 18),
            lookback_days=7,
        )
        triggers = {c.trigger for c in result.candidate_sets}
        assert not any(t.startswith("source_") for t in triggers)


class TestMainCli:
    def test_main_json_output(
        self,
        sample_vault: Vault,
        capsys: pytest.CaptureFixture[str],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.setattr(
            "sys.argv",
            ["disputes_seed.py", "--vault", str(sample_vault.root), "--json"],
        )
        rc = disputes_seed.main()
        assert rc == 0
        out = capsys.readouterr().out
        assert "candidate_sets" in out

    def test_main_human_output(
        self,
        sample_vault: Vault,
        capsys: pytest.CaptureFixture[str],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.setattr(
            "sys.argv",
            ["disputes_seed.py", "--vault", str(sample_vault.root)],
        )
        rc = disputes_seed.main()
        assert rc == 0
        out = capsys.readouterr().out
        # Either lists candidate sets or prints "No candidate sets" — both ok.
        assert "candidate set" in out.lower() or "no candidate sets" in out.lower()

    def test_main_missing_vault(
        self,
        tmp_path: Path,
        capsys: pytest.CaptureFixture[str],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.setattr(
            "sys.argv",
            ["disputes_seed.py", "--vault", str(tmp_path / "missing")],
        )
        rc = disputes_seed.main()
        assert rc == 2


# Sanity-check: lookback_days=1 + today equal to fetched_at still includes the source.
def test_same_day_source_included(sample_vault: Vault) -> None:
    result = seed_candidates(
        sample_vault,
        today=date(2026, 5, 10),  # same day as fetched_at
        lookback_days=1,
    )
    assert any(c.trigger.startswith("source_") for c in result.candidate_sets)


# Plus a quick check that adjusting lookback by one day matters at the boundary.
@pytest.mark.parametrize(
    "delta,expect_recent",
    [(timedelta(days=0), True), (timedelta(days=8), False)],
)
def test_lookback_inclusivity(sample_vault: Vault, delta: timedelta, expect_recent: bool) -> None:
    today = date(2026, 5, 10) + delta
    result = seed_candidates(sample_vault, today=today, lookback_days=7)
    has_recent = any(c.trigger.startswith("source_") for c in result.candidate_sets)
    assert has_recent is expect_recent
