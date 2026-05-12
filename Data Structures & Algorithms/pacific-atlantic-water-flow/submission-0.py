class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pcords = []
        acords = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0:
                    pcords.append((i,j))
                if j == 0:
                    pcords.append((i,j))
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == len(heights)-1:
                    acords.append((i,j))
                if j == len(heights[0]) - 1:
                    acords.append((i,j))
        print(set(pcords))
        print("-----")
        print(set(acords))
        #pacific ocean bfs
        pq = deque(pcords)
        pv = set(pcords)
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        while pq:
            for _ in range(len(pq)):
                i, j = pq.popleft()
                for r, c in dirs:
                    nr, nc = i + r , j + c
                    if nr >= 0 and nc >= 0 and nr < len(heights) and nc < len(heights[0]) and (nr, nc) not in pv:
                        if heights[nr][nc] >= heights[i][j]:
                            pq.append((nr, nc))
                            pv.add((nr, nc))
        aq = deque(acords)
        av = set(acords)
        while aq:
            for _ in range(len(aq)):
                i, j = aq.popleft()
                for r, c in dirs:
                    nr, nc = i + r, j + c
                    if nr >= 0 and nc >= 0 and nr < len(heights) and nc < len(heights[0]) and (nr, nc) not in av:
                        if heights[nr][nc] >= heights[i][j]:
                            aq.append((nr, nc))
                            av.add((nr, nc))
        sol = []
        for cord in av & pv:
            sol.append(cord)
        return [list(cord) for cord in av & pv]
                


