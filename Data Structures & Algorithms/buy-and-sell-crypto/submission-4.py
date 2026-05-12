class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[r] - prices[l] > 0:
                max_profit = max(prices[r] - prices[l], max_profit)
                r+=1
            else:
                l = r
                r+=1
        return max_profit

            