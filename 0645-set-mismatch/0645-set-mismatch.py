class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count ={}

        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1

        
        filt = {key: value for key, value in count.items() if value>1}

        X = list(filt.keys())

        for i in range(1,len(nums)+1):
            if i not in count:
                X.append(i)

        return X