"""Smoke tests: package imports and CLI is wired up."""

from __future__ import annotations

from click.testing import CliRunner


def test_package_imports() -> None:
    import wikipilot

    assert wikipilot.__version__


def test_cli_help_runs() -> None:
    from wikipilot.cli import main

    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "Wikipilot" in result.output


def test_cli_version_runs() -> None:
    from wikipilot.cli import main

    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert "wikipilot" in result.output.lower()


def test_all_subcommands_registered() -> None:
    from wikipilot.cli import main

    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    expected = [
        "lint",
        "init-vault",
        "validate-topics",
        "freshness-report",
        "deck",
        "index-wiki",
        "research",
        "query",
    ]
    for cmd in expected:
        assert cmd in result.output, f"{cmd} subcommand missing from CLI"
