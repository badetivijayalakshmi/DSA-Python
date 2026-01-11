# 🧱 Stack & Monotonic Stack — Interview Revision Notes

These notes focus on **how to think** about stack problems, not just how to code them.  
They are intended for **quick revision before interviews and coding rounds**.

---

## 📌 When to Use a Stack

Use a stack when a problem involves:

- Nearest element (left / right)
- Matching or pairing (parentheses, symbols)
- Undo / backtracking behavior
- Collision or elimination
- Sequential dependency
- “Next Greater / Smaller” element pattern

---

## 📌 What to Store in the Stack?

Before coding, decide:

- **Values** → when only comparison matters
- **Indices** → when distance, position, or result array updates are needed

---

## 🔁 Core Stack Principle

> **Pop elements when they become useless for future comparisons.**

---

## 🧠 Defining the POP Condition (Most Important Step)

Always write the pop condition in words **before coding**.

Examples:

| Problem Type | Pop Condition |
|-------------|--------------|
| Next Greater Element | `stack top < current` |
| Daily Temperatures | `temp[stack top] < current temp` |
| Valid Parentheses | `stack top matches current` |
| Remove Adjacent Duplicates | `stack top == current` |
| Asteroid Collision | `stack top > 0 AND current < 0` |

---

## ⚠️ `while` vs `if`

Use a **`while` loop** when:
- One element can affect **multiple previous elements**
- Chain reactions are possible

Common examples:
- Asteroid Collision
- Next Greater Element
- Daily Temperatures

---

## 📌 When to Push?

General rule:
Push an element ONLY if it survives all conflicts.

- Some problems push immediately
- Some push after resolving conflicts using a `while` loop

---

## 🧩 Monotonic Stack

A **monotonic stack** maintains elements in a specific order.

---

### 🔼 Monotonic Increasing Stack

- Elements increase from bottom to top
- Used for:
  - Next Greater Element
  - Daily Temperatures
  - Taller person / building problems

**Pop rule:**
while stack and stack top < current:
 Monotonic Decreasing Stack

- Elements decrease from bottom to top
- Used for:
  - Next Smaller Element

**Pop rule:**
while stack and stack top > current:
pop

yaml
Copy code

---

## 🪐 Asteroid Collision — Logic Summary

- Positive value → asteroid moving right
- Negative value → asteroid moving left
- Collision occurs only when:
stack top > 0 AND current < 0

yaml
Copy code

### Collision Rules:
- Larger magnitude survives
- Smaller magnitude is destroyed
- Equal magnitude → both destroyed

Use a **while loop** because one asteroid may destroy multiple asteroids.

---

## 🧠 Universal Stack Problem Template

```python
stack = []

for x in arr:
    while stack and conflict(stack[-1], x):
        resolve_conflict()
    if survives:
        stack.append(x)
