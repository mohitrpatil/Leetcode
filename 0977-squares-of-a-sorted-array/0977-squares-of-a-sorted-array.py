class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        x = sorted([i*i for i in nums])

        return x