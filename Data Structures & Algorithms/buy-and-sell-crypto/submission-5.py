class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        l,r = 0, 1
        max_p = 0
        while r < len(prices):
            if prices[r] <= prices[l]:
                l = r 
                r+=1
            else:
                profit = prices[r] - prices[l]
                max_p = max(max_p, profit)
                r+=1
        return max_p
