"""Kitchen flow: a ticket line (queue, FIFO) and an undo stack (LIFO).

Each class exposes only the operations the kitchen's real process allows.
The Python list inside is a private detail; clients never touch it.
"""


class EmptyError(Exception):
    """Raised when you take or look at something that is not there."""


class TicketLine:
    """Order tickets wait here. The oldest ticket is cooked first (FIFO)."""

    def __init__(self):
        self._tickets = []

    def enqueue(self, ticket):
        self._tickets.append(ticket)

    def dequeue(self):
        if not self._tickets:
            raise EmptyError("no tickets waiting")
        return self._tickets.pop(0)

    def peek(self):
        if not self._tickets:
            raise EmptyError("no tickets waiting")
        return self._tickets[0]

    def is_empty(self):
        return not self._tickets

    def size(self):
        return len(self._tickets)


class UndoStack:
    """Cook's actions pile up here. The newest action is undone first (LIFO)."""

    def __init__(self):
        self._actions = []

    def push(self, action):
        self._actions.append(action)

    def pop(self):
        if not self._actions:
            raise EmptyError("nothing to undo")
        return self._actions.pop()

    def peek(self):
        if not self._actions:
            raise EmptyError("nothing to undo")
        return self._actions[-1]

    def is_empty(self):
        return not self._actions

    def size(self):
        return len(self._actions)


def trace_same_input(items):
    """Feed the same items to both structures; return the order each gives back."""
    line, stack = TicketLine(), UndoStack()
    for item in items:
        line.enqueue(item)
        stack.push(item)
    fifo_order, lifo_order = [], []
    while not line.is_empty():
        fifo_order.append(line.dequeue())
    while not stack.is_empty():
        lifo_order.append(stack.pop())
    return fifo_order, lifo_order


if __name__ == "__main__":
    fifo, lifo = trace_same_input(["soup", "burger", "pizza"])
    print("in:   soup, burger, pizza")
    print("FIFO out:", ", ".join(fifo))
    print("LIFO out:", ", ".join(lifo))
