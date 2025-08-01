# Solution 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        for c in s:
            if c.isalnum():
                string += c.lower()

        return string == string[::-1]


valpal = Solution()
valpal.isPalindrome("Was it a car or a cat I saw?")



