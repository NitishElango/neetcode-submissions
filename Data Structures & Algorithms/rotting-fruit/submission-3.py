class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                elif grid[i][j] == 1:
                    fresh +=1
        
        q = deque(rotten)
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        mins = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                    continue
                else:
                    if grid[i][j] == 1:
                        grid[i][j] = 0
                        fresh-=1
                    for r, c in direction:
                        q.append((i + r, j + c))
            print(fresh)
            if fresh!=0:
                mins+=1
        return mins if fresh == 0 else -1


