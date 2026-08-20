class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                left = dp[i][j - 1] if j >= 1 else 0
                up = dp[i - 1][j] if i >= 1 else 0
                dp[i][j] = left + up
        return dp[n - 1][m - 1]