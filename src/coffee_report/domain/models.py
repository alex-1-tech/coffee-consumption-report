"""Student record domain model representing data from CSV files."""

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True, slots=True)
class StudentRecord:
    """Represents a single student record from CSV."""

    student: str
    date: date
    coffee_spent: int
    sleep_hours: float
    study_hours: float
    mood: str
    exam: str
