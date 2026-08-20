class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        def sumofsquares(n):
            ans = 0
            while n:
                ans += (n % 10) ** 2
                n = n // 10
            return ans
        while n != 1 and (n not in d):
            d[n] = 1
            n = sumofsquares(n)
        return n == 1

        