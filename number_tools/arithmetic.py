"""Basic arithmetic helpers."""
from __future__ import annotations

import math


def add(lhs: float, rhs: float) -> float:
    """Return the arithmetic sum of ``lhs`` and ``rhs``."""
    return lhs + rhs


def subtract(lhs: float, rhs: float) -> float:
    """Return the result of ``lhs`` minus ``rhs``."""
    return lhs - rhs


def multiply(lhs: float, rhs: float) -> float:
    """Return the product of ``lhs`` and ``rhs``."""
    return lhs * rhs


def divide(dividend: float, divisor: float) -> float:
    """Return ``dividend`` divided by ``divisor``."""
    if divisor == 0:
        raise ZeroDivisionError("division by zero is undefined")
    return dividend / divisor


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
