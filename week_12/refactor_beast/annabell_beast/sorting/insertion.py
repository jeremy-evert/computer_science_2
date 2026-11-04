"""Insertion sort."""


def insertion_sort(items, counts):
    """Sort in place, counting comparisons and rightward shifts."""
    for index in range(1, len(items)):
        key = items[index]
        previous_index = index - 1
        while previous_index >= 0:
            counts.comparisons += 1
            if items[previous_index] > key:
                items[previous_index + 1] = items[previous_index]
                counts.swaps_or_shifts += 1
                previous_index -= 1
            else:
                break
        items[previous_index + 1] = key
    return items
