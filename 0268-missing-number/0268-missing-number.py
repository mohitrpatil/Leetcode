class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        s = 0
        
        for i in range(len(nums)+1):
            s = s+i
            
        # print(s)
        
        
        for i in range(len(nums)):
            s = s- nums[i]
            
        return s
    
    
#         for i in range(len(sorted_arr)):
#             if i != sorted_arr[i]:
#                 return i
        
#         return i+1