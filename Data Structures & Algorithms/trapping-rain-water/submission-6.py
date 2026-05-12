class Solution:
    def trap(self, height: List[int]) -> int:
        premax, postmax = [0 for i in height], [0 for i in height]
        for i in range(1,len(height)):
            premax[i] = max(height[i-1], premax[i-1])
        for i in range(len(height)-2,-1,-1):
            postmax[i] =  max(height[i+1], postmax[i+1])
        total = 0
        for i in range(len(height)):
            total_water = min(postmax[i], premax[i]) - height[i]
            total += max(0, total_water)
        return total

