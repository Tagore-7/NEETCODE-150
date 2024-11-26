#Given a string s, find the length of the longest substring without duplicate characters.
#
#A substring is a contiguous sequence of characters within a string.
#
#Example 1:
#
#Input: s = "zxyzxyz"
#
#Output: 3
#Explanation: The string "xyz" is the longest without duplicate characters.
#
#Example 2:
#
#Input: s = "xxxx"
#
#Output: 1
#Constraints:
#
#0 <= s.length <= 1000
#s may consist of printable ASCII characters.
#
#


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        length = 0
        smap = set()
        for right in range(len(s)):
            while s[right] in smap:
                smap.remove(s[left])
                left += 1
            smap.add(s[right])
            length = max(length, right - left + 1)
        return length
