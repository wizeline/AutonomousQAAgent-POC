"""Value scaling helpers."""
from __future__ import annotations

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
