"""Configuration loaders for ``topics.yaml`` and ``wikipilot.toml``.

Both files are human-owned (per the file ownership matrix in ``CLAUDE.md``).
The loaders here parse them into typed dataclasses, validate against the
documented schema, and raise ``ConfigError`` with a useful message on any
violation. The CLI's ``validate-topics`` subcommand exposes the topics
validator directly so humans can sanity-check before a routine run.
"""

from __future__ import annotations

import sys
import tomllib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


class ConfigError(ValueError):
    """Raised when a configuration file violates its documented schema."""


VALID_FREQUENCIES: tuple[str, ...] = ("daily", "weekly")

VALID_TOPIC_KEYS: frozenset[str] = frozenset(
    {
        "id",
        "display_name",
        "purpose",
        "search_hints",
        "allowlist_domains",
        "frequency",
        "max_sources_per_run",
        "freshness_window_days",
    }
)

REQUIRED_TOPIC_KEYS: frozenset[str] = frozenset({"id", "display_name", "purpose"})


@dataclass(frozen=True)
class TopicConfig:
    """One entry in ``topics.yaml``."""

    id: str
    display_name: str
    purpose: str
    search_hints: tuple[str, ...] = ()
    allowlist_domains: tuple[str, ...] = ()
    frequency: str = "daily"
    max_sources_per_run: int = 3
    freshness_window_days: int = 30


@dataclass(frozen=True)
class AutomergeRoute:
    max_files_changed: int | None = None
    max_total_diff_lines: int | None = None
    max_files_changed_per_topic: int | None = None
    max_total_diff_lines_per_topic: int | None = None


@dataclass(frozen=True)
class AutomergeCommon:
    require_lint_green: bool = True
    require_tests_green: bool = True
    block_human_only_file_changes: bool = True


@dataclass(frozen=True)
class ImagesConfig:
    enabled: bool = True
    max_image_bytes: int = 5_242_880
    allowed_mimes: tuple[str, ...] = (
        "image/png",
        "image/jpeg",
        "image/gif",
        "image/webp",
        "image/svg+xml",
    )
    cleanup_orphans: bool = True


@dataclass(frozen=True)
class BranchesConfig:
    prefix: str = "claude"
    daily_template: str = "claude/daily-{date}/{topic_id}"
    query_template: str = "claude/query-{date}-{slug}"
    health_template: str = "claude/health-{date}"


@dataclass(frozen=True)
class PRWatcherConfig:
    """``[automerge.pr_watcher]`` — knobs for the PR Watcher routine.

    ``ci_wait_timeout_sec`` bounds the ``gh pr checks --watch`` wait inside
    the watcher session; a timeout is recoverable (the next
    ``pull_request.synchronize`` event re-fires the watcher). ``self_heal_max_attempts``
    caps the loop where the watcher dispatches ``wiki-linter`` to fix
    mechanical errors on ``claude/*`` PRs — tracked via the
    ``wikipilot:heal-attempt-{n}`` PR label.
    """

    ci_wait_timeout_sec: int = 1200
    self_heal_max_attempts: int = 3


@dataclass(frozen=True)
class WikipilotConfig:
    """Parsed ``wikipilot.toml``."""

    automerge_common: AutomergeCommon = field(default_factory=AutomergeCommon)
    daily_research: AutomergeRoute = field(default_factory=AutomergeRoute)
    wiki_query: AutomergeRoute = field(default_factory=AutomergeRoute)
    weekly_health: AutomergeRoute = field(default_factory=AutomergeRoute)
    pr_watcher: PRWatcherConfig = field(default_factory=PRWatcherConfig)
    images: ImagesConfig = field(default_factory=ImagesConfig)
    branches: BranchesConfig = field(default_factory=BranchesConfig)


def load_topics(path: Path | str) -> list[TopicConfig]:
    """Load and validate ``topics.yaml`` at ``path``."""
    raw = _read_yaml(Path(path))
    if raw is None:
        raise ConfigError(f"{path}: file is empty")
    if not isinstance(raw, dict):
        raise ConfigError(f"{path}: top-level must be a mapping with key 'topics:'")
    topics_raw = raw.get("topics")
    if topics_raw is None:
        raise ConfigError(f"{path}: missing 'topics:' key")
    if not isinstance(topics_raw, list):
        raise ConfigError(f"{path}: 'topics:' must be a list (got {type(topics_raw).__name__})")
    topics = [
        _topic_from_dict(entry, source=str(path), index=i) for i, entry in enumerate(topics_raw)
    ]
    _check_unique_ids(topics, source=str(path))
    return topics


def load_wikipilot_config(path: Path | str) -> WikipilotConfig:
    """Load ``wikipilot.toml``; missing keys fall back to documented defaults."""
    p = Path(path)
    if not p.exists():
        return WikipilotConfig()
    with p.open("rb") as handle:
        data = tomllib.load(handle)
    return _config_from_dict(data, source=str(p))


