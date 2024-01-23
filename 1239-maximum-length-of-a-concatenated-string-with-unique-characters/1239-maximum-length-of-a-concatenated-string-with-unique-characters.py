class Solution:
    
    def checkunique(self, temp ,s):
        counter1 = Counter(temp)
        counter2 = Counter(s)
        result_counter = counter1 + counter2
        for key, value in result_counter.items():
            if value >1:
                return False
        return True

    def dfs(self, i, arr, string, n):
        include = 0
        exclude = 0

        if i >= n:
            return len(string)
        
        print(string)
        if self.checkunique(string, arr[i]):
            include = self.dfs(i+1, arr, string+arr[i], n)
            exclude = self.dfs(i+1, arr, string, n)
        else:
            exclude = self.dfs(i+1, arr, string, n)
        
        return max(include, exclude)

    def maxLength(self, arr: List[str]) -> int:
        temp = ''
        n = len(arr)
        i = 0

        return self.dfs(i , arr, temp, n)
                