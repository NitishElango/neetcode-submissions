class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        smallest = float('inf')
        while l < r:
            m = (l+r)//2
            smallest = min(smallest, nums[m])
            if nums[m] < nums[r]:
                r = m
            elif nums[m] > nums[r]:
                l = m + 1
        return nums[l]