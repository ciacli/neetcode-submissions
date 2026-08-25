class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        ans = []
        for i, c in enumerate(s):
            last[c] = i
        lb = 0
        while lb < len(s):
            ub = last[s[lb]]
            i = lb
            while i < ub:
                i += 1
                ub = max(last[s[i]], ub)

            ans.append(ub - lb + 1)
            lb = ub + 1

        return ans
         