class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        
        for ind, val in enumerate(nums):
            if target - val in hashmap:
                return[hashmap[target - val], ind]
            else:
                hashmap[val] = ind

        return -1


            