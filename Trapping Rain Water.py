# Solution 1
class Solution:
    def trap(self, height: List[int]) -> int:
        pref = [0] * len(height)
        suf = [0] * len(height)
        res = 0

        pref[0] = height[0]
        for i in range(1,len(height)):
            pref[i] = max(pref[i-1],height[i])

        suf[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            suf[i] = max(suf[i+1],height[i])

        for i in range(len(height)):
            res += min(pref[i],suf[i]) - height[i]

        return res


traprain = Solution()
traprain.trap([0,2,0,3,1,0,1,3,2,1])
