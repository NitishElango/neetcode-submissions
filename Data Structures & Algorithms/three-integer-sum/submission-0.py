class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = set()
        nums.sort()
        for i in range(len(nums)):
            num = nums[i]
            target = 0 - num
            l, r = i+1, len(nums) - 1
            temp =[]
            while l < r:
                if nums[l] + nums[r] == target:
                    temp.append([num, nums[l], nums[r]])
                    l+=1
                    r-=1
                elif nums[l] + nums[r] > target:
                    r-=1
                else:
                    l+=1
            if len(temp) > 0:
                for arr in temp:
                    sol.add(tuple(arr))
        return list(sol)