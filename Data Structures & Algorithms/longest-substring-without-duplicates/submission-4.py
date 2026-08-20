class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        lb = 0
        d = {}
        for ub in range(len(s)):
            while lb < len(s) and d.get(s[ub], 0) > 0:
                d[s[lb]] = d.get(s[lb], 1) - 1
                lb += 1
            d[s[ub]] = d.get(s[ub], 0) + 1
            ans = max(ans, ub - lb + 1)
        return ans
            
