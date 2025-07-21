# Solution 1
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False



list1 = Solution()       
list1.hasDuplicate([1,2,3,4])



# Solution 2
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) == 1:
            return False
        for i in range(len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False



list1 = Solution()       
list1.hasDuplicate([1,2,3,4])
