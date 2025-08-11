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
        tmp = self.stack[0]
        for i in range(len(self.stack)):
            for j in range(i+1,len(self.stack)):
                if self.stack[i] < self.stack[j]:
                    tmp = min(tmp, self.stack[i])
                else:
                    tmp = min(tmp, self.stack[j])
        return tmp



# Solution 2
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1:
            self.minstack.append(self.stack[0])
        else:
            self.minstack.append(min(self.minstack[-1],val))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]



