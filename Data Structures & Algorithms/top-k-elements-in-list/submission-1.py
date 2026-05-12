class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        for key, val in count.items():
            res.append((val,key))
        heapq.heapify(res)
        
        final = heapq.nlargest(k, res)
        res = []
        for tup in final:
            res.append(tup[1])
        return res