"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            s = max(result[-1].start, intervals[i].start)
            e = min(result[-1].end, intervals[i].end)
            if e - s > 0:
                return False
            else:
                result.append(intervals[i])
        return True
