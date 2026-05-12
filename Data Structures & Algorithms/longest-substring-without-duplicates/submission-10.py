class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        l = 0
        r = 0
        count = 0
        maxCount = 0
        # if(len(s) == 0):
        #     return 0
        # if(len(s) == 1):
        #     return 1
        while r < len(s):
            if s[r] not in mySet:
                mySet.add(s[r])
                count+=1
                r+=1
                print("count: ",count)
                maxCount = max(maxCount, count)
            else:
                maxCount = max(maxCount, count)
                count = 0
                l+=1
                r = l
                mySet.clear()
        return maxCount