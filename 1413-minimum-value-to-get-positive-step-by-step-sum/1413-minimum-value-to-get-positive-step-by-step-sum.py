class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        arr = []
        
        for i in range(len(nums)):
            if i == 0:
                arr.append(nums[i])
            else:
                x = arr[i-1]+nums[i]
                arr.append(x)

        mini = min(arr)
        if mini<=0:
            return abs(mini)+1
        else:
            return 1