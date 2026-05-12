class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            new_ind = abs(nums[i])
            if nums[new_ind] < 0:
                return new_ind
            else:
                nums[new_ind] = -nums[new_ind]