#You are given an integer array nums and an integer k.
#
#Find the longest subsequence of nums that meets the following requirements:
#
#The subsequence is strictly increasing and
#The difference between adjacent elements in the subsequence is at most k.
#Return the length of the longest subsequence that meets the requirements.
#
#A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
#
# 
#
#Example 1:
#
#Input: nums = [4,2,1,4,3,4,5,8,15], k = 3
#Output: 5
#Explanation:
#The longest subsequence that meets the requirements is [1,3,4,5,8].
#The subsequence has a length of 5, so we return 5.
#Note that the subsequence [1,3,4,5,8,15] does not meet the requirements because 15 - 8 = 7 is larger than 3.
#Example 2:
#
#Input: nums = [7,4,5,1,8,12,4,7], k = 5
#Output: 4
#Explanation:
#The longest subsequence that meets the requirements is [4,5,8,12].
#The subsequence has a length of 4, so we return 4.
#Example 3:
#
#Input: nums = [1,5], k = 1
#Output: 1
#Explanation:
#The longest subsequence that meets the requirements is [1].
#The subsequence has a length of 1, so we return 1.
# 
#
#Constraints:
#
#1 <= nums.length <= 105
#1 <= nums[i], k <= 105
#
class SegementTree:
    def __init__(self, N):
        self.n = N
        while (self.n & (self.n - 1)) !=  0:
            self.n += 1
        self.tree = [0] * (2 * self.n)

    def update(self, i, val):
        if val <= self.tree[self.n + i]:
            return
        self.tree[self.n + i] = val
        j = (self.n + i ) >> 1
        while j >= 1:
            self.tree[j] = max(self.tree[j << 1], self.tree[j << 1 | 1])
            j >>= 1

    def query(self, ql, qh):
        l =  ql + self.n
        r = qh + self.n + 1
        res = 0
        while l < r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        ST = SegementTree(max_val  + 1 )
        res = 0

        for num in nums:
            l = max(0, num - k)
            r = max(0, num - 1)
            curr = ST.query(l, r) + 1
            res = max(res, curr)
            ST.update(num, curr)

        return res

