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




# Solution 2
class Solution:
    def trap(self, height: List[int]) -> int:
        min_list = [0] * len(height)
        min_list[0], min_list[len(height)-1] = height[0], height[len(height)-1]
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] <= height[r]:
                l += 1
                min_list[l] = max(height[l],min_list[l-1])
                res += min_list[l] - height[l]
            elif height[l] > height[r]:
                r -= 1
                min_list[r] = max(height[r],min_list[r+1])
                res += min_list[r] - height[r]

        return res


traprain = Solution()
traprain.trap([0,2,0,3,1,0,1,3,2,1])




# Solution 3
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        leftMax = height[l]
        rightMax = height[r]
        while l < r:
            if height[l] <= height[r]:
                l += 1
                leftMax = max(height[l], leftMax)
                res += leftMax - height[l]
            elif height[l] > height[r]:
                r -= 1
                rightMax = max(height[r], rightMax)
                res += rightMax - height[r]

        return res


traprain = Solution()
traprain.trap([0,2,0,3,1,0,1,3,2,1])
        
