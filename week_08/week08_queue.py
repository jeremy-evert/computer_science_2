"""CS2 Week 8: World-Fit Data Abstraction.

WORLD FLOW
Supply requests arrive at a settlement. Workers fulfill them in arrival
order. The oldest waiting request must be handled first.

CHOICE
A queue fits this rule: first in, first out (FIFO).

CLIENT OPERATIONS
add_request(item)     Add a request to the back of the line.
fulfill_next()        Remove and return the oldest request.
waiting_requests()    See a snapshot without changing the line.
is_empty()            Ask whether any requests remain.

WHY THE ABSTRACTION MATTERS
A Python list or deque is a storage choice. "Queue" describes the behavior
the world requires. Clients should ask to add or fulfill a request, not
decide for themselves which end of a container to remove from.

WORLD BIBLE
Changed: Supply requests now have a FIFO queue and defined empty behavior.
Evidence: The trace shows the order; automated tests check FIFO, empty
          behavior, and that a snapshot cannot change the real queue.
Remaining debt: Requests are still strings. A larger world might need
                quantities, requesters, or other request details.
"""

import unittest
from collections import deque


class NoRequestsWaitingError(Exception):
    """A request cannot be fulfilled because the queue is empty."""


class SupplyRequests:
    def __init__(self):
        self._waiting = deque()

    def add_request(self, item):
        self._waiting.append(item)

    def fulfill_next(self):
        if self.is_empty():
            raise NoRequestsWaitingError("No supply requests are waiting.")

        return self._waiting.popleft()

    def waiting_requests(self):
        return list(self._waiting)

    def is_empty(self):
        return not self._waiting


class TestSupplyRequests(unittest.TestCase):
    def test_oldest_request_is_fulfilled_first(self):
        requests = SupplyRequests()
        requests.add_request("flour")
        requests.add_request("bandages")
        requests.add_request("water")

        self.assertEqual(requests.fulfill_next(), "flour")
        self.assertEqual(requests.fulfill_next(), "bandages")
        self.assertEqual(requests.fulfill_next(), "water")
        self.assertTrue(requests.is_empty())

    def test_empty_queue_reports_a_meaningful_error(self):
        requests = SupplyRequests()

        with self.assertRaisesRegex(
            NoRequestsWaitingError,
            "No supply requests are waiting.",
        ):
            requests.fulfill_next()

    def test_snapshot_cannot_change_the_real_queue(self):
        requests = SupplyRequests()
        requests.add_request("flour")

        snapshot = requests.waiting_requests()
        snapshot.clear()

        self.assertEqual(requests.fulfill_next(), "flour")


def show_world_flow():
    requests = SupplyRequests()

    print("WORLD RULE: Fulfill the oldest supply request first.")
    print("Start:", requests.waiting_requests())

    for item in ("flour", "bandages", "water"):
        requests.add_request(item)
        print(f"{item} arrives:", requests.waiting_requests())

    while not requests.is_empty():
        fulfilled = requests.fulfill_next()
        print(f"Fulfilled {fulfilled}; still waiting:", requests.waiting_requests())

    try:
        requests.fulfill_next()
    except NoRequestsWaitingError as error:
        print("Empty-queue response:", error)


def show_learning_contrasts():
    print("\nGOOD AND BAD WAYS TO THINK ABOUT THIS")

    print("\n1. Choosing the abstraction")
    print("BAD:  'I used a list, so this must be a queue.'")
    print("GOOD: 'My world serves the oldest request first, so I need FIFO.'")

    print("\n2. Choosing client operations")
    print("BAD:  'Other code can remove whichever stored item it wants.'")
    print("GOOD: 'Other code calls add_request() or fulfill_next().'")

    print("\n3. Choosing evidence")
    print("BAD:  'The program printed a list, so FIFO must work.'")
    print("GOOD: 'A test checks that flour leaves before bandages and water.'")

    print("\n4. Handling an empty line")
    print("BAD:  'Hope nobody calls fulfill_next() when it is empty.'")
    print("GOOD: 'Define the error, handle it, and test it.'")


if __name__ == "__main__":
    show_world_flow()
    show_learning_contrasts()

    print("\nAUTOMATED TESTS")
    unittest.main(verbosity=2)