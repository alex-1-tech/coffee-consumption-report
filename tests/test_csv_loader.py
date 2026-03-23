"""Unit tests for CSV loader."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest

from coffee_report.domain.models import StudentRecord
from coffee_report.infrastructure.csv_loader import CSVLoader


class TestCSVLoader:
    """Test CSV loading functionality."""

    EXPECTED_RECORDS_COUNT = 4
    EXPECTED_COFFEE_SPENT = 3
    EXPECTED_SLEEP_HOURS = 7.5
    EXPECTED_STUDY_HOURS = 4

    def test_load_single_file(self, temp_csv_file: Path) -> None:
        """Test loading records from a single CSV file."""
        loader = CSVLoader()
        records = loader.load([temp_csv_file])

        assert len(records) == self.EXPECTED_RECORDS_COUNT
        assert all(isinstance(r, StudentRecord) for r in records)

        assert records[0].student == "Иван Кузнецов"
        assert records[0].date == date(2024, 1, 15)
        assert records[0].coffee_spent == self.EXPECTED_COFFEE_SPENT
        assert records[0].sleep_hours == self.EXPECTED_SLEEP_HOURS
        assert records[0].study_hours == self.EXPECTED_STUDY_HOURS
        assert records[0].mood == "good"
        assert records[0].exam == "Math"

    def test_load_multiple_files(self, temp_csv_files: list[Path]) -> None:
        """Test loading records from multiple CSV files."""
        loader = CSVLoader()
        records = loader.load(temp_csv_files)

        assert len(records) == self.EXPECTED_RECORDS_COUNT

        students = {r.student for r in records}
        assert students == {"Иван Кузнецов", "Алексей Смирнов"}

    def test_file_not_found(self) -> None:
        """Test error when file doesn't exist."""
        loader = CSVLoader()
        non_existent_file = Path("/nonexistent/file.csv")

        with pytest.raises(FileNotFoundError, match="File not found"):
            loader.load([non_existent_file])

    def test_empty_file_list(self) -> None:
        """Test loading with empty file list."""
        loader = CSVLoader()
        records = loader.load([])

        assert records == []

    def test_csv_with_extra_whitespace(self, temp_csv_file: Path) -> None:
        """Test that whitespace is properly stripped from fields."""
        loader = CSVLoader()
        records = loader.load([temp_csv_file])

        assert records[0].student == "Иван Кузнецов"
        assert records[0].mood == "good"
        assert records[0].exam == "Math"
