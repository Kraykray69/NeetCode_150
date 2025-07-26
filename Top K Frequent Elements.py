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



# Solution 2
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                if len(res) < k:
                    res.append(num)
        return res                        


topKFreq = Solution()
topKFreq.topKFrequent([1,2,2,4,4,3,3,3],2)  
