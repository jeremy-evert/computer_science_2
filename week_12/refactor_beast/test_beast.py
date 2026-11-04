from beast import SearchMetrics, SortMetrics, bs, lin


def test_linear_search_finds_seven_at_index_one():
    assert lin([4, 7, 9], 7) == 1


def test_linear_search_tracks_probes_without_global_state():
    metrics = SearchMetrics()
    index, metrics = lin([4, 7, 9], 7, metrics)
    assert index == 1
    assert metrics.probes == 2


def test_bubble_sort_tracks_comparisons_and_swaps_without_global_state():
    metrics = SortMetrics()
    sorted_values, metrics = bs([3, 1, 2], metrics)
    assert sorted_values == [1, 2, 3]
    assert metrics.comparisons == 3
    assert metrics.swaps == 2
