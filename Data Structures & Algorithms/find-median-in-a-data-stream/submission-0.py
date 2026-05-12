class MedianFinder:

    def __init__(self):
        self.min_heap, self.max_heap = [], []

    def addNum(self, num: int) -> None:
        if not self.min_heap and not self.max_heap:
            heapq.heappush(self.min_heap, num)
        elif self.min_heap and self.max_heap:
            if num >= self.min_heap[0]:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
        elif self.min_heap:
            if num >= self.min_heap[0]:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)


        if len(self.min_heap) > len(self.max_heap) + 1:
            pop = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -pop)
        elif len(self.max_heap) > len(self.min_heap) + 1:
            pop = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -pop)

    def findMedian(self) -> float:
        print(self.min_heap)
        print(self.max_heap)
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        elif len(self.max_heap) < len(self.min_heap):
            return self.min_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0])/2
        
        