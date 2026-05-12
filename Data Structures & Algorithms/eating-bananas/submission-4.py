class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def works(k):
            t = 0
            for p in piles:
                t+= math.ceil(p/k)
            return t <= h
        s, e = 1, max(piles)
        min_elem = e
        while s <= e:
            mid = (s + e)//2
            if works(mid):
                min_elem = mid
                e = mid - 1
            else:
                s = mid + 1
        return min_elem



