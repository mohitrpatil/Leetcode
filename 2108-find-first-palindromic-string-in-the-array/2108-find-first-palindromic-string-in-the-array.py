class Solution:
    
    def isPalindrome(self, s):
        if s == s[::-1]:
            return True
        else:
            return False
        
    def firstPalindrome(self, words: List[str]) -> str:
        
        for w in words:
            if self.isPalindrome(w):
                return w
        
        return ""
        