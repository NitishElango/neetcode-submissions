class Solution:
    def rob1(self, nums: List[int]) -> int:
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            return dp[-1]
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        num1 = nums[0:len(nums)-1]
        num2 = nums[1:len(nums)]
        return max(self.rob1(num1), self.rob1(num2))