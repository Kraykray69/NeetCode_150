# Solution 1
class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        tmp = 0
        for i in range(len(self.stack)):
            for j in range(i+1,len(self.stack)):
                if self.stack[i] < self.stack[j]:
                    tmp = self.stack[i]
                else:
                    tmp = self.stack[j]
        return tmp




