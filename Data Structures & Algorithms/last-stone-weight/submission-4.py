class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            p1, p2 = -heapq.heappop(stones), -heapq.heappop(stones)
            if p1 >= p2:
                heapq.heappush(stones, -(p1-p2))
        return -stones[0]