class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        for j in range(len(queries)):
            num = queries[j]
            min_interval = float('inf')
            for interval in intervals:
                if num >= interval[0] and num <= interval[1]:
                    min_interval = min((interval[1] - interval[0] + 1), min_interval)
            if min_interval == float('inf'):
                queries[j] = -1
            else:
                queries[j] = min_interval
        return queries