def _read_yaml(path: Path) -> Any:
    if not path.exists():
        raise ConfigError(f"{path}: file does not exist")
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def _topic_from_dict(entry: Any, *, source: str, index: int) -> TopicConfig:
    if not isinstance(entry, dict):
        raise ConfigError(
            f"{source}: topics[{index}] must be a mapping (got {type(entry).__name__})"
        )
    keys = set(entry.keys())
    unknown = keys - VALID_TOPIC_KEYS
    if unknown:
        raise ConfigError(
            f"{source}: topics[{index}] has unknown keys: {sorted(unknown)}; valid keys are {sorted(VALID_TOPIC_KEYS)}"
        )
    missing = REQUIRED_TOPIC_KEYS - keys
    if missing:
        raise ConfigError(f"{source}: topics[{index}] missing required keys: {sorted(missing)}")
    topic_id = entry["id"]
    if not isinstance(topic_id, str) or not topic_id:
        raise ConfigError(f"{source}: topics[{index}].id must be a non-empty string")
    display_name = entry["display_name"]
    if not isinstance(display_name, str) or not display_name:
        raise ConfigError(f"{source}: topics[{index}].display_name must be a non-empty string")
    purpose = entry["purpose"]
    if not isinstance(purpose, str) or not purpose.strip():
        raise ConfigError(
            f"{source}: topics[{index}].purpose must be a non-empty string "
            "(this powers the off-topic rejection in topic-researcher)"
        )
    frequency = entry.get("frequency", "daily")
    if frequency not in VALID_FREQUENCIES:
        raise ConfigError(
            f"{source}: topics[{index}].frequency must be one of {VALID_FREQUENCIES} (got {frequency!r})"
        )
    search_hints = _coerce_str_list(
        entry.get("search_hints", []), where=f"{source}: topics[{index}].search_hints"
    )
    allowlist_domains = _coerce_str_list(
        entry.get("allowlist_domains", []), where=f"{source}: topics[{index}].allowlist_domains"
    )
    max_sources = _coerce_positive_int(
        entry.get("max_sources_per_run", 3), where=f"{source}: topics[{index}].max_sources_per_run"
    )
    freshness = _coerce_positive_int(
        entry.get("freshness_window_days", 30),
        where=f"{source}: topics[{index}].freshness_window_days",
    )
    return TopicConfig(
        id=topic_id,
        display_name=display_name,
        purpose=purpose,
        search_hints=tuple(search_hints),
        allowlist_domains=tuple(allowlist_domains),
        frequency=frequency,
        max_sources_per_run=max_sources,
        freshness_window_days=freshness,
    )


def _check_unique_ids(topics: list[TopicConfig], *, source: str) -> None:
    seen: dict[str, int] = {}
    for i, topic in enumerate(topics):
        if topic.id in seen:
            raise ConfigError(
                f"{source}: duplicate topic id {topic.id!r} at indices {seen[topic.id]} and {i}"
            )
        seen[topic.id] = i


def _coerce_str_list(value: Any, *, where: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise ConfigError(f"{where} must be a list of strings (got {type(value).__name__})")
    out: list[str] = []
    for i, item in enumerate(value):
        if not isinstance(item, str):
            raise ConfigError(f"{where}[{i}] must be a string (got {type(item).__name__})")
        out.append(item)
    return out


def _coerce_positive_int(value: Any, *, where: str) -> int:
    try:
        coerced = int(value)
    except (TypeError, ValueError) as exc:
        raise ConfigError(f"{where} must be a positive integer (got {value!r})") from exc
    if coerced <= 0:
        raise ConfigError(f"{where} must be a positive integer (got {coerced})")
    return coerced


def _config_from_dict(data: dict[str, Any], *, source: str) -> WikipilotConfig:
    automerge = data.get("automerge", {}) or {}
    common = AutomergeCommon(**(automerge.get("common", {}) or {}))
    daily = AutomergeRoute(**(automerge.get("daily_research", {}) or {}))
    query = AutomergeRoute(**(automerge.get("wiki_query", {}) or {}))
    weekly = AutomergeRoute(**(automerge.get("weekly_health", {}) or {}))
    pr_watcher = _pr_watcher_from_dict(automerge.get("pr_watcher", {}) or {}, source=source)
    images_data = data.get("images", {}) or {}
    if "allowed_mimes" in images_data:
        images_data = {**images_data, "allowed_mimes": tuple(images_data["allowed_mimes"])}
    images = ImagesConfig(**images_data)
    branches = BranchesConfig(**(data.get("branches", {}) or {}))
    try:
        return WikipilotConfig(
            automerge_common=common,
            daily_research=daily,
            wiki_query=query,
            weekly_health=weekly,
            pr_watcher=pr_watcher,
            images=images,
            branches=branches,
        )
    except TypeError as exc:
        # Surface unknown keys with the file path attached.
        raise ConfigError(f"{source}: invalid wikipilot.toml: {exc}") from exc


def _pr_watcher_from_dict(data: dict[str, Any], *, source: str) -> PRWatcherConfig:
    timeout = _coerce_positive_int(
        data.get("ci_wait_timeout_sec", 1200),
        where=f"{source}: [automerge.pr_watcher].ci_wait_timeout_sec",
    )
    attempts = _coerce_positive_int(
        data.get("self_heal_max_attempts", 3),
        where=f"{source}: [automerge.pr_watcher].self_heal_max_attempts",
    )
    unknown = set(data.keys()) - {"ci_wait_timeout_sec", "self_heal_max_attempts"}
    if unknown:
        raise ConfigError(f"{source}: [automerge.pr_watcher] has unknown keys: {sorted(unknown)}")
    return PRWatcherConfig(
        ci_wait_timeout_sec=timeout,
        self_heal_max_attempts=attempts,
    )


if __name__ == "__main__":  # pragma: no cover
    print(load_topics(sys.argv[1]))
