class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        cols = len(matrix)
        rows = len(matrix[0])

        dp = [[0 for i in range(cols)] for i in range(rows)]

        for i in range(cols):
            dp[rows-1][i] = matrix[rows-1][i]

        for r in range(rows - 2, -1, -1):
            for c in range(0,cols, 1):
                x = min(dp[r+1][c-1 if c!=0 else c ], dp[r+1][c], dp[r+1][c+1 if c!=cols-1 else c])
                dp[r][c] = x + matrix[r][c]       
        
        mini = 999999
        for i in range(len(dp)):
            mini = min(mini, dp[0][i])

        return mini
        