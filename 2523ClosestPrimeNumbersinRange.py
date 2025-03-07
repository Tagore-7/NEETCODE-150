#Given two positive integers left and right, find the two integers num1 and num2 such that:
#
#left <= num1 < num2 <= right .
#Both num1 and num2 are prime numbers.
#num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
#Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].
#
# 
#
#Example 1:
#
#Input: left = 10, right = 19
#Output: [11,13]
#Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
#The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
#Since 11 is smaller than 17, we return the first pair.
#Example 2:
#
#Input: left = 4, right = 6
#Output: [-1,-1]
#Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
# 
#
#Constraints:
#
#1 <= left <= right <= 106
#
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = self.sieve(right)
        primeNums = [i for i in range(left, right + 1) if is_prime[i]]

        if len(primeNums) < 2:
            return [-1, -1]

        min_gap = float("inf")
        res = []
        for i in range(len(primeNums) - 1):
            diff = primeNums[i + 1] - primeNums[i]
            if diff < min_gap:
                min_gap = diff
                res = [primeNums[i], primeNums[i + 1]]

        return res
        # primeNums = []
        # gap = {}

        # for i in range(left, right + 1):
        #     if self.prime(i):
        #         primeNums.append(i)

        # res = []
        # for i in range(len(primeNums)):
        #     for j in range(i + 1, len(primeNums)):
        #         heapq.heappush(res, [primeNums[j] - primeNums[i], primeNums[i], primeNums[j]])

        # print(res)
        # return heapq.heappop(res)[1:] if res else [-1, -1]


    def sieve(self, n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(sqrt(n)) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        return is_prime

