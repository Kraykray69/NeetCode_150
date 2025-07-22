# Solution 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        

anagram_1 = Solution()
anagram_1.isAnagram('racecar','carrace')
