
from collections import deque


class Queue:
    def __init__(self):
        # Create an empty queue.
        self.items = deque()

    def enqueue(self, item):
        # Add an item to the rear of the queue.
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        # Remove and return the front item.
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None

        return self.items.popleft()

    def peek(self):
        # View the front item without removing it.
        if self.is_empty():
            print("Queue is empty. Nothing to peek.")
            return None

        return self.items[0]

    def is_empty(self):
        # Check whether the queue has no items.
        return len(self.items) == 0

    def size(self):
        # Return the number of items in the queue.
        return len(self.items)


# Test program
my_queue = Queue()

# Enqueue operations
my_queue.enqueue("Apple")
my_queue.enqueue("Banana")
my_queue.enqueue("Orange")

# Check the front item and queue size
print("Front item:", my_queue.peek())
print("Queue size:", my_queue.size())

# Dequeue operations
print("Dequeued:", my_queue.dequeue())
print("Dequeued:", my_queue.dequeue())

# Check the remaining queue
print("Front item:", my_queue.peek())
print("Queue size:", my_queue.size())

# Remove the remaining item
print("Dequeued:", my_queue.dequeue())

# Test empty queue handling
print("Is queue empty?", my_queue.is_empty())
print("Dequeue from empty queue:", my_queue.dequeue())