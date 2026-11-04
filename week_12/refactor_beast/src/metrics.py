"""Mutable counters shared by the experiment's algorithms."""

from dataclasses import dataclass


@dataclass
class OperationCounts:
    """Count algorithm operations when a caller supplies this object."""

    comparisons: int = 0
    swaps: int = 0
    probes: int = 0
