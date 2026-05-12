class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque([])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        out = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    q.append((i,j))
                    while q:
                        n = len(q)
                        for _ in range(n):
                            p = q.popleft()
                            i, j = p
                            for inc in directions:
                                if i + inc[0] >= 0 and i + inc[0] < len(grid) and j + inc[1] >= 0 and j + inc[1] < len(grid[0]):
                                    if grid[i + inc[0]][j + inc[1]] == "1":
                                        q.append((i+inc[0], j + inc[1]))
                                        grid[i + inc[0]][j + inc[1]] = "0"
                    out +=1
        return out
        