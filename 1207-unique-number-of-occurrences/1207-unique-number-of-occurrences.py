class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        count = {}

        for each in arr:
            if each in count:
                count[each]+=1
            else:
                count[each]=1

        X= set(count.values())

        if len(X) == len(count.values()):
            return True
        else:
            return False
        