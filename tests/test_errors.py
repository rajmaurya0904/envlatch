"""Tests for error handling and edge cases in envlatch.util.parse_bool."""

import pytest

from envlatch.util import parse_bool


def test_parse_bool_type_error() -> None:
    with pytest.raises(TypeError):
        parse_bool(123)  # non‑string should raise TypeError


def test_parse_bool_value_error() -> None:
    with pytest.raises(ValueError):
        parse_bool("maybe")  # not a recognized boolean string


def test_parse_bool_case_insensitivity() -> None:
    # Upper‑case variants should be accepted
    assert parse_bool("TRUE") is True
    assert parse_bool("FaLsE") is False


def test_parse_bool_numeric_strings() -> None:
    assert parse_bool("1") is True
    assert parse_bool("0") is False
