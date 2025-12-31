# Stack follows LIFO principle (Last In, First Out)

stack = []

# -------- PUSH Operation --------
# Time Complexity: O(1)
# Space Complexity: O(1)
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# -------- PEEK Operation --------
# Returns top element without removing it
# Time Complexity: O(1)
if len(stack) != 0:
    print("Top element:", stack[-1])
else:
    print("Stack is empty")

# -------- POP Operation --------
# Removes top element
# Time Complexity: O(1)
if len(stack) != 0:
    popped_element = stack.pop()
    print("Popped element:", popped_element)
else:
    print("Stack Underflow")

print("Stack after pop:", stack)

# -------- isEmpty Operation --------
# Time Complexity: O(1)
if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")

# -------- SIZE Operation --------
# Time Complexity: O(1)
print("Size of stack:", len(stack))
