"""Base report interface for all report strategies."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Sequence


class BaseReport(ABC):
    """Base class for all reports.

    All report implementations should inherit from this class and implement
    the build method with specific report logic.
    """

    name: str

    @abstractmethod
    def build(self, records: Sequence) -> list[tuple[str, int | float]]:
        """Build report from records."""
