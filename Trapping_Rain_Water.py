#You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.
#
#Return the maximum area of water that can be trapped between the bars.
#
#Example 1:
#
#
#
#Input: height = [0,2,0,3,1,0,1,3,2,1]
#
#Output: 9
#Constraints:
#
#1 <= height.length <= 1000
#0 <= height[i] <= 1000
#
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        res = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                res += (leftMax - height[left])
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += (rightMax - height[right])

        return res

