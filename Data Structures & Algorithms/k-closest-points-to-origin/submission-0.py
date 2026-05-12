import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for point in points:
            x,y = point
            dist = math.sqrt((x)**2 + (y)**2)
            point_dist = [dist, point]
            heapq.heappush(heap,point_dist)
        sol = []
        for i in range(k):
            pop = heapq.heappop(heap)
            sol.append(pop[1])
        return sol
