"""Command-line interface for coffee consumption report generation."""

import argparse
import logging
import sys
from typing import NoReturn


def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate reports from coffee consumption data",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --files data1.csv data2.csv --report median-coffee
  %(prog)s --files *.csv --report median-coffee
        """,
    )

    parser.add_argument("--files", nargs="+", required=True, help="CSV files to process")

    parser.add_argument(
        "--report",
        required=True,
        choices=["median-coffee"],
        help="Report type to generate (currently only median-coffee is supported)",
    )

    return parser.parse_args(args)


def main() -> NoReturn:
    """Execute the main CLI entry point."""
    args = parse_args()

    _generate_report_placeholder(args)

    sys.exit(0)


def _generate_report_placeholder(args: argparse.Namespace) -> None:
    """Generate placeholder report output."""
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info("Processing files: %s", ", ".join(args.files))
    logger.info("Generating report: %s", args.report)
    logger.info("\n[Placeholder] Report output will appear here")


if __name__ == "__main__":
    main()
