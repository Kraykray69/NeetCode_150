# Solution 1
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, c in enumerate(heights):
            if stack and c < stack[-1][1]:
                index, ht = stack.pop()
                res = max(res,(i-index) * ht)
                stack.append((index,c))
            else:
                stack.append((i,c))

        for i, h in stack:
            res = max(res,h*(len(heights)-i))

        return res
