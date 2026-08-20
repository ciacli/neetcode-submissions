class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * m for _ in range(n)]
        for i, c1 in enumerate(text1):
            for j, c2 in enumerate(text2):
                if c1 == c2:
                    rest = dp[i - 1][j - 1] if i >= 1 and j >= 1 else 0
                    dp[i][j] = 1 + rest
                else:
                    first = dp[i][j - 1] if j >= 1 else 0
                    second = dp[i - 1][j] if i >= 1 else 0
                    dp[i][j] = max(first, second)

        return dp[n - 1][m - 1]