# Solution 1
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()','')
            s = s.replace('[]','')
            s = s.replace('{}','')
        return True if s == '' else False


val = Solution()
val.isValid("([{}])")
