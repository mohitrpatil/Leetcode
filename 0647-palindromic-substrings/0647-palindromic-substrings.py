class Solution:
    def countSubstrings(self, s: str) -> int:
        
        ans = []

        def ispalindrome(s):
            if s == s[::-1]:
                return True
            else:
                return False
        
        size = len(s)
        
        for t in range(1,size+1):
            for i in range(0,len(s)-t+1):
                x = s[i:i+t]
                if ispalindrome(x):
                    ans.append(x)
        
        return len(ans)