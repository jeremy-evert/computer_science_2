"""Week 8: Supply requests form a first-in, first-out queue."""

from collections import deque


class SupplyRequests:
    def __init__(self):
        self._waiting = deque()

    def add_request(self, item):
        self._waiting.append(item)

    def fulfill_next(self):
        return self._waiting.popleft()

    def waiting_requests(self):
        return list(self._waiting)


requests = SupplyRequests()
print("Start:", requests.waiting_requests())

requests.add_request("flour")
print("After flour arrives:", requests.waiting_requests())

requests.add_request("bandages")
print("After bandages arrive:", requests.waiting_requests())

first_fulfilled = requests.fulfill_next()
print("First fulfilled:", first_fulfilled)
print("Still waiting:", requests.waiting_requests())
assert first_fulfilled == "flour"

second_fulfilled = requests.fulfill_next()
print("Second fulfilled:", second_fulfilled)
print("Still waiting:", requests.waiting_requests())
assert second_fulfilled == "bandages"

print("FIFO test passed: flour came out before bandages.")