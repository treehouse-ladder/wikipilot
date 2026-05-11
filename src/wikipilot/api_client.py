"""Thin client for the Anthropic Claude Code Cloud Routines ``/fire`` endpoints.

Phase 1 ships the public surface (``fire_research``, ``fire_query``,
``load_credentials``) so the CLI can import it. Phase 6 fills in the
real HTTP plumbing (bearer auth, ``429`` retry per Anthropic docs,
structured error reporting) and writes the credentials format.

Credentials live at ``~/.config/wikipilot/credentials.toml``:

```toml
[research]
fire_url = "https://api.anthropic.com/v1/routines/<id>/fire"
token    = "..."

[query]
fire_url = "https://api.anthropic.com/v1/routines/<id>/fire"
token    = "..."
```
"""

from __future__ import annotations

import os
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any


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


def fire_research(*, topic: str | None, path: Path | None = None) -> FireResponse:
    """POST a research-routine fire request. Phase 6 implements the HTTP call.

    Phase 1 raises :class:`ApiClientError` so the CLI can surface a clear
    "wired in Phase 6" message; this keeps the CLI shape stable from day one.
    """
    creds = load_credentials("research", path=path)  # validates credentials file
    raise ApiClientError(
        "wikipilot research is wired through the Cloud Routines /fire API "
        f"in Phase 6 (target route: {creds.fire_url}, topic={topic!r})"
    )


def fire_query(question: str, *, path: Path | None = None) -> FireResponse:
    """POST a query-routine fire request. Phase 6 implements the HTTP call."""
    creds = load_credentials("query", path=path)
    raise ApiClientError(
        "wikipilot query is wired through the Cloud Routines /fire API "
        f"in Phase 6 (target route: {creds.fire_url}, question={question!r})"
    )
