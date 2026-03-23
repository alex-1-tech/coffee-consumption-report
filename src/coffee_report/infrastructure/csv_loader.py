"""CSV file loader for student records."""

from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path

from coffee_report.domain.models import StudentRecord


class CSVLoader:
    """Loads and parses CSV files into StudentRecord objects."""

    def load(self, files: list[str | Path]) -> list[StudentRecord]:
        """Load records from multiple CSV files."""
        all_records = []

        for file_path in files:
            path = Path(file_path)
            if not path.exists():
                msg = f"File not found: {file_path}"
                raise FileNotFoundError(msg)

            records = self._load_single_file(path)
            all_records.extend(records)

        return all_records

    def _load_single_file(self, file_path: Path) -> list[StudentRecord]:
        """Load records from a single CSV file."""
        records = []

        with file_path.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = StudentRecord(
                    student=row["student"].strip(),
                    date=datetime.fromisoformat(row["date"]).date(),
                    coffee_spent=int(row["coffee_spent"]),
                    sleep_hours=float(row["sleep_hours"]),
                    study_hours=float(row["study_hours"]),
                    mood=row["mood"].strip(),
                    exam=row["exam"].strip(),
                )
                records.append(record)

        return records
