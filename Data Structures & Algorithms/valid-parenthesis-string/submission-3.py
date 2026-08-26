class Solution:
    def checkValidString(self, s: str) -> bool:
        lo, hi = 0, 0
        for c in s:
            if hi < 0:
                return False

            if c == '(':
                lo += 1
                hi += 1

            elif c == ')':
                lo = max(lo - 1, 0)
                hi -= 1
            else:
                lo = max(lo - 1, 0)
                hi += 1
        return lo == 0