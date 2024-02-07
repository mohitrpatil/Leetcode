class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        count = defaultdict(list)
        
        for i, n in enumerate(nums):
            count[n].append(i)
        
        if target in count.keys():
            return [count[target][0],count[target][-1]]
        else:
            return [-1,-1]
            
        