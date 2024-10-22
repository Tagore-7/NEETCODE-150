#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
#
#Example 1:
#
#Input: nums = [1, 2, 3, 3]
#
#Output: true
#Example 2:
#
#Input: nums = [1, 2, 3, 4]
#
#Output: false
#
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numMap = {}

        for num in nums:
            if num not in numMap:
                numMap[num] = 1
            else:
                return True
        return False
