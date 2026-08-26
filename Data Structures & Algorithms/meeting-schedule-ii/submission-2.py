"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key = lambda t: t.start)
        h = []
        heapq.heappush(h, intervals[0].end)
        for t in intervals[1:]:
            #print(len(h))
            #print(str(t.start) + ' ' + str(t.end))
            
            earliest = h[0]
            heapq.heappush(h, t.end)
            if t.start >= earliest:
                heapq.heappop(h)
        return len(h)
            