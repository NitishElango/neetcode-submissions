class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsDict ={}
        i = 0
        for num in nums:
            if num in numsDict.keys():
                return True
            else:
                numsDict[num] = i
                i+=1
        return False



        
            
         