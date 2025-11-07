"""Simple statistical utilities."""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Iterable, List, Sequence


def _collect(values: Iterable[float]) -> List[float]:
    collected = list(values)
    if not collected:
        raise ValueError("The input collection must contain at least one value.")
    return collected


def mean(values: Iterable[float]) -> float:
    collected = _collect(values)
    return sum(collected) / len(collected)


def median(values: Iterable[float]) -> float:
    collected = sorted(_collect(values))
    length = len(collected)
    mid = length // 2
    if length % 2 == 1:
        return collected[mid]
    return (collected[mid - 1] + collected[mid]) / 2


def mode(values: Iterable[float]) -> float:
    collected = _collect(values)
    counts = Counter(collected)
    most_common_count = max(counts.values())
    for value in collected:
        if counts[value] == most_common_count:
            return value
    raise RuntimeError("Unexpected failure to compute mode")


def variance(values: Iterable[float]) -> float:
    collected = _collect(values)
    if len(collected) == 1:
        return 0.0
    avg = mean(collected)
    return sum((item - avg) ** 2 for item in collected) / len(collected)


@dataclass(frozen=True)
class SummaryStatistics:
    """Aggregate statistics computed from a numeric sequence."""

    count: int
    minimum: float
    maximum: float
    mean: float


def summarize(values: Iterable[float]) -> SummaryStatistics:
    """Compute count, min, max, and mean for ``values``."""
    collected = _collect(values)
    total = sum(collected)
    return SummaryStatistics(
        count=len(collected),
        minimum=min(collected),
        maximum=max(collected),
        mean=total / len(collected),
    )
