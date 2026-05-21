"""Tests for ``wikipilot.api_client`` (credentials + HTTP fire path)."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import pytest

from wikipilot.api_client import (
    MAX_RETRIES,
    ApiClientError,
    CredentialsNotConfigured,
    credentials_path,
    fire,
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


@dataclass
class FakeResponse:
    """Stand-in for ``requests.Response``."""

    status_code: int = 200
    headers: dict[str, str] = field(default_factory=dict)
    json_payload: Any = field(default_factory=dict)
    text: str = ""
    raise_on_json: Exception | None = None

    def json(self) -> Any:
        if self.raise_on_json is not None:
            raise self.raise_on_json
        return self.json_payload


@dataclass
class RecordingPoster:
    """Records each POST and returns from a queue of pre-canned responses."""

    queue: list[FakeResponse | Exception]
    calls: list[dict[str, Any]] = field(default_factory=list)

    def __call__(
        self,
        url: str,
        *,
        json: dict[str, Any],
        headers: dict[str, str],
        timeout: float,
    ) -> FakeResponse:
        self.calls.append({"url": url, "json": json, "headers": dict(headers), "timeout": timeout})
        if not self.queue:
            raise AssertionError("RecordingPoster ran out of queued responses")
        nxt = self.queue.pop(0)
        if isinstance(nxt, Exception):
            raise nxt
        return nxt


@dataclass
class RecordingSleep:
    sleeps: list[float] = field(default_factory=list)

    def __call__(self, seconds: float) -> None:
        self.sleeps.append(seconds)


def _post_factory(responses: Iterable[FakeResponse | Exception]) -> RecordingPoster:
    return RecordingPoster(queue=list(responses))


class TestCredentialsPath:
    def test_env_override(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        custom = tmp_path / "custom.toml"
        monkeypatch.setenv("WIKIPILOT_CREDENTIALS_FILE", str(custom))
        assert credentials_path() == custom

    def test_default_location_returns_path(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("WIKIPILOT_CREDENTIALS_FILE", raising=False)
        path = credentials_path()
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


class TestFireSuccess:
    def test_research_no_topic(self, credentials_file: Path) -> None:
        post = _post_factory(
            [FakeResponse(status_code=202, json_payload={"run_id": "r-1"}, text="{}")]
        )
        sleep = RecordingSleep()
        response = fire_research(topic=None, path=credentials_file, http_post=post, sleep=sleep)
        assert response.ok
        assert response.status_code == 202
        assert response.routine == "research"
        assert response.body["run_id"] == "r-1"
        assert response.retries == 0
        assert sleep.sleeps == []
        # No topic_id in payload when omitted.
        assert post.calls[0]["json"] == {}

    def test_research_with_topic_payload(self, credentials_file: Path) -> None:
        post = _post_factory([FakeResponse(status_code=202, json_payload={"run_id": "x"})])
        fire_research(
            topic="ai-agents", path=credentials_file, http_post=post, sleep=RecordingSleep()
        )
        assert post.calls[0]["json"] == {"text": "topic_id=ai-agents"}
        assert post.calls[0]["url"].endswith("/abc/fire")

    def test_query_payload_and_headers(self, credentials_file: Path) -> None:
        post = _post_factory([FakeResponse(status_code=202, json_payload={"run_id": "q-1"})])
        fire_query("what is X?", path=credentials_file, http_post=post, sleep=RecordingSleep())
        call = post.calls[0]
        assert call["json"] == {"text": "what is X?"}
        assert call["headers"]["Authorization"] == "Bearer tok-query"
        assert call["headers"]["Content-Type"] == "application/json"
        assert call["headers"]["anthropic-beta"] == "experimental-cc-routine-2026-04-01"
        assert call["headers"]["anthropic-version"] == "2023-06-01"
        assert call["headers"]["User-Agent"].startswith("wikipilot-cli/")

    def test_query_strips_whitespace(self, credentials_file: Path) -> None:
        post = _post_factory([FakeResponse(status_code=202, json_payload={"run_id": "q-2"})])
        fire_query(
            "  hello world\n",
            path=credentials_file,
            http_post=post,
            sleep=RecordingSleep(),
        )
        assert post.calls[0]["json"] == {"text": "hello world"}

    def test_query_rejects_empty(self, credentials_file: Path) -> None:
        with pytest.raises(ApiClientError, match="non-empty"):
            fire_query("   ", path=credentials_file)


class TestFireFailures:
    def test_400_surfaces_error_message(self, credentials_file: Path) -> None:
        post = _post_factory([FakeResponse(status_code=400, json_payload={"error": "bad request"})])
        response = fire_query("x?", path=credentials_file, http_post=post, sleep=RecordingSleep())
        assert not response.ok
        assert response.status_code == 400
        assert response.error_message == "bad request"

    def test_500_default_message(self, credentials_file: Path) -> None:
        post = _post_factory([FakeResponse(status_code=500, json_payload={})])
        response = fire_query("x?", path=credentials_file, http_post=post, sleep=RecordingSleep())
        assert not response.ok
        assert response.error_message == "HTTP 500"

    def test_network_error_returns_structured(self, credentials_file: Path) -> None:
        post = _post_factory([ConnectionError("boom")])
        response = fire_query("x?", path=credentials_file, http_post=post, sleep=RecordingSleep())
        assert not response.ok
        assert response.status_code == 0
        assert response.error_message is not None
        assert "boom" in response.error_message

    def test_non_json_body_handled(self, credentials_file: Path) -> None:
        post = _post_factory(
            [
                FakeResponse(
                    status_code=502,
                    text="<html>bad gateway</html>",
                    raise_on_json=ValueError("not json"),
                )
            ]
        )
        response = fire_query("x?", path=credentials_file, http_post=post, sleep=RecordingSleep())
        assert not response.ok
        assert response.body == {}
        assert response.raw.startswith("<html>")


class TestFireRetry:
    def test_429_retried_with_retry_after(self, credentials_file: Path) -> None:
        post = _post_factory(
            [
                FakeResponse(status_code=429, headers={"Retry-After": "2"}),
                FakeResponse(status_code=429, headers={"Retry-After": "1"}),
                FakeResponse(status_code=202, json_payload={"run_id": "r-x"}),
            ]
        )
        sleep = RecordingSleep()
        response = fire_query("x?", path=credentials_file, http_post=post, sleep=sleep)
        assert response.ok
        assert response.retries == 2
        assert sleep.sleeps == [2.0, 1.0]
        assert len(post.calls) == 3

    def test_429_uses_exponential_backoff_when_no_retry_after(self, credentials_file: Path) -> None:
        post = _post_factory(
            [
                FakeResponse(status_code=429),
                FakeResponse(status_code=202, json_payload={"run_id": "y"}),
            ]
        )
        sleep = RecordingSleep()
        fire_query("x?", path=credentials_file, http_post=post, sleep=sleep)
        # First retry uses INITIAL_BACKOFF_SECONDS * 2**0 = 1.0.
        assert sleep.sleeps == [1.0]

    def test_429_gives_up_after_max_retries(self, credentials_file: Path) -> None:
        post = _post_factory(
            [FakeResponse(status_code=429, headers={"Retry-After": "0"})] * (MAX_RETRIES + 1)
        )
        sleep = RecordingSleep()
        response = fire_query("x?", path=credentials_file, http_post=post, sleep=sleep)
        assert not response.ok
        assert response.status_code == 429
        assert response.retries == MAX_RETRIES
        assert len(sleep.sleeps) == MAX_RETRIES

    def test_invalid_retry_after_falls_back_to_backoff(self, credentials_file: Path) -> None:
        post = _post_factory(
            [
                FakeResponse(status_code=429, headers={"Retry-After": "garbage"}),
                FakeResponse(status_code=202, json_payload={"run_id": "z"}),
            ]
        )
        sleep = RecordingSleep()
        fire_query("x?", path=credentials_file, http_post=post, sleep=sleep)
        # Garbage Retry-After triggers exponential backoff (1.0 on first retry).
        assert sleep.sleeps == [1.0]


class TestFireDirect:
    """Cover the lower-level ``fire`` entrypoint that fire_research/query wrap."""

    def test_passes_payload(self, credentials_file: Path) -> None:
        post = _post_factory([FakeResponse(status_code=202, json_payload={})])
        fire(
            "research",
            {"topic_id": "x", "extra": True},
            path=credentials_file,
            http_post=post,
            sleep=RecordingSleep(),
        )
        assert post.calls[0]["json"] == {"topic_id": "x", "extra": True}

    def test_unknown_routine_rejected(self, credentials_file: Path) -> None:
        with pytest.raises(ApiClientError, match="unknown routine"):
            fire("bogus", {}, path=credentials_file)
