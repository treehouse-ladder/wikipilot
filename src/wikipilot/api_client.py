"""Thin client for the Anthropic Claude Code Cloud Routines ``/fire`` endpoints.

This is the bridge between ``wikipilot research`` / ``wikipilot query`` on
the CLI and the Daily Research / Wiki Query routines running in the cloud.
The CLI commands resolve credentials from the file below, POST a single
request to the routine's ``/fire`` URL, and surface a structured
:class:`FireResponse`.

Credentials live at ``~/.config/wikipilot/credentials.toml``
(``%APPDATA%\\wikipilot\\credentials.toml`` on Windows). Override the
location at runtime with the ``WIKIPILOT_CREDENTIALS_FILE`` env var; CI
relies on this to avoid reading from the user's home directory.

```toml
[research]
fire_url = "https://api.anthropic.com/v1/routines/<id>/fire"
token    = "..."

[query]
fire_url = "https://api.anthropic.com/v1/routines/<id>/fire"
token    = "..."
```

Retry policy: on HTTP 429 (rate limit) we honor the ``Retry-After`` header
when present, otherwise back off exponentially up to ``MAX_RETRIES``. All
other 4xx/5xx responses surface immediately as a non-``ok``
:class:`FireResponse` so the caller can decide.
"""

from __future__ import annotations

import json
import os
import sys
import time
import tomllib
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Protocol

DEFAULT_TIMEOUT_SECONDS: float = 30.0
MAX_RETRIES: int = 3
INITIAL_BACKOFF_SECONDS: float = 1.0
MAX_BACKOFF_SECONDS: float = 30.0


class ApiClientError(RuntimeError):
    """Raised when the API client cannot complete a request."""


class CredentialsNotConfigured(ApiClientError):
    """Credentials file missing or incomplete for the requested route."""


@dataclass(frozen=True)
class RoutineCredentials:
    routine: str  # "research" or "query"
    fire_url: str
    token: str


@dataclass(frozen=True)
class FireResponse:
    ok: bool
    status_code: int
    routine: str
    body: dict[str, Any]
    raw: str
    retries: int = 0
    error_message: str | None = None


@dataclass
class _AttemptLog:
    """Internal log of HTTP attempts (used by tests via inspection)."""

    statuses: list[int] = field(default_factory=list)
    sleeps: list[float] = field(default_factory=list)


class HttpResponse(Protocol):
    """Minimal subset of ``requests.Response`` we depend on."""

    status_code: int
    headers: dict[str, str] | Any
    text: str

    def json(self) -> Any: ...


HttpPost = Callable[..., HttpResponse]
SleepFn = Callable[[float], None]


def credentials_path() -> Path:
    """Return the path to the user's wikipilot credentials file.

    Honors ``WIKIPILOT_CREDENTIALS_FILE`` for tests and CI.
    """
    override = os.environ.get("WIKIPILOT_CREDENTIALS_FILE")
    if override:
        return Path(override)
    if sys.platform == "win32":
        base = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
        return base / "wikipilot" / "credentials.toml"
    return Path.home() / ".config" / "wikipilot" / "credentials.toml"


def load_credentials(routine: str, *, path: Path | None = None) -> RoutineCredentials:
    """Load credentials for ``routine`` from the credentials file."""
    if routine not in {"research", "query"}:
        raise ApiClientError(f"unknown routine {routine!r}; expected 'research' or 'query'")
    cred_path = path or credentials_path()
    if not cred_path.exists():
        raise CredentialsNotConfigured(
            f"credentials file not found at {cred_path}; "
            "see docs/runbook.md 'Storing the API tokens'"
        )
    with cred_path.open("rb") as handle:
        data = tomllib.load(handle)
    section = data.get(routine)
    if not section:
        raise CredentialsNotConfigured(f"credentials file {cred_path} has no [{routine}] section")
    fire_url = section.get("fire_url")
    token = section.get("token")
    if not fire_url or not token:
        raise CredentialsNotConfigured(
            f"[{routine}] section in {cred_path} must define both 'fire_url' and 'token'"
        )
    return RoutineCredentials(routine=routine, fire_url=str(fire_url), token=str(token))


def _default_post(
    url: str, *, json: dict[str, Any], headers: dict[str, str], timeout: float
) -> HttpResponse:  # noqa: A002 — `json` matches requests' kwarg
    import requests  # imported lazily so test fakes don't pay the cost

    return requests.post(url, json=json, headers=headers, timeout=timeout)


