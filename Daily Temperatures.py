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




# Solution 2
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, c in enumerate(temperatures):
            while stack and c > stack[-1][1]:
                index, temp = stack.pop()
                res[index] = i - index
            stack.append((i,c))

        return res


dailytemp = Solution()
dailytemp.dailyTemperatures([30,38,30,36,35,40,28])
