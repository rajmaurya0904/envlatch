"""Utility functions for envlatch package."""

from __future__ import annotations

__all__ = ["parse_bool"]


def parse_bool(value: str) -> bool:
    """Parse a string into a boolean.

    Accepts common truthy and falsy strings (case‑insensitive). Raises ``TypeError``
    if *value* is not a ``str`` and ``ValueError`` if the string cannot be
    interpreted as a boolean.
    """
    if not isinstance(value, str):
        raise TypeError("value must be a string")
    lowered = value.lower()
    if lowered in {"true", "1", "yes", "y"}:
        return True
    if lowered in {"false", "0", "no", "n"}:
        return False
    raise ValueError(f"Invalid boolean value: {value}")
