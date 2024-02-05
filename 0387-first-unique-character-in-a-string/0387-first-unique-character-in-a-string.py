class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        c = defaultdict(list)
        
        for i in range(len(s)):
            c[s[i]].append(i)
        
        mini = len(s)+1
        
        for key, value in c.items():
            if len(value) == 1:
                mini = min(mini, value[0])
                
        if mini > len(s):
            return -1
                
        return mini
            
        