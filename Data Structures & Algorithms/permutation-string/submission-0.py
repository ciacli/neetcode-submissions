class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = {}
        d2 = {}
        ans = False
        lb = 0
        for c in s1:
            d1[c] = d1.get(c, 0) + 1
        for ub in range(len(s2)):
            d2[s2[ub]] = d2.get(s2[ub], 0) + 1
            while lb < len(s2) and d2[s2[ub]] > d1.get(s2[ub], 0):
                d2[s2[lb]] -= 1
                lb += 1
            if ub - lb + 1 == len(s1):
                ans = True
        return ans
        