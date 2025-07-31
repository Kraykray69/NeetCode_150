# Solution 1
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        check = set(nums)
        longest = 0

        for i in range(len(nums)):
            current = nums[i]
            count = 1
            if current - 1 not in check:
                while current + 1 in check:
                    current += 1
                    count += 1
            longest = max(longest,count)

        return longest


longcons = Solution()
longcons.longestConsecutive([2,20,4,10,3,4,5])
