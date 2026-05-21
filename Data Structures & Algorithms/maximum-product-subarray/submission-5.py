class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        g_sum = nums[0]
        mins, maxs, cur = nums[0], nums[0], 1
        r = 1
        while r < len(nums):
            cur = max(nums[r],  nums[r] * mins, nums[r] * maxs)
            mins = min(nums[r] * mins, nums[r], nums[r] * maxs)
            maxs = cur
            g_sum = max(g_sum, cur)
            r+=1
        return g_sum