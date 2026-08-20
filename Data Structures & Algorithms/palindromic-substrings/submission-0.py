class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            lb = i - 1
            ub = i + 1
            ans += 1
            while lb >= 0 and ub < n and s[lb] == s[ub]:
                lb -= 1
                ub += 1
                ans += 1
        for i in range(1, 2 * n - 1, 2):
            lb = (i - 1) // 2
            ub = (i + 1) // 2
            while lb >= 0 and ub < n and s[lb] == s[ub]:
                lb -= 1
                ub += 1
                ans += 1
        return ans
