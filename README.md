# Coffee Consumption Report

CLI tool for generating reports from student coffee consumption data.

## Installation

```bash
git clone [<repository-url>](https://github.com/alex-1-tech/coffee-consumption-report/edit/main/README.md)
cd coffee-consumption-report
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .
```

## Usage

```bash
coffee-report --files data1.csv data2.csv --report median-coffee
coffee-report --files *.csv --report median-coffee --verbose
coffee-report --help
```

## Demo

<img width="756" height="578" alt="image" src="https://github.com/user-attachments/assets/fe059cd0-bf1d-4c5d-bb46-a353d4f3e1a3" />


## Documentation

- [Git Workflow](docs/git-workflow.md) - Commit conventions
- [Development](docs/development.md) - Adding new reports
- [Architecture](docs/architecture.md) - Project structure

## Testing

```bash
pytest
pytest --cov=coffee_report
```
<img width="927" height="226" alt="image" src="https://github.com/user-attachments/assets/20dcdf58-4f5b-4043-b790-ce2fe29d7824" />

## License

MIT
