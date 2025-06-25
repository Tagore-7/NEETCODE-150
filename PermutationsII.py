#You are given an array nums, that might contain duplicates , return all possible unique permutations in any order.
#
#Example 1:
#
#Input: nums = [1,1,2]
#
#Output: [
#    [1,1,2],
#    [1,2,1],
#    [2,1,1]
#]
#Example 2:
#
#Input: nums= [2,2]
#
#Output: [[2,2]]
#Constraints:
#
#1 <= nums.length <= 8
#-10 <= nums[i] <= 10
#
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = {n : 0 for n in nums}
        for num in nums:
            count[num] += 1

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for num in count:
                if count[num] > 0:
                    perm.append(num)
                    count[num] -= 1
                    dfs()
                    count[num] += 1
                    perm.pop()

        dfs()
        return res

