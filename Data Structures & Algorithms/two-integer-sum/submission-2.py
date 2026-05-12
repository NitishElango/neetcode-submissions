class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = dict()
        for i in range(len(nums)):
            number = nums[i]
            comp = target - number
            if comp in hashm:
                return [hashm[comp], i]
            else:
                hashm[number] = i
                
