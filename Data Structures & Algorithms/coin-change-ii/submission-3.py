class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * n for _ in range(amount + 1)]
        dp[0] = [1] * n
        for i in range(1, amount + 1):
            for idx, coin in enumerate(coins):
                dp[i][idx] += dp[i][idx - 1] if idx > 0 else 0
                if coin <= i:
                    dp[i][idx] += dp[i - coin][idx]
        return dp[amount][n - 1]