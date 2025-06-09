#iYou are given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
#
#You may return the answer in any order.
#
#Example 1:
#
#Input: n = 3, k = 2
#
#Output: [
#    [1,2],
#    [1,3],
#    [2,3]
#]
#Example 2:
#
#Input: n = 3, k = 3
#
#Output: [[1,2,3]]
#Constraints:
#
#1 <= k <= n <= 20
#
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return

            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()

        backtrack(1, [])

        return res


