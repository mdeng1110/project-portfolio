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