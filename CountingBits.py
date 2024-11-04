#Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].
#
#Return an array output where output[i] is the number of 1's in the binary representation of i.
#
#Example 1:
#
#Input: n = 4
#
#Output: [0,1,1,2,1]
#Explanation:
#0 --> 0
#1 --> 1
#2 --> 10
#3 --> 11
#4 --> 100
#
#Constraints:
#
#0 <= n <= 1000
#
class Solution:
    def countBits(self, n: int) -> List[int]:
        nums = []
        for i in range(n + 1):
            nums.append(self.count1bits(i))
        return nums

    def count1bits(self, n: int) -> int:
        count = 0
        while n:
            if n & 1:
                count += 1
            n >>= 1
        return count
