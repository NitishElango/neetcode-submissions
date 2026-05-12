class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])
        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            ps, pe = stack[-1]
            cs, ce = intervals[i]
            if pe >= cs:
                stack.pop()
                stack.append([min(ps, cs), max(pe, ce)])
            else:
                stack.append(intervals[i])
        return stack