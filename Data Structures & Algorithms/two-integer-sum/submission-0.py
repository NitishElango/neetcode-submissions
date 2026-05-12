class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #load in values from the list into hashmap for efficient lookup
        #use a for loop to iterate through the values of the list O(n)
        #subtract target and see if new target value already exists in hashmap
          #if so return the indices as a list, if not continue
        hashmap = {}
        for i, val in enumerate(nums):
            temp = target - val
            if temp in hashmap:
                return[hashmap[temp],i]
            hashmap[val] = i
        return []
            

        