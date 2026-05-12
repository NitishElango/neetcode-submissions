class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for ind, val in enumerate(nums):
            if target - val in seen:
                return [seen[target-val], ind]
            else:
                seen[val] = ind
        