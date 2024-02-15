class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        sort = sorted(nums)
        
        prefix_sum = sum(sort)
        i = len(sort)-1
        while i >= 0:
            x = prefix_sum - sort[i]
            if x > sort[i]:
                return prefix_sum
            else:
                prefix_sum = prefix_sum - sort[i]
                i -=1

        if prefix_sum == 0:
            return -1
        return prefix_sum
