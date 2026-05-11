"""Shared pytest fixtures for the wikipilot test suite.

The ``sample_vault`` fixture copies ``tests/fixtures/sample_vault/`` into a
temporary directory so each test gets a clean, writable vault. Tests that
need to mutate frontmatter or write new pages can do so without polluting
the canonical fixture.
"""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from wikipilot.wiki import Vault

FIXTURES_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture
def sample_vault(tmp_path: Path) -> Vault:
    """Yield a writable copy of the canonical sample vault."""
    src = FIXTURES_DIR / "sample_vault"
    dst = tmp_path / "wiki"
    shutil.copytree(src, dst)
    return Vault.at(dst)


@pytest.fixture
def sample_topics_path(tmp_path: Path) -> Path:
    """Yield a writable copy of the sample topics.yaml file."""
    src = FIXTURES_DIR / "sample_topics.yaml"
    dst = tmp_path / "topics.yaml"
    shutil.copy(src, dst)
    return dst


@pytest.fixture
def sample_config_path(tmp_path: Path) -> Path:
    """Yield a writable copy of the sample wikipilot.toml file."""
    src = FIXTURES_DIR / "sample_wikipilot.toml"
    dst = tmp_path / "wikipilot.toml"
    shutil.copy(src, dst)
    return dst
