class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        i = 0
        if n%2 == 0 or n == 1:
            while i <= 32:
                x = pow(2,i)
                if x == n:
                    return True
                i+=1
            return False
        else:
            return False
