class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        have = {}
        lb = 0
        ans = ""
        important = 0
        bestsize = -1
        for c in t:
            need[c] = need.get(c, 0) + 1
        for ub in range(len(s)):
            have[s[ub]] = have.get(s[ub], 0) + 1
            if need.get(s[ub], 0) > 0 and have[s[ub]] <= need[s[ub]]:
                important += 1
            while lb <= ub and have[s[lb]] > need.get(s[lb], 0):
                have[s[lb]] -= 1
                lb += 1
            if important >= len(t) and (bestsize == -1 or (ub - lb + 1) < bestsize):
                bestsize = ub - lb + 1
                ans = s[lb:ub + 1]
        return ans