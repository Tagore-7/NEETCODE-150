#Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.
#
#Note: (0,8),(8,10) is not considered a conflict at 8.
#
#Example 1:
#
#Input: intervals = [(0,40),(5,10),(15,20)]
#
#Output: 2
#Explanation:
#day1: (0,40)
#day2: (5,10),(15,20)
#
#Example 2:
#
#Input: intervals = [(4,9)]
#
#Output: 1
#Constraints:
#
#0 <= intervals.length <= 500
#0 <= intervals[i].start < intervals[i].end <= 1,000,000
#
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals.sort(key=lambda i: i.start)
        # min_heap = []

        # for interval in intervals:
        #     if min_heap and min_heap[0] <= interval.start:
        #         heapq.heappop(min_heap)
        #     heapq.heappush(min_heap, interval.end)

        # return len(min_heap)

        # two pointers
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res = count = 0
        s = e = 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1

            res = max(res, count)
        return res

