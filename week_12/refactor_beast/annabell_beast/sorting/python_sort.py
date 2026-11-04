"""Python's built-in sort with comparison counting."""

from functools import cmp_to_key


def python_sort_counted(items, counts):
    """Sort in place, counting calls to the comparison function."""

    def counted_compare(left, right):
        counts.comparisons += 1
        return (left > right) - (left < right)

    items.sort(key=cmp_to_key(counted_compare))
    return items
