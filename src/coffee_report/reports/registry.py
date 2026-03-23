"""Report registry for managing report strategies."""

from __future__ import annotations

from typing import TYPE_CHECKING

from coffee_report.domain.exceptions import ReportNotFoundError
from coffee_report.reports.median_coffee import MedianCoffeeReport

if TYPE_CHECKING:
    from coffee_report.reports.base import BaseReport


def default_registry() -> dict[str, BaseReport]:
    """Return default report registry with all available reports."""
    return {
        MedianCoffeeReport.name: MedianCoffeeReport(),
    }


class ReportRegistry:
    """Registry for report strategies.

    Manages available report implementations and provides access to them
    by name. Supports custom registries and default registry.
    """

    def __init__(self, reports: dict[str, BaseReport] | None = None) -> None:
        """Initialize registry with optional custom reports."""
        self._reports = reports or default_registry()

    def get(self, name: str) -> BaseReport:
        """Get report by name."""
        if name not in self._reports:
            msg = f"Unknown report: {name}. Available: {list(self._reports.keys())}"
            raise ReportNotFoundError(msg)

        return self._reports[name]
