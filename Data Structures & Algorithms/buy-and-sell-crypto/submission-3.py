class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit_max = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit_max = max(prices[r] - prices[l], profit_max)
                r+=1
            else:
                l = r
                r += 1
        return profit_max
            