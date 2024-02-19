class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        x = []
        for i in range(32):
            x.append(pow(2,i))
        
        if n in x:
            return True
        else:
            return False
        
        # i=0
        # while i <= 32:
        #     x = pow(2,i)
        #     if x == n:
        #         return True
        #     i+=1
        # return False
        