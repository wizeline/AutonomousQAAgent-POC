"""Core helpers for the Autonomous QA agent."""
import math


def get_square_root(number: float) -> float:
    """Return the square root of ``number``."""
    return math.sqrt(number)


def is_positive_number(number: float) -> bool:
    """Return True when ``number`` is strictly greater than zero."""
    return number > 0

