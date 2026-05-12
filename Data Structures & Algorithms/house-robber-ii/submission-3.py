class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            dp = [0 for _ in range(len(nums))]
            dp[0] = nums[0]
            for i in range(1,len(nums)):
                if i == 1:
                    dp[i] = max(dp[0], nums[i])
                else:
                    dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return dp[-1]
        
        if len(nums) == 0:
                return 0
        elif len(nums) == 1:
                return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))