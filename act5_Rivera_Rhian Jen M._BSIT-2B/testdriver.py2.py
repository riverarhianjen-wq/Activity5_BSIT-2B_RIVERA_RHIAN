# Test driver for all stack and queue implementations.

from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def test_array_stack():
    stack = ArrayStack(2)

    assert stack.is_empty()
    stack.push(10)
    stack.push(20)

    assert stack.is_full()
    assert stack.peek() == 20
    assert stack.pop() == 20
    assert stack.pop() == 10

    try:
        stack.pop()
    except IndexError:
        print("ArrayStack underflow test passed.")

    stack.push(1)
    stack.push(2)

    try:
        stack.push(3)
    except OverflowError:
        print("ArrayStack overflow test passed.")


def test_linked_stack():
    stack = LinkedStack()

    stack.push("A")
    stack.push("B")

    assert stack.peek() == "B"
    assert stack.pop() == "B"
    assert stack.pop() == "A"
    assert stack.is_empty()

    try:
        stack.pop()
    except IndexError:
        print("LinkedStack underflow test passed.")


def test_array_queue():
    queue = ArrayQueue(3)

    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")

    assert queue.is_full()
    assert queue.dequeue() == "A"

    # Test circular wrap-around.
    queue.enqueue("D")

    assert queue.peek_front() == "B"
    assert queue.dequeue() == "B"
    assert queue.dequeue() == "C"
    assert queue.dequeue() == "D"
    assert queue.is_empty()

    print("ArrayQueue wrap-around test passed.")

    try:
        queue.dequeue()
    except IndexError:
        print("ArrayQueue underflow test passed.")

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    try:
        queue.enqueue(4)
    except OverflowError:
        print("ArrayQueue overflow test passed.")


def test_linked_queue():
    queue = LinkedQueue()

    queue.enqueue(100)
    queue.enqueue(200)

    assert queue.peek_front() == 100
    assert queue.dequeue() == 100
    assert queue.dequeue() == 200
    assert queue.is_empty()

    try:
        queue.dequeue()
    except IndexError:
        print("LinkedQueue underflow test passed.")


if _name_ == "_main_":
    test_array_stack()
    test_linked_stack()
    test_array_queue()
    test_linked_queue()

    print("\nAll stack and queue tests passed!")