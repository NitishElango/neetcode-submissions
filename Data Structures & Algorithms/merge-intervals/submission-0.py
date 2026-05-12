class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return intervals
        intervals.sort()
        results = [intervals[0]]
        for i in range(1, len(intervals)):
            s = max(intervals[i][0], results[-1][0])
            e = min(intervals[i][1], results[-1][1])
            if e - s >= 0:
                results[-1] = [min(intervals[i][0], results[-1][0]),max(intervals[i][1], results[-1][1])]
            else:
                results.append(intervals[i])
        return results