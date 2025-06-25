#Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.
#
#Example 1:
#
#Input: nums = [1,2,3]
#
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#Example 2:
#
#Input: nums = [7]
#
#Output: [[7]]
#Constraints:
#
#1 <= nums.length <= 6
#-10 <= nums[i] <= 10
#
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(0, nums)

    def helper(self, i, nums):
        if i == len(nums):
            return [[]]

        resPerms = []
        perms = self.helper(i + 1, nums)
        for p in perms:
            for j in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(j, nums[i])
                resPerms.append(pCopy)
        return resPerms

