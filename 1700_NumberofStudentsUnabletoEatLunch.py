# The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

# The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

#     If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
#     Otherwise, they will leave it and go to the queue's end.

# This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

# You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

 

# Example 1:

# Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
# Output: 0 
# Explanation:
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
# - Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
# - Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
# - Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
# - Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
# Hence all students are able to eat.

# Example 2:

# Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
# Output: 3

 

# Constraints:

#     1 <= students.length, sandwiches.length <= 100
#     students.length == sandwiches.length
#     sandwiches[i] is 0 or 1.
#     students[i] is 0 or 1.


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ss = 0
        cs = 0
        for s in students:
            if s == 0:
                cs += 1
            else:
                ss += 1
        for sn in sandwiches:
            if sn == 0 and cs == 0:
                return ss
            if ss == 0 and sn == 1:
                return cs

            if sn == 0:
                cs -= 1
            else:
                ss -= 1
        return 0 


# using stack and queue
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        length = len(students)
        st_queue = deque()
        sn_stack = []

        for i in range(length):
            sn_stack.append(sandwiches[length - i - 1])
            st_queue.append(students[i])

        lser = 0
        while len(st_queue) > 0 and lser < len(st_queue):
            if sn_stack[-1] == st_queue[0]:
                sn_stack.pop()
                st_queue.popleft()
                lser = 0
            else:
                st_queue.append(st_queue.popleft())
                lser += 1
        return len(st_queue)










  

