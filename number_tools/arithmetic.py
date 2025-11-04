"""Basic arithmetic helpers."""
from __future__ import annotations

import math


def get_square_root(number: float) -> float:
    """Return the square root of ``number`` using :func:`math.sqrt`."""
    return math.sqrt(number)


def is_positive_number(number: float) -> bool:
    """Return True when ``number`` is strictly greater than zero."""
    return number > 0


def factorial(number: int) -> int:
    """Return ``number``! for non-negative integers."""
    if number < 0:
        raise ValueError("factorial is undefined for negative numbers")
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result

