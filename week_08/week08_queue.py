"""Week 8: A queue for supply requests.

World rule:
    Supply requests wait their turn. The oldest request is fulfilled first.

Client operations:
    add_request(item) puts a request at the back of the line.
    fulfill_next() takes the request at the front of the line.

Evidence:
    If flour is requested before bandages, flour must be fulfilled first.
"""

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


#requests = SupplyRequests()
#requests.add_request("flour")
#requests.add_request("bandages")

requests = SupplyRequests()
print("Start:", requests.waiting_requests())

requests.add_request("flour")
print("After flour arrives:", requests.waiting_requests())

requests.add_request("bandages")
print("After bandages arrive:", requests.waiting_requests())

fulfilled = requests.fulfill_next()
print("Fulfilled:", fulfilled)
print("Still waiting:", requests.waiting_requests())

assert fulfilled == "flour"
print("FIFO test passed.")

first_fulfilled = requests.fulfill_next()

assert first_fulfilled == "flour"
print(f"First fulfilled: {first_fulfilled}")
print("FIFO test passed.")