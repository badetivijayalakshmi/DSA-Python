#Implementation using Arrays(Dynamic array)
#Creation of a stack class
class Stack:
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
    
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(40)
my_stack.push(50)
print("Stack:",my_stack.stack)
print("Pop:",my_stack.pop())
print("New Stack:",my_stack.stack)
print("Peek:",my_stack.peek())
print("Empty or not:",my_stack.isEmpty())
print("Size:",my_stack.size())
#POP removes and returns the top element.
#PEEK only returns the top element without removing it.
