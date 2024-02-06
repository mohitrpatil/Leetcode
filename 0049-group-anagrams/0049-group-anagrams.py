class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c = defaultdict(list)
        
        for i in range(len(strs)):
            x = tuple(sorted(strs[i]))
            c[x].append(strs[i])
            
        ans = []
        for key, value in c.items():
            ans.append(value)
            
        return ans