class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n + m != len(s3):
            return False
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            dp[i][0] = s1[ : i] == s3[ : i]
        for j in range(1, m + 1):
            dp[0][j] = s2[ : j] == s3[ : j]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i - 1][j]
                if s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i][j - 1]
                    
        return dp[n][m] == 1