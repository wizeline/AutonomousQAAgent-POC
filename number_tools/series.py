"""Helpers for working with numeric series."""
from __future__ import annotations

from typing import Iterable, List


class NumberSeries:
    """Mutable container that exposes rolling statistics over numeric data."""

    def __init__(self, initial_values: Iterable[float] | None = None) -> None:
        self._values: List[float] = []
        if initial_values is not None:
            for value in initial_values:
                self.add(value)

    def add(self, value: float) -> None:
        self._values.append(value)

    @property
    def values(self) -> List[float]:
        return list(self._values)

    def mean(self) -> float:
        if not self._values:
            raise ValueError("mean() is undefined for empty series")
        return sum(self._values) / len(self._values)

    def moving_average(self, window: int) -> List[float]:
        if window <= 0:
            raise ValueError("window must be positive")
        if window > len(self._values):
            raise ValueError("window cannot be larger than the series length")
        averages: List[float] = []
        for index in range(window - 1, len(self._values)):
            window_values = self._values[index - window + 1 : index + 1]
            averages.append(sum(window_values) / window)
        return averages

