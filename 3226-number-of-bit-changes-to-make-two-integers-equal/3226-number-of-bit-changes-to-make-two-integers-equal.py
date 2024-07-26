class Solution:
    def minChanges(self, n: int, k: int) -> int:
        
        nbin = str(bin(n))[2:]
        # print(nbin)
        
        kbin = str(bin(k))[2:]
        # print(kbin)
        
        if len(nbin) < len(kbin):
            while len(nbin) != len(kbin):
                nbin = '0'+nbin
        else:
            while len(nbin) != len(kbin):
                kbin = '0'+kbin
                
        print(nbin)
        print(kbin)
        s = 0
        
        for i in range(len(nbin)):
            if nbin[i] == '1' and kbin[i] == '0':
                s = s + 1
            elif nbin[i] == '0' and kbin[i] == '1':
                return -1
            else:
                continue
                
        return s
                
        