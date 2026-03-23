"""Table formatting for report output."""
from __future__ import annotations

from tabulate import tabulate


class TableFormatter:
    """Formats report data as tables."""

    def render(self, rows: list[tuple[str, int | float]], headers: list[str] | None = None) -> str:
        """Render rows as formatted table."""
        if headers is None:
            headers = ["student", "value"]

        formatted_rows = []
        for student, value in rows:
            if isinstance(value, float) and value.is_integer():
                formatted_rows.append((student, int(value)))
            else:
                formatted_rows.append((student, value))

        return tabulate(formatted_rows, headers=headers, tablefmt="grid")
