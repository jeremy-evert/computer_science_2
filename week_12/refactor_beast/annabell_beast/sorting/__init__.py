"""Sorting algorithms used by the experiment."""

from .bubble import bubble_sort, bubble_sort_early_exit
from .insertion import insertion_sort
from .python_sort import python_sort_counted
from .selection import selection_sort

# Keep this order stable because it determines CSV, report, and plot order.
SORT_ALGORITHMS = {
    "bubble": bubble_sort,
    "bubble_early_exit": bubble_sort_early_exit,
    "insertion": insertion_sort,
    "selection": selection_sort,
    "python": python_sort_counted,
}

__all__ = [
    "SORT_ALGORITHMS",
    "bubble_sort",
    "bubble_sort_early_exit",
    "insertion_sort",
    "python_sort_counted",
    "selection_sort",
]
