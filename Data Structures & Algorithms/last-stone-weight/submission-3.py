import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            p1, p2 = -heapq.heappop(stones), -heapq.heappop(stones)
            print(p1,p2)
            p1-=p2
            p1 = max(p1,0)
            p1*=-1
            print(p1)
            heapq.heappush(stones,p1)
            print(stones)
        return abs(stones[0])