# Solution 1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        arr = []
        for i,cnt in count.items():
            arr.append([cnt,i])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res


topKFreq = Solution()
topKFreq.topKFrequent([1,2,2,4,4,3,3,3],2)
