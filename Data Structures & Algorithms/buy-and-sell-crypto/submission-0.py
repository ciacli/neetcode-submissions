class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lb = 0
        ub = 1
        ans = 0
        while lb < len(prices):
            if(ub == len(prices)): break
            best = 0
            while ub < len(prices) and prices[ub] > prices[lb]:
                best = max(best, prices[ub])
                ub += 1
            ans = max(best- prices[lb], ans)
            lb = ub
            ub += 1
        return ans


        