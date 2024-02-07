class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left =0
        right = len(height)-1
        
        ans = 0
        
        while left < right:
            max_height = min(height[left], height[right])
            max_width = right - left
            store = max_height * max_width
            ans = max(ans, store)
            
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        
        return ans
            
            
            
        