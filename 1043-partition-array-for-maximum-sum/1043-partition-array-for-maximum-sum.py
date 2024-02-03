class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        n = len(arr)
        @cache
        def dfs(i):
            if i >= n:
                return 0
            # make all possible k partitions for a partition          
            res = 0
            max_in_part = 0
            for j in range(0, k):
                if j + i < n:
                    max_in_part = max(max_in_part, arr[i+j])
                    res = max(res, max_in_part*(j+1) + dfs(i+(j+1)))
            return res
        return dfs(0)