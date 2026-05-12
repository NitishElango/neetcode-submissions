class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sub = [], []

        def dfs(i,sumn):
            if sumn == target:
                res.append(sub[:])
                return
            elif sumn > target or i == len(nums):
                return
            else:
                sub.append(nums[i])
                dfs(i, sumn + nums[i])
                sub.pop()
                dfs(i + 1, sumn)
        dfs(0,0)
        return res
