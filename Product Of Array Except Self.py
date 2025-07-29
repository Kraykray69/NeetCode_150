# Solution 1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i==j:
                    continue
                prod *= nums[j]
            res.append(prod)
        return res


prodself = Solution()
prodself.productExceptSelf([-1,0,1,2,3])



# Solution 2
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
        if zero_cnt > 1:
            return [0] * len(nums)

        res = [0] * len(nums)
        for i in range(len(nums)):
            if zero_cnt:
                if nums[i]:
                    res[i] = 0
                else:
                    res[i] = prod
            else:
                res[i] = prod // nums[i]
        return res


prodself = Solution()
prodself.productExceptSelf([-1,0,1,2,3])



# Solution 3
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pref = [0] * len(nums)
        suf = [0] * len(nums)

        pref[0] = suf[len(nums)-1] = 1
        for i in range(1,len(nums)):
            pref[i] = nums[i-1] * pref[i-1]
        for i in range(len(nums)-2,-1,-1):
            suf[i] = nums[i+1] * suf[i+1]
        for i in range(len(nums)):
            res[i] = pref[i] * suf[i]

        return res
        

prodself = Solution()
prodself.productExceptSelf([-1,0,1,2,3])
