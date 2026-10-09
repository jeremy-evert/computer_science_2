from starship_log import MissionQueue


def test_new_queue_is_empty():
    queue = MissionQueue()
    assert queue.is_empty()
