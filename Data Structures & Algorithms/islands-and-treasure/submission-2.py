class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m = len(grid)
        n = len(grid[0])
        q = deque()
        visit = set()
        
        def addCell(i, j ):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j] == -1 or (i,j) in visit: 
                return 
            visit.add((i, j))
            q.append([i, j])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visit.add((i, j))
        
        dist = 0
        while q:
            for k in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = dist
                addCell(i + 1, j)
                addCell(i - 1, j)
                addCell(i, j + 1)
                addCell(i, j - 1)
            dist += 1
                    
