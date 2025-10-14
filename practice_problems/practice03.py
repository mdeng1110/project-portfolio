from collections import deque

class PrintJob:
    """Represents a single print job with a name."""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Print Job: {self.name}"

hello = "hello"
paren_input = "(([]))"

def reverse_str(lst):
    stack = []

    for char in lst:
        stack.append(char)

    reversed_chars = []
    while stack:
        reversed_chars.append(stack.pop())

    return "".join(reversed_chars)

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

def simulate_print_queue():
    """Simulates adding and processing print jobs in a queue."""
    print_queue = deque()

    # Add 5 print jobs to the queue
    print("Adding 5 print jobs to the queue:")
    for i in range(1, 6):
        job_name = f"Document_{i}.pdf"
        job = PrintJob(job_name)
        print_queue.append(job)
        print(f"  Added: {job}")

    print("\nDequeuing print jobs one by one:")
    # Dequeue print jobs until the queue is empty
    while print_queue:
        current_job = print_queue.popleft()
        print(f"  Printing: {current_job}")

    print("\nPrint queue is now empty.")

if __name__ == "__main__":
    simulate_print_queue()


reversed_string = reverse_str(hello)
print("Original String:", hello)
print("Reversed string:", reversed_string)
print("Original parentheses:", paren_input)
balance_parens = check_balanced_parens(paren_input)
print("Balanced Parentheses?:", balance_parens)
print("Queue Stimulation:", simulate_print_queue)