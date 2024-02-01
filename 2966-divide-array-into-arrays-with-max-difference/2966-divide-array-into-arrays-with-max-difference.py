class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        sorted_arr = sorted(nums)
        size = 3
        ans = []
        
        for i in range(0,len(sorted_arr),3):
            x = sorted_arr[i:i+3]
            
            if x[2] - x[0] <=k:
                ans.append(x)
            else:
                return []
        
        return ans
            