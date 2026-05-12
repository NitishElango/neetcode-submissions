class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []

        def dfs(i):
            if i < len(nums):
                subsets.append(nums[i])
                dfs(i+1)
                subsets.pop()
                dfs(i+1)
            elif i >= len(nums):
                res.append(subsets[:])
        dfs(0)
        return res