class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        ans = []
        for i, c in enumerate(s):
            last[c] = i
        i = 0
        lb = 0
        ub = 0
        while i < len(s):
            ub = max(ub, last[s[i]])
            if i == ub:
                ans.append(ub - lb + 1)
                lb = i + 1
            i += 1

        return ans
         