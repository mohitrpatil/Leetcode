class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 1: 
            return 1
            
        ans = ""
        count = 0 

        for j in s:
            if j not in ans:
                ans += j
            else:
                x = ans.index(j)
                ans = ans[x+1:]+j
            
            if len(ans)>count:
                count = len(ans)
        return count