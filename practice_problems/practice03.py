hello = "hello"

def reverse_str(lst):
    stack = []

    for char in lst:
        stack.append(char)

    reversed_chars = []
    while stack:
        reversed_chars.append(stack.pop())

    return "".join(reversed_chars)


reversed_string = reverse_str(hello)
print("Original String:", hello)
print("Reversed string:", reversed_string)