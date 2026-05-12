class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.nums = [-i for i in nums]
        self.k = k
        heapq.heapify(self.nums)
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        popped = []
        for _ in range(self.k):
            pop = heapq.heappop(self.nums)
            popped.append(pop)
        for i in range(len(popped)):
            heapq.heappush(self.nums,popped[i])
        return -pop
        
