"""Small data classes shared by the algorithms and experiments."""

from dataclasses import dataclass


@dataclass
class OperationCounts:
    """Counts gathered while one algorithm runs."""

    comparisons: int = 0
    swaps_or_shifts: int = 0
    probes: int = 0

    def reset(self):
        """Clear counts before reusing this object for another trial."""
        self.comparisons = 0
        self.swaps_or_shifts = 0
        self.probes = 0


@dataclass
class SortResult:
    """Average measurements for one input kind, algorithm, and size."""

    avg_comparisons: float
    avg_swaps_or_shifts: float
    avg_seconds: float


@dataclass
class SearchResult:
    """Average probes per lookup for one list size."""

    linear_avg_probes: float
    binary_avg_probes: float
