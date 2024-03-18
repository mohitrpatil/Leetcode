class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key=lambda x:x[0])
        # print(points)
        end = points[0][1]
        # print(end)
        
        count = 1
        
        for balloon in points[1:]:
            if balloon[0] > end:
                count += 1
                end = balloon[1]
            else:
                end = min(end, balloon[1])
                
        return count