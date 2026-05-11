"""Tests for ``wikipilot.api_client`` (Phase 1: credentials handling).

Phase 6 layers actual HTTP / retry tests on top of these.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from wikipilot.api_client import (
    ApiClientError,
    CredentialsNotConfigured,
    credentials_path,
    fire_query,
    fire_research,
    load_credentials,
)


@pytest.fixture
def credentials_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    path = tmp_path / "credentials.toml"
    path.write_text(
        "[research]\n"
        'fire_url = "https://api.anthropic.com/v1/routines/abc/fire"\n'
        'token = "tok-research"\n'
        "\n"
        "[query]\n"
        'fire_url = "https://api.anthropic.com/v1/routines/def/fire"\n'
        'token = "tok-query"\n',
        encoding="utf-8",
    )
    monkeypatch.setenv("WIKIPILOT_CREDENTIALS_FILE", str(path))
    return path


class TestCredentialsPath:
    def test_env_override(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        custom = tmp_path / "custom.toml"
        monkeypatch.setenv("WIKIPILOT_CREDENTIALS_FILE", str(custom))
        assert credentials_path() == custom

    def test_default_location_exists(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("WIKIPILOT_CREDENTIALS_FILE", raising=False)
        path = credentials_path()
        # Just checking we get a Path; the actual location is platform-specific.
        assert isinstance(path, Path)


class TestLoadCredentials:
    def test_loads_research(self, credentials_file: Path) -> None:
        creds = load_credentials("research", path=credentials_file)
        assert creds.token == "tok-research"
        assert creds.fire_url.endswith("/abc/fire")

    def test_loads_query(self, credentials_file: Path) -> None:
        creds = load_credentials("query", path=credentials_file)
        assert creds.token == "tok-query"

    def test_unknown_routine(self, credentials_file: Path) -> None:
        with pytest.raises(ApiClientError, match="unknown routine"):
            load_credentials("bogus", path=credentials_file)

    def test_missing_file(self, tmp_path: Path) -> None:
        with pytest.raises(CredentialsNotConfigured):
            load_credentials("research", path=tmp_path / "nope.toml")

    def test_missing_section(self, tmp_path: Path) -> None:
        path = tmp_path / "creds.toml"
        path.write_text('[research]\nfire_url = "x"\ntoken = "y"\n', encoding="utf-8")
        with pytest.raises(CredentialsNotConfigured, match="\\[query\\]"):
            load_credentials("query", path=path)

    def test_missing_token(self, tmp_path: Path) -> None:
        path = tmp_path / "creds.toml"
        path.write_text('[research]\nfire_url = "x"\n', encoding="utf-8")
        with pytest.raises(CredentialsNotConfigured, match="fire_url"):
            load_credentials("research", path=path)


class TestFirePhase1Stubs:
    def test_research_raises_phase6_message(self, credentials_file: Path) -> None:
        with pytest.raises(ApiClientError, match="Phase 6"):
            fire_research(topic="ai-agents", path=credentials_file)

    def test_query_raises_phase6_message(self, credentials_file: Path) -> None:
        with pytest.raises(ApiClientError, match="Phase 6"):
            fire_query("what is X?", path=credentials_file)
