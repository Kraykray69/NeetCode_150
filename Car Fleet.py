# Solution 1
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pospeed = list(zip(position,speed))
        pospeed.sort(reverse=True)

        for p, s in pospeed:
            stack.append((target - p)/s)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


car = Solution()
car.carFleet(target = 10, position = [1,4], speed = [3,2])
