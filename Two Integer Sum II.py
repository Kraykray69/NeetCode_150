# Solution 1
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]


twosum = Solution()
twosum.twoSum([1,2,3,4],3)



# Solution 2
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        check = {}
        for i, c in enumerate(numbers):
            check[c] = i
        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference in check and i!=check[difference]:
                return [i+1,check[difference]+1]
            

twosum = Solution()
twosum.twoSum([1,2,3,4], 3)  
