"""Entry point re-exporting helpers for legacy compatibility."""
from __future__ import annotations

from typing import TYPE_CHECKING

from number_tools import (
    NumberSeries,
    SummaryStatistics,
    add,
    arithmetic_sequence,
    divide,
    factorial,
    fibonacci,
    geometric_sequence,
    get_square_root,
    is_positive_number,
    mean,
    median,
    mode,
    normalize,
    scale_linear,
    multiply,
    subtract,
    summarize,
    variance,
)

if TYPE_CHECKING:  # pragma: no cover
    from auto_agent import AutoAgent


def main() -> AutoAgent:
    """Instantiate an AutoAgent and print a short status message."""
    from auto_agent import AutoAgent as _AutoAgent

    agent = _AutoAgent()
    agent.activate()
    print(f"{agent.name} initialized in state: {agent.state}")
    agent.reset()
    return agent


__all__ = [
    "get_square_root",
    "is_positive_number",
    "factorial",
    "normalize",
    "scale_linear",
    "add",
    "subtract",
    "multiply",
    "divide",
    "fibonacci",
    "arithmetic_sequence",
    "geometric_sequence",
    "mean",
    "median",
    "mode",
    "variance",
    "SummaryStatistics",
    "summarize",
    "NumberSeries",
    "main",
]
