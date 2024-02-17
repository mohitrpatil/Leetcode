class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        building_gap_heap = []
        
        total_buildings = len(heights)
        
        for i in range( total_buildings-1 ):
            
            cur_building_gap = heights[i+1] - heights[i]
            
            
            if cur_building_gap > 0:

                heappush(building_gap_heap, cur_building_gap)
            
            
            if len(building_gap_heap) > ladders:
                
                gap_to_climb = heappop(building_gap_heap)
                bricks -= gap_to_climb
            
            
            if bricks < 0:
                return i

        return total_buildings-1