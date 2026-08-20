class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        ans = 0
        balance = [[0] * 2 for _ in range(n)] # 1 == has stock to sell
        balance[0][1] = -prices[0]
        balance[0][0] = 0
        for i in range(1, n):
            tmp = balance[i - 2][0] if i > 1 else 0
            balance[i][0] = max(balance[i - 1][0], 
                balance[i - 1][1] + prices[i]) #he had it last round but sold it now
            balance[i][1] = max(balance[i - 1][1],
                 tmp - prices[i]) #he did not have before and bought it now, this is why it could not have bought it last round(against the rules)
        print(balance)
        return balance[n - 1][0]

