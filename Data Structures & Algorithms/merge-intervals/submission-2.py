class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda t: t[0])
        ans = []
        i = 0
        while i < len(intervals):
            lb = intervals[i][0]
            ub = intervals[i][1]
            if ans and lb <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], ub)
            else:
                ans.append(intervals[i])
            i += 1

        return ans
