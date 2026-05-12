class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.nums = [-i for i in self.nums]
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        popped = []
        for i in range(self.k):
            pop = heapq.heappop(self.nums)
            popped.append(pop)
        for num in popped:
            heapq.heappush(self.nums, num)
        return -pop
        

        
