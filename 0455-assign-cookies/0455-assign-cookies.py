class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        size_pointer = 0
        greed_pointer = 0
        
        sorted_size_desc = sorted(s, reverse=True)
        sorted_greed_desc = sorted(g, reverse=True)
        
        if len(s) ==0:
            return 0
        
        count = 0
        for i in range(len(g)):
            print("greed:", sorted_greed_desc[i])
            print("size:", sorted_size_desc[size_pointer])
            if sorted_greed_desc[i] <= sorted_size_desc[size_pointer]:
                count+=1
                if len(s) == size_pointer + 1:
                    break
                size_pointer+=1

        print("count:",count)
        return count