class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin,len(dp)):
                if i == coin:
                    dp[i] = 1
                else:
                    if i % coin == 0:
                        dp[i] = min(dp[i], i // coin)
                    else:
                        for c in coins:
                            if i - c < amount and i - c >= 0:
                                dp[i] = min(dp[i-c]+1, dp[i])
        return dp[-1] if dp[-1] != float('inf') else -1
                