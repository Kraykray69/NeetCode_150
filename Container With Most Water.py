# Solution 1
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        longest = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                longest = max(longest, min(heights[i],heights[j]) * (j-i))

        return longest
