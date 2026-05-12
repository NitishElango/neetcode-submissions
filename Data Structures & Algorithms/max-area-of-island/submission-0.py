class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        def dfs(i,j, count):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            else:
                grid[i][j] = 0
                count[0] +=1
                dfs(i +1 , j, count)
                dfs(i - 1, j, count)
                dfs(i , j+ 1, count)
                dfs(i, j - 1, count)
                return count

        

        maxArea = 0
        count = [0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j, count)
                    maxArea = max(maxArea, count[0])
                    count[0] = 0
        return maxArea