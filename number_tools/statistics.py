"""Simple statistical utilities."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List


@dataclass(frozen=True)
class SummaryStatistics:
    """Aggregate statistics computed from a numeric sequence."""

    count: int
    minimum: float
    maximum: float
    mean: float


def summarize(values: Iterable[float]) -> SummaryStatistics:
    """Compute count, min, max, and mean for ``values``."""
    collected: List[float] = list(values)
    if not collected:
        raise ValueError("summarize() requires at least one value")
    total = sum(collected)
    return SummaryStatistics(
        count=len(collected),
        minimum=min(collected),
        maximum=max(collected),
        mean=total / len(collected),
    )

