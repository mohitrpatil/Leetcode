class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        sorted_arr = sorted(nums)

        for i in range(len(sorted_arr)):
            if i != sorted_arr[i]:
                return i
        
        return i+1