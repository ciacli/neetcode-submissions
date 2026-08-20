class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i, c in enumerate(s):
            ub = i
            d = {}
            while ub < len(s) and d.get(s[ub], 0) == 0:
                d[s[ub]] = 1
                ub += 1
            ans = max(ans, ub - i)
        return ans
            
        