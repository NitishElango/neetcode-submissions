class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area = 0
        for i in range(len(heights)):
            if not stk:
                stk.append((heights[i], i))
            else:
                if stk[-1][0] > heights[i]:
                    while stk and stk[-1][0] > heights[i]:
                        val, ind = stk.pop()
                        area = (i - ind) * val
                        max_area = max(max_area, area)
                    stk.append((heights[i], ind))
                    print(stk)
                else:
                    stk.append((heights[i], i))
        if stk:
            while stk:
                val, ind = stk.pop()
                area = (len(heights) - ind) * val
                max_area = max(max_area, area)
        return max_area