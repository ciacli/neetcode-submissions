"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key = lambda i: i.start)
        for i in range(1, len(intervals)):
            start1, end1 = intervals[i - 1].start, intervals[i - 1].end
            start2, end2 = intervals[i].start, intervals[i].end
            if start2 < end1:
                return False
        return True