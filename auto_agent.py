"""Core helpers for the Autonomous QA agent."""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict


def get_square_root(number: float) -> float:
    """Return the square root of ``number``."""
    return math.sqrt(number)


def is_positive_number(number: float) -> bool:
    """Return True when ``number`` is strictly greater than zero."""
    return number > 0


@dataclass
class AutoAgent:
    """Lightweight stub agent used in generated tests."""

    name: str = "AutoAgent"
    state: str = "idle"
    context: Dict[str, Any] = field(default_factory=dict)

    def activate(self) -> None:
        self.state = "active"

    def reset(self) -> None:
        self.state = "idle"
        self.context.clear()

    def update_context(self, key: str, value: Any) -> None:
        self.context[key] = value
