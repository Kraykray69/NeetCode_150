# Solution 1
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(openN,closedN):
            if openN < n:
                stack.append('(')
                backtrack(openN+1,closedN)
                stack.pop()
            if openN > closedN:
                stack.append(')')
                backtrack(openN,closedN+1)
                stack.pop()
            if openN == closedN == n:
                res.append(''.join(stack))
                return

        backtrack(0,0)
        return res


genpar = Solution()
genpar.generateParenthesis(5)
