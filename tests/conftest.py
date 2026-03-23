"""Pytest fixtures for coffee consumption report tests."""

from __future__ import annotations

import csv
import tempfile
from pathlib import Path
from typing import Generator

import pytest


@pytest.fixture
def sample_data() -> list[dict[str, str]]:
    """Provide sample data for testing."""
    return [
        {
            "student": "Иван Кузнецов",
            "date": "2024-01-15",
            "coffee_spent": "3",
            "sleep_hours": "7.5",
            "study_hours": "4",
            "mood": "good",
            "exam": "Math",
        },
        {
            "student": "Алексей Смирнов",
            "date": "2024-01-15",
            "coffee_spent": "5",
            "sleep_hours": "6.0",
            "study_hours": "5",
            "mood": "normal",
            "exam": "Physics",
        },
        {
            "student": "Иван Кузнецов",
            "date": "2024-01-16",
            "coffee_spent": "2",
            "sleep_hours": "8.0",
            "study_hours": "3",
            "mood": "good",
            "exam": "Math",
        },
        {
            "student": "Алексей Смирнов",
            "date": "2024-01-16",
            "coffee_spent": "4",
            "sleep_hours": "6.5",
            "study_hours": "4",
            "mood": "normal",
            "exam": "Physics",
        },
    ]


@pytest.fixture
def temp_csv_file(sample_data: list[dict[str, str]]) -> Generator[Path, None, None]:
    """Create a temporary CSV file with sample data."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8") as f:
        fieldnames = ["student", "date", "coffee_spent", "sleep_hours", "study_hours", "mood", "exam"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sample_data)
        temp_path = Path(f.name)

    yield temp_path
    temp_path.unlink()


@pytest.fixture
def temp_csv_files(sample_data: list[dict[str, str]]) -> Generator[list[Path], None, None]:
    """Create two temporary CSV files with sample data."""
    files = []
    for _ in range(2):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["student", "date", "coffee_spent", "sleep_hours", "study_hours", "mood", "exam"],
            )
            writer.writeheader()
            writer.writerows(sample_data[:2])
            temp_path = Path(f.name)
            files.append(temp_path)

    yield files

    for f in files:
        f.unlink()
