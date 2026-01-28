class MyQueue:
    def __init__(self, cap):
        # Initialize queue with fixed capacity
        self.arr = [0] * cap          # Array to store queue elements
        self.size = 0                # Current number of elements
        self.front = 0               # Index of front element
        self.capacity = cap          # Maximum size of queue

    def enqueue(self, x):
        # Check for overflow condition
        if self.size == self.capacity:
            print("Overflow")
            return

        # Calculate rear index using circular logic
        rear = (self.front + self.size) % self.capacity
        self.arr[rear] = x            # Insert element at rear
        self.size += 1                # Increase queue size

    def dequeue(self):
        # Check for underflow condition
        if self.size == 0:
            return -1

        # Remove front element
        res = self.arr[self.front]
        # Move front pointer circularly
        self.front = (self.front + 1) % self.capacity
        self.size -= 1                # Decrease queue size
        return res

    def getRear(self):
        # Return rear element of queue
        if self.size == 0:
            return -1
        rear = (self.front + self.size - 1) % self.capacity
        return self.arr[rear]

    def getFront(self):
        # Return front element of queue
        if self.size == 0:
            return -1
        return self.arr[self.front]


# -------- Driver Code to Test Circular Queue --------

q = MyQueue(5)

# Enqueue elements
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

# Check front and rear
print("Front:", q.getFront())   # Expected: 10
print("Rear:", q.getRear())     # Expected: 30

# Dequeue one element
print("Dequeue:", q.dequeue())  # Expected: 10
print("Front after dequeue:", q.getFront())  # Expected: 20

# Test circular behavior
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)                   # Wraps around to index 0

print("Rear:", q.getRear())     # Expected: 60

# Remove all elements
print(q.dequeue())  # 20
print(q.dequeue())  # 30
print(q.dequeue())  # 40
print(q.dequeue())  # 50
print(q.dequeue())  # 60

# Dequeue from empty queue
print(q.dequeue())  # Expected: -1

#Concepts Used:
#Circular Queue, Modulo Arithmetic, Array-based Queue

#Time Complexity:
#Enqueue → O(1), Dequeue → O(1)

#Why Circular Queue?
#Avoids wasted space caused by false overflow in linear queues.
