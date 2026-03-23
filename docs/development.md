# Development Guide

## Adding a New Report

1. Create file in `src/coffee_report/reports/`

```python
from statistics import mean
from typing import Sequence
from coffee_report.reports.base import BaseReport


class AverageStudyHoursReport(BaseReport):
    name = "average-study-hours"

    def build(self, records: Sequence) -> list[tuple[str, float]]:
        student_hours = {}

        for r in records:
            if r.student not in student_hours:
                student_hours[r.student] = []
            student_hours[r.student].append(r.study_hours)

        results = [(s, mean(h)) for s, h in student_hours.items()]
        results.sort(key=lambda x: (-x[1], x[0]))
        return results
```

2. Register in `registry.py`

```python
from coffee_report.reports.average_study_hours import AverageStudyHoursReport

def default_registry():
    return {
        MedianCoffeeReport.name: MedianCoffeeReport(),
        AverageStudyHoursReport.name: AverageStudyHoursReport(),
    }
```

3. Add tests in `tests/`

## Code Style

```bash
ruff check . --fix
```

Use type hints and docstrings for all public functions.

