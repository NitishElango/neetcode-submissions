class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, subres = [], []

        def dfs(i, sumn):
            if i == len(nums) or sumn > target:
                return
            if sumn == target:
                res.append(subres[:]) 
                return
            else:
                subres.append(nums[i])
                dfs(i, sumn + nums[i])
                subres.pop()

                dfs(i + 1, sumn)


        dfs(0, 0)
        return res