class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        i = 0
        while i < len(s):
            c = s[i]
            ub = i
            lb = i
            remaining = k
            nexti = -1
            while ub < len(s) and (s[ub] == c or remaining > 0):
                if c != s[ub]:
                    if nexti == -1:
                        nexti = ub
                    remaining -= 1
                ub += 1
            ans = max(ub - i + min(remaining, i), ans)
            if nexti == -1:
                nexti = ub
            i = nexti
        return ans
            
        