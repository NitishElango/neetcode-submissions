class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1 for _ in range(m)] for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                d,r = 0,0
                if j + 1 < m:
                    r = max(r, grid[i][j+1])
                if i + 1 < n:
                    d = max(d, grid[i+1][j])
                if r == 0 and d == 0:
                    grid[i][j] = 1
                else:
                    grid[i][j] = r + d
        return grid[0][0]
