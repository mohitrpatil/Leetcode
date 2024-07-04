class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        x = []
        
        ref = [3*i for i in range(50)]
        # print(ref)
        
        for i in range(len(nums)):
            mini = 9999999
            for j in range(len(ref)):
                mini = min(mini, abs (nums[i] - ref[j]))
                
            x.append(mini)
        # print(x)
        return sum(x)