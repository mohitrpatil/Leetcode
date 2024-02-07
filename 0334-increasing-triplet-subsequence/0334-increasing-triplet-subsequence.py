class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first = second = float('inf')
        for i in range(0, len(nums)):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] <= second:
                second = nums[i]
            else:
                return True

        return False
        