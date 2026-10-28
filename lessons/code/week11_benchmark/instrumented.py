"""Week 11 story micro-lab, part 2: count what the sorts actually DO.

Every algorithm has two versions that do the same work:
  * ``<name>_counted(data) -> (sorted_list, counters)``  counts each operation
  * ``<name>_plain(data)   -> sorted_list``               no counters, for honest timing
Counting slows a program down, so wall-clock time is ALWAYS measured on the
plain version. The operation counts do not depend on the machine at all.

Operation types (bubble sort):
  outer_iters   passes of the outer for loop
  inner_iters   trips through the inner for loop
  comparisons   items[i] > items[i+1] tests
  swaps         exchanges performed
  index_reads   list[...] reads  (2 per comparison, 2 per swap)
  index_writes  list[...] writes (2 per swap)
  flag_sets     'swapped = True' assignments (one per swap: a CONSTANT factor
                on the swap count, so it grows like n^2 too)
  bookkeeping   the lower-order stuff Big O says to ignore: copying the input,
                len(), building each range() and resetting 'swapped' (all O(n))
"""
from collections import Counter


def bubble_counted(data):
    c = Counter()
    items = list(data); c["bookkeeping"] += len(items)       # copy
    n = len(items); c["bookkeeping"] += 1                    # len()
    for end in range(n - 1, 0, -1):
        c["outer_iters"] += 1
        c["bookkeeping"] += 2                                # range() + swapped = False
        swapped = False
        for i in range(end):
            c["inner_iters"] += 1
            c["comparisons"] += 1; c["index_reads"] += 2
            if items[i] > items[i + 1]:
                c["swaps"] += 1; c["index_reads"] += 2; c["index_writes"] += 2
                c["flag_sets"] += 1                          # swapped = True
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True
    return items, c


def bubble_plain(data):
    items = list(data)
    n = len(items)
    for end in range(n - 1, 0, -1):
        for i in range(end):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
    return items


def bubble_early_counted(data):
    """Same as bubble, but stop after a pass with no swap."""
    c = Counter()
    items = list(data); c["bookkeeping"] += len(items)
    n = len(items); c["bookkeeping"] += 1
    for end in range(n - 1, 0, -1):
        c["outer_iters"] += 1
        c["bookkeeping"] += 2
        swapped = False
        for i in range(end):
            c["inner_iters"] += 1
            c["comparisons"] += 1; c["index_reads"] += 2
            if items[i] > items[i + 1]:
                c["swaps"] += 1; c["index_reads"] += 2; c["index_writes"] += 2
                c["flag_sets"] += 1
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True
        if not swapped:
            break
    return items, c


def bubble_early_plain(data):
    items = list(data)
    for end in range(len(items) - 1, 0, -1):
        swapped = False
        for i in range(end):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True
        if not swapped:
            break
    return items


def insertion_counted(data):
    c = Counter()
    items = list(data); c["bookkeeping"] += len(items)
    for i in range(1, len(items)):
        c["outer_iters"] += 1
        value, j = items[i], i - 1
        c["index_reads"] += 1
        while j >= 0:
            c["inner_iters"] += 1
            c["comparisons"] += 1; c["index_reads"] += 1
            if items[j] > value:
                items[j + 1] = items[j]
                c["swaps"] += 1                              # one shift (a move, not a full swap)
                c["index_reads"] += 1; c["index_writes"] += 1
                j -= 1
            else:
                break
        items[j + 1] = value; c["index_writes"] += 1
    return items, c


def insertion_plain(data):
    items = list(data)
    for i in range(1, len(items)):
        value, j = items[i], i - 1
        while j >= 0 and items[j] > value:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = value
    return items


def merge_counted(data):
    c = Counter()

    def sort(part):
        c["bookkeeping"] += 1                                # one call
        if len(part) <= 1:
            return list(part)
        mid = len(part) // 2
        c["bookkeeping"] += len(part)                        # two slices copy len(part) items
        left, right = sort(part[:mid]), sort(part[mid:])
        merged, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            c["inner_iters"] += 1; c["comparisons"] += 1; c["index_reads"] += 2
            if left[i] <= right[j]:
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
            c["swaps"] += 1                                  # one item moved into the output
        rest = len(left) - i + len(right) - j
        c["swaps"] += rest; c["index_reads"] += rest
        merged.extend(left[i:]); merged.extend(right[j:])
        return merged

    return sort(list(data)), c


def merge_plain(data):
    if len(data) <= 1:
        return list(data)
    mid = len(data) // 2
    left, right = merge_plain(data[:mid]), merge_plain(data[mid:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:]); merged.extend(right[j:])
    return merged


ALGORITHMS = {
    "bubble": (bubble_counted, bubble_plain),
    "bubble_early": (bubble_early_counted, bubble_early_plain),
    "insertion": (insertion_counted, insertion_plain),
    "merge": (merge_counted, merge_plain),
}
COUNTER_FIELDS = ["outer_iters", "inner_iters", "comparisons", "swaps",
                  "index_reads", "index_writes", "flag_sets", "bookkeeping"]
