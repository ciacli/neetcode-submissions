class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        ans = []
        while i < n and intervals[i][0] < newInterval[0]:
            i += 1
        intervals.insert(i, newInterval)
        i = 1
        ans.append(intervals[0])
        while i <= n:
            if ans[-1][1] >= intervals[i][0]:
                ans[-1][1] =  max(ans[-1][1], intervals[i][1])
            else:    
                ans.append(intervals[i])
            i += 1
        return ans