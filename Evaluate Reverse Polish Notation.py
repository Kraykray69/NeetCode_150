# Solution 1
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in '+-/*':
                b = int(stack.pop())
                a = int(stack.pop())
                if i == '+':
                    stack.append(a+b)
                elif i == '-':
                    stack.append(a-b)
                elif i == '*':
                    stack.append(a*b)
                elif i == '/':
                    stack.append(int(a/b))
            else:
                stack.append(i)
        return stack[-1]


rpn = Solution()
rpn.evalRPN(["1","2","+","3","*","4","-"])
