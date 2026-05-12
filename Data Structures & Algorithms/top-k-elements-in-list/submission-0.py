class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        for n, c in count.items():
            freq[c].append(n)
        
        for i in range(len(freq)-1, -1, -1):
            if len(freq[i]) != 0:
                for num in freq[i]:
                    res.append(num)
            if len(res) == k:
                return res

            