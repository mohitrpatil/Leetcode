class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        x = list(count.values())
        if len(x) == len(set(x)):
            return True
        return False
        
        