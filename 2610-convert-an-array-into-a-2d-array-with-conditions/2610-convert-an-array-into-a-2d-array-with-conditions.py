class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:

        count = Counter(nums)
        a = {0}
        main = []

        while set(count.values()) != a:
            arr = []
            for key, value in count.items():
                if value != 0:
                    arr.append(key)
                    count[key] -= 1
            
            main.append(arr)

        return main
                
            
        