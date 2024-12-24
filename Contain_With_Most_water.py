#You are given an integer array heights where heights[i] represents the height of the 
#i
#t
#h
#i 
#th
#  bar.
#
#You may choose any two bars to form a container. Return the maximum amount of water a container can store.
#
#Example 1:
#
#
#
#Input: height = [1,7,2,5,4,7,3,6]
#
#Output: 36
#Example 2:
#
#Input: height = [2,2,2]
#
#Output: 4
#Constraints:
#
#2 <= height.length <= 1000
#0 <= height[i] <= 1000
#

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force
        # res = 0

        # for left in range(len(heights)):
        #     for right in range(left + 1, len(heights)):
        #         area = (right - left) * min(heights[left], heights[right])
        #         res = max(area, res)
        # return res

        # linear time
        res = 0
        left, right = 0, len(heights) - 1

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            res = max(area, res)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return res

