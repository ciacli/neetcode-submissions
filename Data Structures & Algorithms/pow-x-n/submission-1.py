class Solution:
    def myPow(self, x: float, n: int) -> float:
        def expPow(x, n):
            if n == 0:
                return 1
            if n % 2 == 1:
                return x * expPow(x, n - 1)
            else:
                p = expPow(x, n // 2)
                return p * p

        return expPow(x, n) if n >= 0 else expPow(1 / x, abs(n))