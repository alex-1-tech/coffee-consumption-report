"""Median coffee consumption report."""

from __future__ import annotations

from statistics import median
from typing import TYPE_CHECKING, Sequence

from coffee_report.reports import BaseReport

if TYPE_CHECKING:
    from coffee_report.domain.models import StudentRecord


class MedianCoffeeReport(BaseReport):
    """Report showing median coffee consumption per student.

    Calculates median coffee spent for each student and returns results
    sorted by median value descending, then by student name ascending.
    """

    name = "median-coffee"

    def build(self, records: Sequence[StudentRecord]) -> list[tuple[str, float]]:
        """Calculate median coffee spent per student."""
        student_coffee: dict[str, list[int]] = {}

        for record in records:
            if record.student not in student_coffee:
                student_coffee[record.student] = []
            student_coffee[record.student].append(record.coffee_spent)

        results = []
        for student, coffee_list in student_coffee.items():
            median_value = median(coffee_list)
            results.append((student, median_value))

        results.sort(key=lambda x: (-x[1], x[0]))

        return results
