#The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.
#
#For examples, if arr = [2,3,4], the median is 3.
#For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
#You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
#
#Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.
#
# 
#
#Example 1:
#
#Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
#Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
#Explanation: 
#Window position                Median
#---------------                -----
#[1  3  -1] -3  5  3  6  7        1
# 1 [3  -1  -3] 5  3  6  7       -1
# 1  3 [-1  -3  5] 3  6  7       -1
# 1  3  -1 [-3  5  3] 6  7        3
# 1  3  -1  -3 [5  3  6] 7        5
# 1  3  -1  -3  5 [3  6  7]       6
#Example 2:
#
#Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
#Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
# 
#
#Constraints:
#
#1 <= k <= nums.length <= 105
#-231 <= nums[i] <= 231 - 1
#


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        min_heap = []
        max_heap = []
        diff = defaultdict(int)

        for i in range(k):
            heapq.heappush(min_heap, -nums[i])
        for i in range(k // 2):
            heapq.heappush(max_heap, -1 * heapq.heappop(min_heap))

        res = [-1 * min_heap[0] if k & 1 else (max_heap[0] -min_heap[0]) / 2]

        for i in range(k, len(nums)):
            diff[nums[i - k]] += 1
            balance = -1 if min_heap and nums[i - k] <= -min_heap[0] else 1

            if min_heap and nums[i] <= -min_heap[0]:
                heapq.heappush(min_heap, -1 * nums[i])
                balance += 1
            else:
                heapq.heappush(max_heap, nums[i])
                balance -= 1

            if balance > 0:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            if balance < 0:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))

            while min_heap and diff[-min_heap[0]] > 0:
                diff[-heapq.heappop(min_heap)] -= 1

            while max_heap and diff[max_heap[0]] > 0:
                diff[heapq.heappop(max_heap)] -= 1

            res.append(-min_heap[0] if k & 1 else (max_heap[0] -min_heap[0]) / 2)

        return res







        #brute force
        # res = []

        # for i in range(len(nums) - k + 1):
        #     tmp = nums[i : i + k ][:]
        #     tmp.sort()
        #     if k & 1:
        #         res.append(tmp[k // 2])
        #     else:
        #         res.append((tmp[k //2 ] + tmp[(k -1) // 2]) / 2)

        # return res


