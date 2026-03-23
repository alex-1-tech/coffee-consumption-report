"""Command-line interface for coffee consumption report generation."""

from __future__ import annotations

import argparse
import logging
import sys
from typing import NoReturn

from coffee_report.app import CoffeeReportApp
from coffee_report.domain.exceptions import DataFileNotFoundError, ReportNotFoundError


def setup_logging(*, verbose: bool = False) -> None:
    """Configure logging for the CLI application."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate reports from coffee consumption data",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  coffee-report --files data1.csv data2.csv --report median-coffee
  coffee-report --files *.csv --report median-coffee
        """,
    )

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="CSV files to process",
    )

    parser.add_argument(
        "--report",
        required=True,
        help="Report type to generate (currently only median-coffee is supported)",
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose output",
    )

    return parser.parse_args(args)


def main() -> NoReturn:
    """Execute the main CLI entry point."""
    args = parse_args()

    setup_logging(verbose=args.verbose)
    logger = logging.getLogger(__name__)

    try:
        logger.debug("Starting coffee consumption report generation")
        logger.debug("Files to process: %s", args.files)
        logger.debug("Report type: %s", args.report)

        app = CoffeeReportApp()
        output = app.run(files=args.files, report_name=args.report)

        logger.debug("Report generation completed successfully")
        print(output) # noqa: T201

    except ReportNotFoundError as e:
        error_msg = f"Report not found: {e}"
        logger.exception(error_msg)
        sys.exit(1)
    except DataFileNotFoundError as e:
        error_msg = f"Data file not found: {e}"
        logger.exception(error_msg)
        sys.exit(1)
    except Exception as e:
        error_msg = f"Unexpected error occurred: {e}"
        logger.exception(error_msg)
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
