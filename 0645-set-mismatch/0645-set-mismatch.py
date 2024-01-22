class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        keys = []
        for key, value in count.items():
            if value>1:
                keys.append(key)
        
        for i in range(1, len(nums)+1):
            if i not in count:
                keys.append(i)
                
        return keys