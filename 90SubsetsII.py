#Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
#
#The solution set must not contain duplicate subsets. Return the solution in any order.
#
# 
#
#Example 1:
#
#Input: nums = [1,2,2]
#Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#Example 2:
#
#Input: nums = [0]
#Output: [[],[0]]
# 
#
#Constraints:
#
#1 <= nums.length <= 10
#-10 <= nums[i] <= 10
#
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, curset = [], []
        self.helper(0, nums, subsets, curset)
        return subsets

    def helper(self, i, nums, subsets, curset):
        if i >= len(nums):
            subsets.append(curset.copy())
            return

        curset.append(nums[i])
        self.helper(i + 1, nums, subsets, curset)
        curset.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

        self.helper(i + 1, nums, subsets, curset)

