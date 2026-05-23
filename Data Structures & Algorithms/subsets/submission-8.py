class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        n = len(nums)
        def dfs(ind, sub):
            if ind == n:
                res.append(sub)
            else:
                sub.append(nums[ind])
                dfs(ind+1,sub[:])
                sub.pop()
                dfs(ind + 1,sub[:])
        dfs(0, sub)
        return res