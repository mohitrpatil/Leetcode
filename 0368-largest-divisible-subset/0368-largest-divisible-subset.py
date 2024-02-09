class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        # Sort the input array
        nums.sort()

        # Initialize a dynamic programming table
        # dp[i] stores the size of the largest divisible subset that ends with nums[i]
        dp = [1] * len(nums)

        # Initialize a backtracking table
        # prev[i] stores the index of the previous element in the largest divisible subset that ends with nums[i]
        prev = [-1] * len(nums)

        # Find the largest divisible subset and its size
        max_size = 1
        max_index = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i

        # Backtrack to find the largest divisible subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]

        return result[::-1]
                
        
        
                     
            
        