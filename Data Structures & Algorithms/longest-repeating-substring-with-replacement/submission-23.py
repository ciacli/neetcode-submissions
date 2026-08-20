
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        lb = 0
        ub = 0
        best = 0
        d = {}
        while ub < len(s):
            d[s[ub]] = d.get(s[ub], 0) + 1
            best = max(best, d[s[ub]])
            if best < (ub - lb + 1) - k:
                if best == d[s[lb]]:
                    best -= 1
                    for v in d.values():
                        if v > best:
                            best = v
                d[s[lb]] -= 1
                lb += 1
            ans = max(ans, ub - lb + 1)
            ub += 1
        return ans
            

               
            
        