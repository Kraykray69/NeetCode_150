# Solution 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    answer.append(i)
                    answer.append(j)
                    return answer


two_sum = Solution()
two_sum.twoSum([3,4,5,6],7)


# Solution 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i, value in enumerate(nums):
            check[value] = i
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in check and i != check[difference]:
                return [i,check[difference]]

  
two_sum = Solution()
two_sum.twoSum([3,4,5,6],7)

