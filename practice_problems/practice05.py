from collections import deque

hello = "hello"
paren_input = "(([]))"

stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack:", stack)

top = stack.pop()
print("Popped:", top)
print("Stack after pop:", stack)

peek = stack[-1] if stack else None
print("Peek:", peek)

queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

front = queue.popleft()
print("Dequeue:", front)
print("Queue after dequeue:", queue)

def check_balanced_parens(lst):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["} 

    for char in lst:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack

def reverse_str(lst):
    stack = []
    for char in lst:
        stack.append(char)
    reversed_chars = []
    while stack:
        reversed_chars.append(stack.pop())
    return "".join(reversed_chars)

class QueueUsingTwoStacks:
    def __init__(self):
        self.in_stack = []  # Used for enqueue operations
        self.out_stack = [] # Used for dequeue operations

    def enqueue(self, item):
        """Adds an item to the back of the queue."""
        self.in_stack.append(item)

    def dequeue(self):
        """Removes and returns the item from the front of the queue."""
        if not self.out_stack:
            if not self.in_stack:
                raise IndexError("Dequeue from empty queue")
            # Transfer elements from in_stack to out_stack to reverse order
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self):
        """Returns the item at the front of the queue without removing it."""
        if not self.out_stack:
            if not self.in_stack:
                raise IndexError("Peek from empty queue")
            # Transfer elements from in_stack to out_stack to reverse order
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def is_empty(self):
        """Checks if the queue is empty."""
        return not self.in_stack and not self.out_stack

    def size(self):
        """Returns the number of items in the queue."""
        return len(self.in_stack) + len(self.out_stack)

# Testing the implementation
import unittest

class TestQueueUsingTwoStacks(unittest.TestCase):
    def test_enqueue_and_dequeue(self):
        queue = QueueUsingTwoStacks()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        queue.enqueue(4)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)
        self.assertTrue(queue.is_empty())

    def test_dequeue_from_empty_queue(self):
        queue = QueueUsingTwoStacks()
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_peek(self):
        queue = QueueUsingTwoStacks()
        queue.enqueue(10)
        queue.enqueue(20)
        self.assertEqual(queue.peek(), 10)
        queue.dequeue()
        self.assertEqual(queue.peek(), 20)
        self.assertFalse(queue.is_empty())

    def test_is_empty(self):
        queue = QueueUsingTwoStacks()
        self.assertTrue(queue.is_empty())
        queue.enqueue(5)
        self.assertFalse(queue.is_empty())
        queue.dequeue()
        self.assertTrue(queue.is_empty())

    def test_size(self):
        queue = QueueUsingTwoStacks()
        self.assertEqual(queue.size(), 0)
        queue.enqueue('a')
        self.assertEqual(queue.size(), 1)
        queue.enqueue('b')
        self.assertEqual(queue.size(), 2)
        queue.dequeue()
        self.assertEqual(queue.size(), 1)
        queue.dequeue()
        self.assertEqual(queue.size(), 0)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


print("Original parentheses:", paren_input)
balance_parens = check_balanced_parens(paren_input)
print("Balanced Parentheses?:", balance_parens)
reversed_string = reverse_str(hello)
print("Original String:", hello)
print("Reversed string:", reversed_string)