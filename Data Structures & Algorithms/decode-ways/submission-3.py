class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0': return 0
        if n == 1: return 1
        ans = 0
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            cur = ord(s[i]) - ord('0')
            prev = ord(s[i - 1]) - ord('0')
            sm = prev * 10 + cur
            dp1 = dp[i - 1]
            dp2 = dp[i - 2] if i > 1 else 1
            if cur == 0:
                dp[i] = dp2 if (sm < 27 and prev != 0)  else 0
            else:
                dp[i] += dp1
                if prev != 0 and sm < 27:
                    dp[i] += dp2
        return dp[n - 1]
        