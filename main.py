"""Entry point re-exporting helpers for legacy compatibility."""
from __future__ import annotations

from typing import TYPE_CHECKING

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
