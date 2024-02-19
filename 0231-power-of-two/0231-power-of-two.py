class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i=0
        while i <= 32:
            x = pow(2,i)
            if x == n:
                return True
            i+=1
        return False
        