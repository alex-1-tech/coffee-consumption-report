# Architecture

## Structure

```
src/coffee_report/
├── cli.py           # Argument parsing, error handling
├── app.py           # Main orchestrator
├── domain/          # Models and exceptions
├── infrastructure/  # CSV loading, table formatting
└── reports/         # Report strategies
```

## Flow

```
CLI → App → Loader → Records → Report → Formatter → Output
```

## Patterns

- **Strategy**: Reports are interchangeable via `BaseReport`
- **Dependency Injection**: Components passed to `CoffeeReportApp`
- **Single Responsibility**: Each module has one job

## Adding Reports

1. Create class inheriting `BaseReport`
2. Implement `build()` method
3. Add to `ReportRegistry`
