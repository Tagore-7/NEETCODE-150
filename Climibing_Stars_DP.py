#You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.
#
#Return the number of distinct ways to climb to the top of the staircase.
#
#Example 1:
#
#Input: n = 2
#
#Output: 2
#Explanation:
#
#1 + 1 = 2
#2 = 2
#Example 2:
#
#Input: n = 3
#
#Output: 3
#Explanation:
#
#1 + 1 + 1 = 3
#1 + 2 = 3
#2 + 1 = 3
#Constraints:
#
#1 <= n <= 30
#
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.dp(n , {})

    def dp(self, n: int, cache: dict) -> int:
        if n == 2:
            return 2
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = self.dp(n - 1, cache) +  self.dp(n - 2, cache)
        return cache[n]

