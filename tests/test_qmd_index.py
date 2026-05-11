"""Tests for ``wikipilot.qmd_index`` (subprocess-mocked)."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from unittest.mock import patch

from wikipilot.qmd_index import IndexResult, index_vault, qmd_available


def _fake_completed(
    returncode: int, stdout: str = "", stderr: str = ""
) -> subprocess.CompletedProcess:
    return subprocess.CompletedProcess(
        args=["qmd"], returncode=returncode, stdout=stdout, stderr=stderr
    )


class TestQmdAvailable:
    def test_real_check(self) -> None:
        # Whatever the host returns, qmd_available should match shutil.which.
        assert qmd_available() == (shutil.which("qmd") is not None)


class TestIndexVault:
    def test_qmd_missing_returns_clear_message(self, tmp_path: Path) -> None:
        with patch("wikipilot.qmd_index.qmd_available", return_value=False):
            result = index_vault(tmp_path)
        assert result.qmd_available is False
        assert result.ok is False
        assert "qmd not found" in result.message

    def test_qmd_success(self, tmp_path: Path) -> None:
        runner_calls: list[list[str]] = []

        def runner(args, **kwargs):
            runner_calls.append(list(args))
            return _fake_completed(0, stdout="indexed 7 files\n")

        with patch("wikipilot.qmd_index.qmd_available", return_value=True):
            result = index_vault(tmp_path, runner=runner)
        assert result.ok is True
        assert result.indexed_files == 7
        assert runner_calls[0][:2] == ["qmd", "index"]

    def test_qmd_full_flag_passed(self, tmp_path: Path) -> None:
        captured: list[list[str]] = []

        def runner(args, **kwargs):
            captured.append(list(args))
            return _fake_completed(0, stdout="indexed 1 files\n")

        with patch("wikipilot.qmd_index.qmd_available", return_value=True):
            index_vault(tmp_path, full=True, runner=runner)
        assert "--full" in captured[0]

    def test_qmd_failure(self, tmp_path: Path) -> None:
        def runner(args, **kwargs):
            return _fake_completed(2, stderr="boom")

        with patch("wikipilot.qmd_index.qmd_available", return_value=True):
            result = index_vault(tmp_path, runner=runner)
        assert result.ok is False
        assert result.qmd_available is True
        assert "boom" in result.message

    def test_index_result_dataclass(self) -> None:
        r = IndexResult(ok=True, qmd_available=True, indexed_files=3, message="ok")
        assert r.indexed_files == 3
