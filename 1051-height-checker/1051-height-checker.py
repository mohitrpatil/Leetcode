class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        sorted_arr = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != sorted_arr[i]:
                count += 1
        return count