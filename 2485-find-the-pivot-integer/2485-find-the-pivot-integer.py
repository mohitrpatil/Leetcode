class Solution:
    def pivotInteger(self, n: int) -> int:
        
        arr = [i for i in range(1, n+1)]
        
        for i in range(1,n+1):
            x = sum(arr[:i])
            y = sum(arr[i-1:])
            print("X: ",x)
            print("Y: ",y)
            if x == y:
                return i
        
        return -1
        