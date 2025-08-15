# Solution 1
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res.append(j-i)
                    break
                elif j == len(temperatures) - 1:
                    res.append(0)
        res.append(0)
        return res


dailytemp = Solution()
dailytemp.dailyTemperatures([30,38,30,36,35,40,28])
