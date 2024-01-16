class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        dict1 = Counter(nums)
        count = 0       
        max_value = max(dict1.values())

        for key, value in dict1.items():            
            if max_value == value:
                count += value
 
        return count