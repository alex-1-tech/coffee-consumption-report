"""Main application orchestrator for coffee consumption report generation."""
from __future__ import annotations

from coffee_report.domain.exceptions import DataFileNotFoundError
from coffee_report.infrastructure import CSVLoader, TableFormatter
from coffee_report.reports import ReportRegistry


class CoffeeReportApp:
    """Main application orchestrator."""

    def __init__(
        self, loader: CSVLoader = None, registry: ReportRegistry = None, formatter: TableFormatter = None
    ) -> None:
        """Initialize the application with optional components."""
        self._loader = loader or CSVLoader()
        self._registry = registry or ReportRegistry()
        self._formatter = formatter or TableFormatter()

    def run(self, files: list[str], report_name: str) -> str:
        """Run report generation and return formatted output."""
        try:
            records = self._loader.load(files)

            if not records:
                return "No records found in the provided files."

            report = self._registry.get(report_name)
            rows = report.build(records)

            headers = ["student", report_name.replace("-", "_")]
            return self._formatter.render(rows, headers)

        except FileNotFoundError as e:
            raise DataFileNotFoundError(str(e)) from e
