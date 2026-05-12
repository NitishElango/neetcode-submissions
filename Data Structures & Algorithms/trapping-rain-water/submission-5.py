class Solution:
    def trap(self, height: List[int]) -> int:
        # iterate until first number greater than 0
            # assign left pointer to this number and right pointer to next number
        # expand sliding window until right pointer >= left pointer
            # while expalnding track the total rain water by subtracitng current index value by left index value and add to temp

        # when right pointer >= left pointer
            # left = right, right +=1
            # total += temp
        # continue sliding window until right pointer >= left pointer or right pointer out of bounds

        ### solution ###
        
        premax, postmax = [0 for i in height], [0 for i in height]
        total = 0
        for i in range(1,len(height)):
            premax[i] = max(premax[i-1], height[i-1])
        for i in range(len(height) - 2, -1, -1):
            postmax[i] = max(postmax[i+1], height[i+1])
        for i in range(len(height)):
            total += max(min(premax[i], postmax[i]) - height[i], 0)
        return total
        

       
            
            