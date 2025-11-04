"""Entry point re-exporting helpers for legacy compatibility."""

from number_tools import (
    NumberSeries,
    SummaryStatistics,
    factorial,
    get_square_root,
    is_positive_number,
    normalize,
    summarize,
)

__all__ = [
    "get_square_root",
    "is_positive_number",
    "factorial",
    "normalize",
    "SummaryStatistics",
    "summarize",
    "NumberSeries",
]
