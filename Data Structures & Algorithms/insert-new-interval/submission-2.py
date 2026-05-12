class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #insert 
        inserted = False
        for i in range(len(intervals)):
            s,e = intervals[i][0], intervals[i][1]
            if i == 0:
                if s >= newInterval[0]:
                    intervals.insert(0, newInterval)
                    inserted = True
                    break
            else:
                if s >= newInterval[0]:
                    intervals.insert(i, newInterval)
                    inserted = True
                    break
        if not inserted:
            intervals.append(newInterval)
            inserted = True
        
        #merge
        print(intervals)
        results = [intervals[0]]
        for i in range(1, len(intervals)):
            s = max(intervals[i][0], results[-1][0])
            e = min(intervals[i][1], results[-1][1])
            if e - s >= 0:
                results[-1] = [min(intervals[i][0], results[-1][0]),max(intervals[i][1], results[-1][1])]
            else:
                results.append(intervals[i])
        return results
