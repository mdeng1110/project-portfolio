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

def factorial(n):
    print("factorial called with n=", str(n))
    if n > 1:
        return n*factorial(n-1)
    print("Ending condition met.")
    return 1

def search(searchList, key):
    mid = int(len(searchList)/2)
    print("searching midpoint at", str(searchList[mid]))

    if mid == 0:
        print("Key not found!")
        return key
    
    elif key == searchList[mid]:
        print("Key found!")
        return searchList[mid]
    
    elif key > searchList[mid]:
        print("SearchList now contains", searchList[mid:len(searchList)])
        search(searchList[mid:len(searchList)], key)

    else:
        print("SearchList now contains", searchList[0:mid])
        search(searchList[0:mid], key)


reversed_string = reverse_str(hello)
print("Original String:", hello)
print("Reversed string:", reversed_string)
print("Original parentheses:", paren_input)
balance_parens = check_balanced_parens(paren_input)
print("Balanced Parentheses?:", balance_parens)
print("Queue Simulation:")
simulate_print_queue() 
print(factorial(5))
aList= list(range(1,21))
search(aList, 5)