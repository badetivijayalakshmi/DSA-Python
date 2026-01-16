 🧠 Deque (Double-Ended Queue) — Cheat Sheet for DSA

## 1️⃣ What is a Deque?

A **Deque (Double-Ended Queue)** is a linear data structure that allows **insertion and deletion from both ends** (front & rear).

👉 It can behave like:

* **Stack (LIFO)**
* **Queue (FIFO)**

---

## 2️⃣ Why Deque Matters in DSA

Deque is used to:

* Implement **Stacks & Queues**
* Solve **Sliding Window** problems
* Build **Monotonic Stack / Queue**
* Achieve **O(1)** insertions & deletions at both ends

---

## 3️⃣ Deque vs Stack vs Queue

| Structure | Insert    | Delete    | Order    |
| --------- | --------- | --------- | -------- |
| Stack     | One end   | Same end  | LIFO     |
| Queue     | Rear      | Front     | FIFO     |
| Deque     | Both ends | Both ends | Flexible |

---

## 4️⃣ Python Deque Initialization

```python
from collections import deque
dq = deque()
```

---

## 5️⃣ Core Deque Operations (O(1))

| Operation     | Code               |
| ------------- | ------------------ |
| Insert rear   | `dq.append(x)`     |
| Insert front  | `dq.appendleft(x)` |
| Remove rear   | `dq.pop()`         |
| Remove front  | `dq.popleft()`     |
| Front element | `dq[0]`            |
| Rear element  | `dq[-1]`           |

---

## 6️⃣ Implementing Stack Using Deque

### Stack (Using Rear as Top)

```python
stack = deque()

stack.append(10)   # push
stack.append(20)

stack.pop()        # pop
top = stack[-1]    # peek
```

✔ LIFO behavior
✔ O(1) operations

---

### Stack (Using Front as Top)

```python
stack = deque()

stack.appendleft(10)
stack.appendleft(20)

stack.popleft()
```

---

## 7️⃣ Why Deque over List?

| Feature                | List   | Deque  |
| ---------------------- | ------ | ------ |
| Insert/Delete at front | ❌ O(n) | ✅ O(1) |
| Stack operations       | ✅      | ✅      |
| Queue operations       | ❌      | ✅      |
| DSA efficiency         | ⚠️     | ✅      |

👉 **Deque is safer and more efficient**

---

## 8️⃣ Deque in Monotonic Stack / Queue

Used when maintaining **ordered elements**.

### Monotonic Decreasing Deque

```python
while dq and dq[-1] < curr:
    dq.pop()
dq.append(curr)
```

✔ Front always stores maximum

---

## 9️⃣ Sliding Window Pattern (Core Idea)

```python
# remove out-of-window indices
if dq[0] == i - k:
    dq.popleft()

# maintain monotonic order
while dq and nums[dq[-1]] < nums[i]:
    dq.pop()

dq.append(i)
```

---

## 🔟 When to Use Deque?

✔ Need both stack & queue behavior
✔ Sliding window problems
✔ Monotonic stack/queue
✔ O(1) front & rear operations

