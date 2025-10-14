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


reversed_string = reverse_str(hello)
print("Original String:", hello)
print("Reversed string:", reversed_string)
print("Original parentheses:", paren_input)
balance_parens = check_balanced_parens(paren_input)
print("Balanced Parentheses?:", balance_parens)