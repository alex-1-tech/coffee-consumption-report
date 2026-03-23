"""Report generation module with strategy pattern."""

from coffee_report.reports.base import BaseReport
from coffee_report.reports.median_coffee import MedianCoffeeReport
from coffee_report.reports.registry import ReportRegistry, default_registry

__all__ = ["BaseReport", "MedianCoffeeReport", "ReportRegistry", "default_registry"]
