class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        if len(arr) == k:
            return 0
        
        count = Counter(arr)
        
        sorted_count = {key: value for key, value in sorted(count.items() ,key=lambda item:item[1])}
        
        x = list(sorted_count.keys())
        y = list(sorted_count.values())
        
        ans = 0
        for j in range(len(y)):
            if y[j] <= k:
                k = k-y[j]
            else:
                k=0
                ans = j
                break
        
        return len(x[ans:])
        