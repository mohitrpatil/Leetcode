class Solution:
    
    def solve(self, low, high, size, arr):
        
        local_ans =[]
        
        for i in range(1, len(arr)):
            x = arr[i:i+size]
            if len(x) == size:
                d = int("".join(x))
                if low <= d <= high:
                    local_ans.append(d)
        
        return local_ans
            
        
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        ans = []
        l = len(str(low))
        h = len(str(high))

        size_allowed = [i for i in range(l, h+1)]
        
        arr = [str(i) for i in range(0, 10)]
        
        for i in range(len(size_allowed)):
            ans = ans + self.solve(low, high, size_allowed[i], arr)
        
        return ans