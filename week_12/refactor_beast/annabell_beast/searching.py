"""Linear and binary search algorithms with probe counting."""


def linear_search(items, target, counts):
    """Return the target index, or -1; count each equality check as a probe."""
    for index, item in enumerate(items):
        counts.probes += 1
        if item == target:
            return index
    return -1


def binary_search(items, target, counts):
    """Search sorted items; equality and less-than checks each count as probes."""
    low = 0
    high = len(items) - 1
    while low <= high:
        middle = (low + high) // 2
        counts.probes += 1
        if items[middle] == target:
            return middle
        counts.probes += 1
        if items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1
