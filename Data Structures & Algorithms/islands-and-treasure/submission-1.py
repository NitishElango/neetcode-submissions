class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append([i,j])
        level = 0
        visited = set()
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == -1 or (i,j) in visited:
                    continue
                else:
                    visited.add((i,j))
                    grid[i][j] = level
                    q.append([i+1,j])
                    q.append([i-1,j])
                    q.append([i,j+1])
                    q.append([i,j-1])
            level +=1
