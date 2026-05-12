class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] # (dist, [x,y])
        for p in points:
            dist = math.sqrt((p[0]**2) + (p[1] **2))
            heapq.heappush(heap, [dist, [p[0], p[1]]])
        sol = []
        for _ in range(k):
            pop = heapq.heappop(heap)
            sol.append(pop[1])
        return sol

