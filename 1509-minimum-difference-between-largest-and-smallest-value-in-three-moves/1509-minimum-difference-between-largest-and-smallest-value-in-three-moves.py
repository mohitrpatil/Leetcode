class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(nums)
        
        if len(sorted_nums) > 3:
            mini = 9999999999999999
            x = sorted_nums[-1] - sorted_nums[3]
            mini = min(mini, x)
            y = sorted_nums[-4] - sorted_nums[0]
            mini = min(mini, y)
            u = sorted_nums[-2] - sorted_nums[2]
            mini = min(mini, u)
            z = sorted_nums[-3] - sorted_nums[1]
            mini = min(mini, z)
            return mini
        else:
            return 0
            