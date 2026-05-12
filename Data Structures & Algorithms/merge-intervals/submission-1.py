class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if len(intervals) == 0:
            return []
        stack = [intervals[0]]
        for i in range(1,len(intervals)):
            cs, ce = intervals[i][0], intervals[i][1]
            ps, pe = stack[-1][0], stack[-1][1]
            if pe < cs:
                stack.append(intervals[i])
            else:
                stack.pop()
                ns, ne = min(cs, ps), max(pe, ce)
                stack.append([ns, ne])
        return stack