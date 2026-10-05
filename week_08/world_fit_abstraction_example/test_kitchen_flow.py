"""Written in teaching order. Each step was red before its code existed."""
import pytest

from kitchen_flow import EmptyError, TicketLine, UndoStack, trace_same_input


# Step 1: a new ticket line is empty.
def test_new_ticket_line_is_empty():
    line = TicketLine()
    assert line.is_empty()
    assert line.size() == 0


# Step 2: first in, first out.
def test_ticket_line_serves_oldest_ticket_first():
    line = TicketLine()
    line.enqueue("soup")
    line.enqueue("burger")
    assert line.dequeue() == "soup"
    assert line.dequeue() == "burger"


# Step 3: peek looks without taking.
def test_peek_shows_next_ticket_without_removing_it():
    line = TicketLine()
    line.enqueue("soup")
    assert line.peek() == "soup"
    assert line.size() == 1


# Step 4: the real process has no answer for an empty line, so it says so.
def test_dequeue_and_peek_on_empty_line_raise():
    line = TicketLine()
    with pytest.raises(EmptyError):
        line.dequeue()
    with pytest.raises(EmptyError):
        line.peek()


# Step 5: the undo stack is the opposite: last in, first out.
def test_undo_stack_undoes_newest_action_first():
    undo = UndoStack()
    undo.push("add salt")
    undo.push("add pepper")
    assert undo.peek() == "add pepper"
    assert undo.pop() == "add pepper"
    assert undo.pop() == "add salt"
    assert undo.is_empty()


def test_pop_and_peek_on_empty_stack_raise():
    undo = UndoStack()
    with pytest.raises(EmptyError):
        undo.pop()
    with pytest.raises(EmptyError):
        undo.peek()


# Step 6: same input, opposite order. This is the whole lesson.
def test_same_input_comes_out_in_opposite_orders():
    fifo, lifo = trace_same_input(["soup", "burger", "pizza"])
    assert fifo == ["soup", "burger", "pizza"]
    assert lifo == ["pizza", "burger", "soup"]


# Step 7: the abstraction does not leak its list.
def test_clients_cannot_reach_into_the_middle():
    line = TicketLine()
    line.enqueue("soup")
    assert not hasattr(line, "insert")
    with pytest.raises(TypeError):
        line[0]
