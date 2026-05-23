class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(ind, curr_sum):
            if ind >= n:
                return False
            elif curr_sum > sub_sum:
                return False
            elif curr_sum == sub_sum:
                return True
            else:
                return dfs(ind + 1, curr_sum + nums[ind]) or dfs(ind + 1, curr_sum)
        
        n = len(nums)
        tot_sum = sum(nums)
        if tot_sum % 2 != 0:
            return False
        else:
            sub_sum = tot_sum // 2
            return dfs(0, 0)

        