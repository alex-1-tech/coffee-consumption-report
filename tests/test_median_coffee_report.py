"""Unit tests for median coffee report."""

from __future__ import annotations

from datetime import date
from statistics import median
from typing import TYPE_CHECKING

import pytest

from coffee_report.domain.models import StudentRecord
from coffee_report.reports.median_coffee import MedianCoffeeReport

if TYPE_CHECKING:
    from coffee_report.reports.base import BaseReport


class TestMedianCoffeeReport:
    """Test median coffee report functionality."""

    EXPECTED_MEDIAN = 3.5
    EXPECTED_INTEGER_MEDIAN = 4.0
    EXPECTED_SINGLE_VALUE = 5
    EXPECTED_UNIQUE_STUDENTS = 2

    @pytest.fixture
    def report(self) -> BaseReport:
        """Create report instance."""
        return MedianCoffeeReport()

    def test_single_student_odd_count(self, report: BaseReport) -> None:
        """Test median with single student and odd number of records."""
        records = [
            StudentRecord("Иван", date(2024, 1, 1), 3, 7.5, 4, "good", "Math"),
            StudentRecord("Иван", date(2024, 1, 2), 5, 7.5, 4, "good", "Math"),
            StudentRecord("Иван", date(2024, 1, 3), 2, 7.5, 4, "good", "Math"),
        ]

        result = report.build(records)

        assert len(result) == 1
        assert result[0][0] == "Иван"
        assert result[0][1] == median([3, 5, 2])

    def test_single_student_even_count(self, report: BaseReport) -> None:
        """Test median with single student and even number of records."""
        records = [
            StudentRecord("Иван", date(2024, 1, 1), 3, 7.5, 4, "good", "Math"),
            StudentRecord("Иван", date(2024, 1, 2), 5, 7.5, 4, "good", "Math"),
            StudentRecord("Иван", date(2024, 1, 3), 2, 7.5, 4, "good", "Math"),
            StudentRecord("Иван", date(2024, 1, 4), 8, 7.5, 4, "good", "Math"),
        ]

        result = report.build(records)

        assert len(result) == 1
        assert result[0][1] == median([3, 5, 2, 8])

    def test_multiple_students_sorting(self, report: BaseReport) -> None:
        """Test sorting by median descending."""
        records = [
            StudentRecord("Анна", date(2024, 1, 1), 10, 7.5, 4, "good", "Math"),
            StudentRecord("Анна", date(2024, 1, 2), 8, 7.5, 4, "good", "Math"),
            StudentRecord("Борис", date(2024, 1, 1), 5, 7.5, 4, "good", "Math"),
            StudentRecord("Борис", date(2024, 1, 2), 3, 7.5, 4, "good", "Math"),
            StudentRecord("Виктор", date(2024, 1, 1), 7, 7.5, 4, "good", "Math"),
            StudentRecord("Виктор", date(2024, 1, 2), 6, 7.5, 4, "good", "Math"),
        ]

        result = report.build(records)

        assert result[0][0] == "Анна"
        assert result[1][0] == "Виктор"
        assert result[2][0] == "Борис"

    def test_equal_medians_stable_sorting(self, report: BaseReport) -> None:
        """Test stable sorting when medians are equal (sort by name)."""
        records = [
            StudentRecord("Мария", date(2024, 1, 1), 5, 7.5, 4, "good", "Math"),
            StudentRecord("Мария", date(2024, 1, 2), 7, 7.5, 4, "good", "Math"),
            StudentRecord("Алексей", date(2024, 1, 1), 6, 7.5, 4, "good", "Math"),
            StudentRecord("Алексей", date(2024, 1, 2), 6, 7.5, 4, "good", "Math"),
            StudentRecord("Дмитрий", date(2024, 1, 1), 5, 7.5, 4, "good", "Math"),
            StudentRecord("Дмитрий", date(2024, 1, 2), 7, 7.5, 4, "good", "Math"),
        ]

        result = report.build(records)

        names = [r[0] for r in result]
        assert names == ["Алексей", "Дмитрий", "Мария"]

    def test_empty_records(self, report: BaseReport) -> None:
        """Test with empty records list."""
        result = report.build([])

        assert result == []

    def test_single_record(self, report: BaseReport) -> None:
        """Test with single record."""
        records = [
            StudentRecord("Иван", date(2024, 1, 1), 5, 7.5, 4, "good", "Math"),
        ]

        result = report.build(records)

        assert len(result) == 1
        assert result[0][0] == "Иван"
        assert result[0][1] == self.EXPECTED_SINGLE_VALUE

    def test_float_median_values(self, report: BaseReport) -> None:
        """Test that median returns float when needed."""
        records = [
            StudentRecord("Иван", date(2024, 1, 1), 3, 7.5, 4, "good", "Math"),
            StudentRecord("Иван", date(2024, 1, 2), 4, 7.5, 4, "good", "Math"),
        ]

        result = report.build(records)

        assert result[0][1] == self.EXPECTED_MEDIAN
        assert isinstance(result[0][1], float)

    def test_integer_median_values(self, report: BaseReport) -> None:
        """Test that median returns integer when appropriate."""
        records = [
            StudentRecord("Иван", date(2024, 1, 1), 3, 7.5, 4, "good", "Math"),
            StudentRecord("Иван", date(2024, 1, 2), 5, 7.5, 4, "good", "Math"),
        ]

        result = report.build(records)

        assert result[0][1] == self.EXPECTED_INTEGER_MEDIAN

    def test_preserves_all_records(self, report: BaseReport) -> None:
        """Test that all students appear even with single record."""
        records = [
            StudentRecord("Иван", date(2024, 1, 1), 3, 7.5, 4, "good", "Math"),
            StudentRecord("Петр", date(2024, 1, 1), 5, 7.5, 4, "good", "Math"),
            StudentRecord("Иван", date(2024, 1, 2), 4, 7.5, 4, "good", "Math"),
        ]

        result = report.build(records)

        assert len(result) == self.EXPECTED_UNIQUE_STUDENTS
        assert {r[0] for r in result} == {"Иван", "Петр"}
