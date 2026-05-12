class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        list_nums = []
        for key, val in freq_dict.items():
            list_nums.append((-val, key))
        heapq.heapify(list_nums)
        sol = []
        for i in range(k):
            sol.append(heapq.heappop(list_nums)[1])
        return sol

    
        
        
        