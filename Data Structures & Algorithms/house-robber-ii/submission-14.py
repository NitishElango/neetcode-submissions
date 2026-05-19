class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robs(numbers):
            dp = [0] * len(numbers)
            dp[0] = numbers[0]
            print(numbers)
            for i in range(1, len(numbers)):
                if i == 1:
                    dp[i] = max(numbers[i-1], numbers[i])
                else:
                    dp[i] = max(numbers[i] + dp[i-2], dp[i-1])
            print(dp)
            return dp[-1]
        if len(nums) == 1:
            return nums[0]
        nums1, nums2 = nums[1:], nums[0:len(nums)-1]
        print(nums1, nums2)
        return max(robs(nums1), robs(nums2))