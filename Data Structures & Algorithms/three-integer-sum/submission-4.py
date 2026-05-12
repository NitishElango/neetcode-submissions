class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = set()
        for i in range(len(nums)):
            curr = nums[i]
            target = 0-curr
            l,r = i+1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    ans = [nums[i], nums[l], nums[r]]
                    ans = tuple(ans)
                    if ans not in sol:
                        sol.add(ans)
                    l+=1
                    r-=1
                elif nums[l] + nums[r] > target:
                    r-=1
                else:
                    l+=1
        return list(sol)

