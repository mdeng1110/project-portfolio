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

def sliding_window_max(nums, k):

# Sliding Window Maximum (Optional)

# Given an array of numbers and a window size k, print the maximum in each sliding window.
# Hint: Use a deque to keep track of potential maxima efficiently.

    dq = deque()
    result =[]
    for i in range(len(nums)):
        if dq and dq[0] == i - k:
            dq.popleft()

        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)
        if i >= k -1:
            result.append(nums[dq[0]])

    return result

def isValid(str):
    close_to_open = {
        ")":"()",
        "}":"{",
        "]":"[]"
    }
    stack = []
    for bracket in str:
        if bracket in close_to_open:
            if not stack:
                return False
            top = stack.pop()
            if close_to_open[bracket] != top:
                return False
        else:
            stack.append(bracket)
    if stack:
        return False
    else:
        return True

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
#Expected output: {'apple': 3, 'banana': 2, 'orange': 1}
def frequency_counter(words):
    counter = {}
    for word in words:
        if word not in counter:
            counter[word] = 1
        else:
            counter[word] += 1
    return counter

def frequency_counter2(words):
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    return counter

def remove_duplicates(nums):
    result = []
    for num in nums:
        if num not in result:
            result.append(num)
        else:
            continue
    return result

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


print("Original parentheses:", paren_input)
balance_parens = check_balanced_parens(paren_input)
print("Balanced Parentheses?:", balance_parens)
reversed_string = reverse_str(hello)
print("Original String:", hello)
print("Reversed string:", reversed_string)

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
nums = [1, 2, 2, 3, 4, 4, 5]
output = sliding_window_max(arr, k)
print("Result of Sliding Window Maximum:", output) 
# Expected output: [3, 3, 5, 5, 6, 7]
print("Original Parentheses:", paren_input)
print("Result of isValid method:", isValid(paren_input))
print("Original words:", words)
print("Dictionary of words:", frequency_counter(words))
print("Another Dictionary of words using the get method:", frequency_counter2(words))
print("Original list of numbers:", nums)
print("Removed Duplications in numbers list:", remove_duplicates(nums))