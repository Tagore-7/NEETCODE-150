#Given an array nums of unique integers, return all possible subsets of nums.
#
#The solution set must not contain duplicate subsets. You may return the solution in any order.
#
#Example 1:
#
#Input: nums = [1,2,3]
#
#Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#Example 2:
#
#Input: nums = [7]
#
#Output: [[],[7]]
#Constraints:
#
#1 <= nums.length <= 10
#-10 <= nums[i] <= 10
#
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, curSet = [], []
        self.helper(0, nums, subsets, curSet)
        return subsets

    def helper(self, i, nums, subsets, curSet):
        if i >= len(nums):
            subsets.append(curSet.copy())
            return

        curSet.append(nums[i])
        self.helper(i + 1, nums, subsets, curSet)
        curSet.pop()

        self.helper(i + 1, nums, subsets, curSet)


