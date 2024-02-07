class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        count = Counter(nums)
        
        sorted_count = {key:value for key, value in sorted(count.items(), key=lambda item:(item[1], -item[0]))}
        
        ans = []
        
        for key, value in sorted_count.items():
            for i in range(value):
                ans.append(key)
                
        return ans
            