def _backoff_seconds(attempt: int) -> float:
    """Exponential backoff capped at :data:`MAX_BACKOFF_SECONDS`."""
    return min(INITIAL_BACKOFF_SECONDS * (2**attempt), MAX_BACKOFF_SECONDS)


def _retry_after_seconds(headers: Any) -> float | None:
    if not hasattr(headers, "get"):
        return None
    for key in ("Retry-After", "retry-after", "RETRY-AFTER"):
        raw = headers.get(key)
        if raw is None:
            continue
        try:
            seconds = float(raw)
            if seconds >= 0:
                return seconds
        except (TypeError, ValueError):
            return None
    return None


def fire(
    routine: str,
    payload: dict[str, Any],
    *,
    path: Path | None = None,
    http_post: HttpPost | None = None,
    sleep: SleepFn | None = None,
    timeout: float = DEFAULT_TIMEOUT_SECONDS,
    max_retries: int = MAX_RETRIES,
) -> FireResponse:
    """POST ``payload`` to ``routine``'s ``/fire`` endpoint.

    Retries on HTTP 429 honoring ``Retry-After`` when present, capped at
    ``max_retries``. Other 4xx/5xx surface as a non-``ok`` response so the
    caller can present a structured error rather than raising.
    """
    creds = load_credentials(routine, path=path)
    poster = http_post or _default_post
    sleeper = sleep or time.sleep
    headers = {
        "Authorization": f"Bearer {creds.token}",
        "Content-Type": "application/json",
        "anthropic-beta": "claude-code-routines-2025-01-01",
        "User-Agent": "wikipilot-cli/0.1",
    }
    attempts = 0
    last_response: HttpResponse | None = None
    while True:
        attempts += 1
        try:
            response = poster(
                creds.fire_url,
                json=payload,
                headers=headers,
                timeout=timeout,
            )
        except Exception as exc:  # noqa: BLE001 — surface any transport error structurally
            return FireResponse(
                ok=False,
                status_code=0,
                routine=routine,
                body={},
                raw="",
                retries=attempts - 1,
                error_message=f"network error: {exc}",
            )

        last_response = response
        status = int(getattr(response, "status_code", 0))
        if status == 429 and attempts <= max_retries:
            wait = _retry_after_seconds(getattr(response, "headers", {}))
            if wait is None:
                wait = _backoff_seconds(attempts - 1)
            sleeper(wait)
            continue
        break

    assert last_response is not None  # loop body always assigns or returns
    status = int(getattr(last_response, "status_code", 0))
    raw = getattr(last_response, "text", "") or ""
    body: dict[str, Any]
    try:
        parsed = last_response.json() if callable(getattr(last_response, "json", None)) else None
        body = parsed if isinstance(parsed, dict) else {}
    except (ValueError, json.JSONDecodeError):
        body = {}
    ok = 200 <= status < 300
    error_message = None
    if not ok:
        message = body.get("error") if isinstance(body, dict) else None
        error_message = str(message) if message else f"HTTP {status}"
    return FireResponse(
        ok=ok,
        status_code=status,
        routine=routine,
        body=body,
        raw=raw,
        retries=attempts - 1,
        error_message=error_message,
    )


def fire_research(
    *,
    topic: str | None,
    path: Path | None = None,
    http_post: HttpPost | None = None,
    sleep: SleepFn | None = None,
) -> FireResponse:
    """Fire the Daily Research routine.

    ``topic=None`` runs the full daily fan-out; ``topic="<id>"`` restricts
    the run to one topic — handy for ad-hoc re-runs after iterating on a
    purpose.md.
    """
    payload: dict[str, Any] = {}
    if topic:
        payload["topic_id"] = topic
    return fire("research", payload, path=path, http_post=http_post, sleep=sleep)


def fire_query(
    question: str,
    *,
    path: Path | None = None,
    http_post: HttpPost | None = None,
    sleep: SleepFn | None = None,
) -> FireResponse:
    """Fire the Wiki Query routine with a free-text ``question``."""
    if not question or not question.strip():
        raise ApiClientError("question must be a non-empty string")
    return fire(
        "query",
        {"question": question.strip()},
        path=path,
        http_post=http_post,
        sleep=sleep,
    )
