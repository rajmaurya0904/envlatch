"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import envlatch


def test_version_is_set() -> None:
    assert envlatch.__version__
