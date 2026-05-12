class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            else:
                grid[i][j] = 0
                u = dfs(i + 1, j)
                d = dfs(i - 1, j)
                l = dfs(i, j - 1)
                r = dfs(i, j + 1)
                return 1 + u + d + l + r
        maxc = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = dfs(i, j)
                    maxc = max(maxc, count)
        return maxc
