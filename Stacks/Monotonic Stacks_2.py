#Example-Leetcode-735-Asteroid Collision
#Code
s=[3,5,-6,2,-1,4]
n=len(s)
st=[]
for i in s:
    alive = True
    while st and i<0 and st[-1]>0:
        if abs(i)>abs(st[-1]):
            st.pop()
            continue
        elif abs(i)==abs(st[-1]):
            st.pop()
        alive = False
        break
    if alive:
        st.append(i)
print(st)
