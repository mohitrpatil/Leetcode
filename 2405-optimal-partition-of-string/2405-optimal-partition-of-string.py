class Solution:
    def partitionString(self, s: str) -> int:
        
        ans = []
        left = 0
        right = 0
        x = []
        
        while(left<=right and right != len(s)):
            new = s[right]
            if new in x:
                left = right
                ans.append(x)
                x = []
                x.append(new)
            else:
                x.append(new)
            right +=1
        
        ans.append(x)
        return len(ans)