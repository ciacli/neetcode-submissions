class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        coins = sorted(coins, key = lambda value: -value)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                count = 1 + dp[i - coin] if coin <= i else -1
                if count > 0:
                    dp[i] = min(dp[i], count) if dp[i] != -1 else count
        return dp[amount]
                