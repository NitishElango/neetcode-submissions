class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(r):
            count = 0
            for p in piles:
                count += math.ceil(p/r)
            return count
        
        l,r = 1, max(piles)
        ans = -1
        while l <= r:
            mid = (l+r)//2
            if hours(mid) <= h:
                r = mid - 1
                ans = mid
            elif hours(mid) > h:
                l = mid + 1
        return ans
        
