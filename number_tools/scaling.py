"""Value scaling helpers."""
from __future__ import annotations

import math
from typing import Iterable, Sequence, Union

Number = Union[int, float]


def scale_linear(
    value: Number,
    source_min: Number,
    source_max: Number,
    target_min: Number,
    target_max: Number,
) -> float:
    """Map ``value`` from the source range to the target range."""
    if source_min == source_max:
        raise ValueError("source_min and source_max cannot be equal")
    ratio = (value - source_min) / (source_max - source_min)
    return target_min + ratio * (target_max - target_min)


def rescale(
    value: Number,
    source_min: Number,
    source_max: Number,
    target_min: Number,
    target_max: Number,
) -> float:
    """Alias for :func:`scale_linear` for semantic clarity."""
    return scale_linear(value, source_min, source_max, target_min, target_max)


def normalize(
    value: Union[Number, Sequence[Number], Iterable[Number]],
    minimum: Number | None = None,
    maximum: Number | None = None,
) -> Union[float, list[float]]:
    """Normalize scalars or sequences into the range [0, 1].

    * When ``value`` is a scalar, ``minimum`` and ``maximum`` must be provided and
      the result is a single float that clamps to [0, 1].
    * When ``value`` is an iterable of numbers and ``minimum``/``maximum`` are
      omitted, the function returns a list where each element is normalized
      according to the min/max inside the iterable.
    """
    if minimum is None and maximum is None:
        if not isinstance(value, Iterable) or isinstance(value, (str, bytes)):
            raise ValueError(
                "Iterable normalization requires an iterable of numeric values"
            )
        sequence = list(value)
        if not sequence:
            return []
        low = min(sequence)
        high = max(sequence)
        if low == high:
            return [0.0 for _ in sequence]
        span = high - low
        return [(item - low) / span for item in sequence]

    if minimum is None or maximum is None:
        raise ValueError("minimum and maximum must both be supplied for scalar values")
    if minimum >= maximum:
        raise ValueError("minimum must be less than maximum")

    numeric_value = float(value)
    if numeric_value <= minimum:
        return 0.0
    if numeric_value >= maximum:
        return 1.0
    return (numeric_value - minimum) / (maximum - minimum)


def min_max_scale(
    values: Sequence[Number], feature_range: tuple[Number, Number] = (0.0, 1.0)
) -> list[float]:
    """Scale ``values`` into the provided feature range."""
    if not values:
        return []
    low = min(values)
    high = max(values)
    if low == high:
        return [feature_range[0] for _ in values]
    target_min, target_max = feature_range
    span = target_max - target_min
    source_span = high - low
    return [
        target_min + ((value - low) / source_span) * span for value in values
    ]


def standardize(values: Sequence[Number]) -> list[float]:
    """Return z-score standardization for the provided ``values``."""
    if not values:
        return []
    avg = sum(values) / len(values)
    variance = sum((value - avg) ** 2 for value in values) / len(values)
    if variance == 0:
        return [0.0 for _ in values]
    std = math.sqrt(variance)
    return [(value - avg) / std for value in values]
