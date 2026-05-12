class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # add all rotten oranges to a queue and then ->
        # perform a bfs on the rotten orange and add infectd oranges to a queue
        # for each level traversed increase the minute counter by 1
        # at the end we can iterate through the whole grid to check for any fresh oranges
            # if there are any fresh oranges return -1 , else return minutes

        q = []
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh +=1
        minutes = 0
        while q and fresh > 0:
            n = len(q)
            for _ in range(n):
                orange = q.pop(0)
                i, j = orange
                if i + 1 < len(grid):
                    if grid[i+1][j] == 1:
                        grid[i+1][j] = 2
                        fresh-=1
                        q.append((i+1, j))
                if i - 1 >= 0:
                    if grid[i-1][j] == 1:
                        grid[i-1][j] = 2
                        fresh-=1
                        q.append((i-1, j))
                if j + 1 < len(grid[0]):
                    if grid[i][j+1] == 1:
                        grid[i][j+1] = 2
                        fresh-=1
                        q.append((i, j+1))
                if j - 1 >= 0:
                    if grid[i][j-1] == 1:
                        grid[i][j-1] = 2
                        fresh-=1
                        q.append((i, j-1))
            if q:
                minutes += 1

        return minutes if fresh == 0 else -1
        

        
        