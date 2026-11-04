"""Bubble sort variants."""


def bubble_sort(items, counts):
    """Sort in place with bubble sort, counting comparisons and swaps."""
    size = len(items)
    for pass_index in range(size):
        for index in range(size - pass_index - 1):
            counts.comparisons += 1
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
                counts.swaps_or_shifts += 1
    return items


def bubble_sort_early_exit(items, counts):
    """Bubble sort that stops after a pass makes no swaps."""
    size = len(items)
    for pass_index in range(size):
        swapped = False
        for index in range(size - pass_index - 1):
            counts.comparisons += 1
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
                counts.swaps_or_shifts += 1
                swapped = True
        if not swapped:
            break
    return items
