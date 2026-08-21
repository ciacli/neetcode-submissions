class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        carry = 0
        ans = 0
        order = 1
        b = 0
        for c in num2:
            b = b * 10 + (ord(c) - ord('0'))

        for x in num1[::-1]:
            a = ord(x) - ord('0')
            p = a * b * order
            ans += p
            order *= 10
        return str(ans)
        