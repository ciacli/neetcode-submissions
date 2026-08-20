class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        ans = 0
        dp = {}
        def dfs(pos, mustBuy):
            nonlocal n
            if pos == 0:
               return -prices[0]

            if (pos, mustBuy) in dp:
                return dp[(pos, mustBuy)]

            if not mustBuy: #aka must_sell
                tmp = prices[pos] + dfs(pos - 1, True) if pos >= 1 else 0
                dp[(pos, mustBuy)] =  max(dfs(pos - 1, False), tmp) 
                return dp[(pos, mustBuy)]
            if mustBuy:
                tmp = -prices[pos] + dfs(pos - 2, False) if pos >= 2 else -prices[pos]
                dp[(pos, mustBuy)] = max(dfs(pos - 1, True), tmp) 
                return dp[(pos, mustBuy)]

        return max(dfs(n - 1, False), 0)
