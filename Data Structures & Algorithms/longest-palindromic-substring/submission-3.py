class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        ans = ""
        for i in range(1, (2 * n) - 1, 2):
            lb  = (i - 1) // 2
            ub = (i + 1) // 2
            cnt = 0
            while lb >= 0 and ub < n and (s[lb] == s[ub]):
                cnt += 2
                lb -= 1
                ub += 1
            if cnt > len(ans):
                ans = s[lb + 1 : ub]
        for i in range(n):
            lb = i - 1
            ub = i + 1
            cnt = 1
            while lb >= 0 and ub < n and (s[lb] == s[ub]):
                cnt += 2
                lb -= 1
                ub += 1
            if cnt > len(ans):
                ans = s[lb + 1 : ub]

        return ans