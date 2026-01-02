# Implementation of Stack using Fixed Size Array
class myStack:
    def __init__(self, cap):
        self.arr = [0] * cap
        self.capacity = cap
        self.top = -1

    def push(self, x):
        if self.top == self.capacity - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return -1
        value = self.arr[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.top == -1:
            print("Stack is Empty")
            return -1
        return self.arr[self.top]

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def display(self):
        if self.top == -1:
            print("Stack is Empty")
            return
        print("Stack (bottom → top):", end=" ")
        for i in range(0, self.top + 1):
            print(self.arr[i], end=" ")
        print()

if __name__ == "__main__":
    stack = myStack(4)
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)

    stack.display()
    print("Pop:", stack.pop())
    print("Peek:", stack.peek())
    print("Is Empty:", stack.isEmpty())
    print("Is Full:", stack.isFull())

    #POP removes and returns the top element.
    #PEEK only returns the top element without removing it.
