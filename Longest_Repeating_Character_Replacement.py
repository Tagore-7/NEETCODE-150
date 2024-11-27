#You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.
#
#After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
#
#Example 1:
#
#Input: s = "XYYX", k = 2
#
#Output: 4
#Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.
#
#Example 2:
#
#Input: s = "AAABABB", k = 1
#
#Output: 5
#Constraints:
#
#1 <= s.length <= 1000
#0 <= k <= s.length
#
class Solution:
    def characterReplacement(self, k: int, s: str) -> int:
        count = {}
        res = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            while ( right - left  + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res 

test = Solution()
print(test.characterReplacement(1, "AAABABB"))

