class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(nums)
        
        if len(sorted_nums) > 3:
            arr = []
            x = sorted_nums[-1] - sorted_nums[3]
            arr.append(x)
            y = sorted_nums[-4] - sorted_nums[0]
            arr.append(y)
            u = sorted_nums[-2] - sorted_nums[2]
            arr.append(u)
            z = sorted_nums[-3] - sorted_nums[1]
            arr.append(z)
            return min(arr)
        else:
            return 0
            