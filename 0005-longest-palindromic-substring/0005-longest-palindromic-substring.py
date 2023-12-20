class Solution:

    def check(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            return False

    def longestPalindrome(self, s: str) -> str:
        
        length = len(s)

        while(length > 0):
            for i in range(len(s) - length +1):
                sub = s[i:i+length]
                if self.check(sub):
                    return sub
            length -= 1