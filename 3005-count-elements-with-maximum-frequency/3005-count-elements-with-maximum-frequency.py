class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        maxi  = max(count.values())
        ans = 0
        
        for key,value in count.items():
            if value == maxi:
                ans = ans+maxi
                
        return ans