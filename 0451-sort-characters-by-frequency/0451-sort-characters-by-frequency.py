class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = Counter(s)
        print(count)
        
        sorted_count = {key:value for key, value in sorted(count.items(), key=lambda item:item[1], reverse= True)}
        print(sorted_count)
        
        ans = []
        
        for key, value in sorted_count.items():
            for i in range(value):
                ans.append(key)
                
        return ''.join(ans)