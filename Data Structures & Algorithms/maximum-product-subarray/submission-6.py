class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        g_sum = nums[0]
        mins, maxs = nums[0], nums[0]
        r = 1
        while r < len(nums):
            mins, maxs = min(nums[r], nums[r] * mins, nums[r] * maxs), max(nums[r], nums[r] * maxs, nums[r] * mins)
            g_sum = max(g_sum, maxs)
            r+=1
        return g_sum