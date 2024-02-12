class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = Counter(nums)

        thresh = len(nums)/2

        for key, value in count.items():
            if value > thresh:
                return key
