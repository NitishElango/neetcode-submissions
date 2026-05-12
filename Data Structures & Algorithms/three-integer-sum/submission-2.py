class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = set()
        for i in range(len(nums)):
            target = -nums[i]
            l,r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    r-=1
                elif nums[l] + nums[r] < target:
                    l+=1
                else:
                    sol.add((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1
                print(sol)
        return list(sol)