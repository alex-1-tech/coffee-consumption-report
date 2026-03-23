"""Custom exceptions for the domain layer.

This module defines exception classes used throughout the domain layer
to handle error conditions in a consistent and meaningful way.
"""

class ReportNotFoundError(Exception):
    """Raised when requested report doesn't exist."""


class DataFileNotFoundError(Exception):
    """Raised when data file doesn't exist."""
