"""Value scaling helpers."""
from __future__ import annotations


def normalize(value: float, minimum: float, maximum: float) -> float:
    """Scale ``value`` into the inclusive range [0, 1]."""
    if minimum >= maximum:
        raise ValueError("minimum must be less than maximum")
    if value <= minimum:
        return 0.0
    if value >= maximum:
        return 1.0
    return (value - minimum) / (maximum - minimum)

