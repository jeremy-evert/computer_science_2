"""Selection sort."""


def selection_sort(items, counts):
    """Sort in place by moving the smallest remaining item forward."""
    size = len(items)
    for index in range(size):
        min_index = index
        for candidate_index in range(index + 1, size):
            counts.comparisons += 1
            if items[candidate_index] < items[min_index]:
                min_index = candidate_index
        if min_index != index:
            items[index], items[min_index] = items[min_index], items[index]
            counts.swaps_or_shifts += 1
    return items
