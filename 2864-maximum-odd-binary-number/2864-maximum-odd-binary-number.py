class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        count = Counter(s)

        number_of_1s = count['1']-1
        number_of_0s = count['0']   

        ans = ""
        for i in range(number_of_1s):
            ans += "1"
        
        for i in range(number_of_0s):
            ans += "0"

        ans = ans+"1"

        return ans
        
