# Solution 1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add(tuple([nums[i],nums[j],nums[k]]))

        return list(res)


threesum = Solution()
threesum.threeSum([-1,0,1,2,-1,-4])



