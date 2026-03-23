"""Unit tests for the CLI module."""

import pytest

from coffee_report.cli import parse_args


def test_parse_args_valid() -> None:
    """Test parsing valid arguments."""
    args = parse_args(["--files", "file1.csv", "file2.csv", "--report", "median-coffee"])

    expected_files = ["file1.csv", "file2.csv"]
    expected_report = "median-coffee"

    assert args.files == expected_files
    assert args.report == expected_report


def test_parse_args_missing_files() -> None:
    """Test error when files are missing."""
    with pytest.raises(SystemExit):
        parse_args(["--report", "median-coffee"])


def test_parse_args_missing_report() -> None:
    """Test error when report is missing."""
    with pytest.raises(SystemExit):
        parse_args(["--files", "file.csv"])


def test_parse_args_invalid_report() -> None:
    """Test error with invalid report type."""
    with pytest.raises(SystemExit):
        parse_args(["--files", "file.csv", "--report", "invalid-report"])


def test_help_output() -> None:
    """Test that help message is displayed."""
    with pytest.raises(SystemExit) as exc_info:
        parse_args(["--help"])

    assert exc_info.value.code == 0
