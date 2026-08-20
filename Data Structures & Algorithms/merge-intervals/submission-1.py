class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda t: t[0])
        ans = []
        i = 0
        while i < len(intervals):
            j = i + 1
            ub = intervals[i][1]
            while j < len(intervals) and intervals[j][0] <= ub:
                ub = max(ub, intervals[j][1])
                j += 1
            ans.append([intervals[i][0], ub])
            i = j

        return ans
