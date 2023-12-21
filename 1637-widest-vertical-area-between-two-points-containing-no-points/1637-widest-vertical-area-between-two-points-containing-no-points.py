class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        max_width = -9999
        arr = []
        for i in range (len(points)):
            arr.append(points[i][0])
        # print(arr)
        
        s_arr = sorted(arr)
        for i in range(len(arr)-1):
            max_width = max(max_width, s_arr[i+1]-s_arr[i])
            
        return max_width
            