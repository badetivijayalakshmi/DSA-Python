from collections import deque
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Convert students list into a queue
        q = deque(students)
        i = 0  # index for sandwiches
        failed = 0  # count of consecutive failed attempts

        # Continue while students remain and sandwiches remain
        while q and i < len(sandwiches):
            # If front student likes the current sandwich
            if q[0] == sandwiches[i]:
                q.popleft()      # student eats
                i += 1           # move to next sandwich
                failed = 0       # reset failure counter
            else:
                # Student doesn't like sandwich → rotate
                q.append(q.popleft())
                failed += 1

                # If all students have failed for this sandwich → stop
                if failed == len(q):
                    break

        # Remaining students who couldn't eat
        return len(q)

#Metric	Value
#Time	O(n²) worst case
#Space	O(n)
