class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        MOD = 10**9 + 7
        dp = [[[0] * (maxMove+1) for _ in range(n)] for _ in range(m)]
        dp[startRow][startColumn][0] = 1
        count = 0

        for k in range(maxMove):
            for i in range(m):
                for j in range(n):
                    if dp[i][j][k] > 0:
                        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            ni, nj = i+di, j+dj
                            if 0 <= ni < m and 0 <= nj < n:
                                dp[ni][nj][k+1] = (dp[ni][nj][k+1] + dp[i][j][k]) % MOD
                            else:
                                count = (count + dp[i][j][k]) % MOD

        return count
        