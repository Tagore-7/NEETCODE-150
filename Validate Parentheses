class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack_s = []
        for c in s:
            if c not in close_to_open:
                stack_s.append(c)
            elif len(stack_s) and close_to_open[c] == stack_s[-1]:
                    stack_s.pop()
            else:
                return False
        return False if len(stack_s) else True
