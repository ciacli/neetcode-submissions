class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals = sorted(intervals, key = lambda t: t[1])
        last = 0
        ans = 0
        for i in range(1, n):
            if intervals[last][1] > intervals[i][0]:
                ans += 1
            else:
                last = i
        return ans
