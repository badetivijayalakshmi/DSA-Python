# ================================
# MONOTONIC STACK — REVISION NOTES
# ================================

# A monotonic stack is a stack that maintains its elements
# in a specific order by popping elements when the rule is violated.

# --------------------------------
# CASE 1: MONOTONIC DECREASING STACK
# Use case: Next Greater Element on the Right
# --------------------------------

a = [4, 5, 2, 10, 8]
n = len(a)

ans = [-1] * n           # stores next greater element
st = []                  # stack stores indices

for i in range(n):
    while st and a[st[-1]] < a[i]:
        idx = st.pop()
        ans[idx] = a[i]
    st.append(i)

print(ans)
# Output: [5, 10, 10, -1, -1]

# --------------------------------
# CASE 2: MONOTONIC DECREASING STACK (Right to Left)
# Use case: Check if an element has a taller element on the right
# --------------------------------

s = [3, 7, 4, 5, 2]
n = len(s)

ans = [True] * n         # True means visible
st = []                  # stack stores heights

for i in range(n - 1, -1, -1):
    while st and st[-1] <= s[i]:
        st.pop()

    if st:
        ans[i] = False

    st.append(s[i])

print(ans)
# Output: [False, True, False, True, True]

# --------------------------------
# CASE 3: MONOTONIC INCREASING STACK 
# Use case: Find nearest smaller element on the left.
# --------------------------------

s = [1, 3, 0, 2, 5]
st = []
n = len(s)
ans = [-1] * n
for i in range(n-1, -1, -1):
    while st and s[st[-1]] > s[i]:
        x = st.pop()
        ans[x] = s[i]
    st.append(i)
    
print(ans)
#Output: [-1, 1, -1, 0, 2]
