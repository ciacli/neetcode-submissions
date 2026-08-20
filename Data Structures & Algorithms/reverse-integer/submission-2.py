class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        MAX = 2 ** 31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            digit = x % 10
            x = x // 10
             
            if (MAX - digit) / 10 < ans:
                return 0
            ans = ans * 10 + digit
        return ans * sign
        
            