#Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
#
#An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#
#Example 1:
#
#Input: s = "racecar", t = "carrace"
#
#Output: true
#Example 2:
#
#Input: s = "jar", t = "jam"
#
#Output: false
#Constraints:
#
#s and t consist of lowercase English letters.
#
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
        # sorted
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        #hash map
        smap = defaultdict(int)
        tmap = defaultdict(int)
        for c in s:
            smap[c] += 1
        for c in t:
            tmap[c] += 1
        return smap == tmap








