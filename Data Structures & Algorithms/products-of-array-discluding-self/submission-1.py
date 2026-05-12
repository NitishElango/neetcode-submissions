class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postnums, prenums = [1 for i in nums], [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            prenums[i] = nums[i-1] * prenums[i-1]

        for i in range(len(nums)-2, -1, -1):
            postnums[i] = postnums[i+1] * nums[i+1]
        
        res = []
        for i in range(len(postnums)):
            res.append(postnums[i] * prenums[i])
        return res