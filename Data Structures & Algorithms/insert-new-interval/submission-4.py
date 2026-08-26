class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        ans = []
        i = 0
        inserted = False
        while i < n:
            if intervals[i][0] >= newInterval[0] and not inserted:
                next = newInterval[:]
                inserted = True
            else:
                next = intervals[i][:]
                i += 1

            if ans and ans[-1][1] >= next[0]:
                ans[-1][1] =  max(ans[-1][1], next[1])
            else:    
                ans.append(next)
        if not inserted:
            if ans and ans[-1][1] >= newInterval[0]:
                ans[-1][1] =  max(ans[-1][1], newInterval[1])
            else:    
                ans.append(newInterval)
        return ans