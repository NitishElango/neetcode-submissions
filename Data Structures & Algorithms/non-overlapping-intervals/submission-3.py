class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0

        intervals.sort(key = lambda x:x[0])
        stack = [intervals[0]]

        for i in range(1,len(intervals)):
            ps, pe = stack[-1]
            cs, ce = intervals[i]
            
            if pe > cs:
                if pe > ce:
                    stack.pop()
                    stack.append(intervals[i])
            else:
                stack.append(intervals[i])
        print(stack)
        return len(intervals) - len(stack)
