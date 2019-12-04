"""
Implement a stack API using only a heap. A stack implements the following
methods:

push(item), which adds an element to the stack
pop(), which removes and returns the most recently added element (or
throws an error if there is nothing on the stack)

Recall that a heap has the following operations:

push(item), which adds a new key to the heap
pop(), which removes and returns the max value of the heap
"""

class Heap:
    """A heap implementation."""
    def __init__(self):
        """Initialise the heap."""
        self.heap = []

    def push(self, item):
        """Add item to heap."""
        self.heap.append(item)

    def pop(self):
        """Remove and return max item from heap."""
        maxitem = max(self.heap)
        self.heap.remove(maxitem)
        return maxitem

class Stack:
    """A stack implementation using heap."""
    def __init__(self):
        self.counter = 0
        self.heap = Heap()

    def push(self, item):
        """Add item to heap."""
        self.heap.push((self.counter, item))
        self.counter += 1

    def pop(self):
        """Remove and return most recent item."""
        most_recent = self.heap.pop() # Returns max item, ie item with higest counter
        return most_recent[1]


# TEST

s = Stack()
s.push("first")
s.push("second")
s.push("third")
s.push("fourth")
s.push("fifth")
s.push("sixth")

print(s.pop())
print(s.pop())
s.push(1)
print(s.pop())
print(s.pop())
s.push(2)
s.push(3)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
