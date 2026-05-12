"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = []
        max_r = 0
        intervals.sort(key = lambda x:x.start)
        for i in range(len(intervals)):
            print(rooms)
            if len(rooms) == 0:
                heapq.heappush(rooms, intervals[i].end)
            else:
                if intervals[i].start >= rooms[0]:
                    heapq.heappushpop(rooms, intervals[i].end)
                else:
                    heapq.heappush(rooms, intervals[i].end)
            max_r = max(max_r, len(rooms))
        return max_r

            
