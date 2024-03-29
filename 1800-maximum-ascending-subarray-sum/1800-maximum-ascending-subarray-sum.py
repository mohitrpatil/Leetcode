class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        left = 0
        right = 0
        ans = nums[0]
        local_sum = nums[0]

        while right < len(nums)-1 and left < len(nums)-1:

            right += 1
            
            if nums[right] > nums[right-1]:
                local_sum = local_sum + nums[right]
                ans = max(ans, local_sum)      

            else:
                left = right
                local_sum = nums[left]
                ans = max(ans, local_sum)
                   
        return ans
 