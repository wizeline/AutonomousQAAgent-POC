"""Helpers for working with numeric series."""
from __future__ import annotations

from typing import Iterable, List


def fibonacci(length: int) -> List[int]:
    if length < 0:
        raise ValueError("length must be non-negative")
    sequence: List[int] = []
    a, b = 0, 1
    for _ in range(length):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def arithmetic_sequence(start: float, step: float, count: int) -> List[float]:
    if count < 0:
        raise ValueError("count must be non-negative")
    return [start + step * i for i in range(count)]


def geometric_sequence(start: float, ratio: float, count: int) -> List[float]:
    if ratio == 0:
        raise ValueError("ratio must be non-zero")
    if count < 0:
        raise ValueError("count must be non-negative")
    sequence: List[float] = []
    value = start
    for _ in range(count):
        sequence.append(value)
        value *= ratio
    return sequence


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
