class Solution:
    def trap(self, height: List[int]) -> int:
        maxl, maxr = [0] * len(height), [0] * len(height)
        for i in range(1, len(height)):
            maxl[i] = max(maxl[i-1], height[i-1])
        for i in range(len(height)-2,-1,-1):
            maxr[i] = max(maxr[i+1], height[i+1])
        
        water = 0
        for i in range(len(height)):
            water += max(min(maxl[i], maxr[i]) - height[i], 0)
        return water
            