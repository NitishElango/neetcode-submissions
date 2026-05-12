"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        s_list = sorted(intervals, key=lambda Interval:Interval.end)
        for i in range(len(s_list) - 1):
            curr_end = s_list[i].end
            next_start = s_list[i+1].start
            if curr_end > next_start:
                return False
        return True