class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        q = deque()
        visit = set()

        def addCell(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0 or (i,j) in visit:
                return
            grid[i][j] = 2
            q.append([i, j])
            visit.add((i, j))

        n_fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i,j])
                    visit.add((i,j))
                if grid[i][j] == 1:
                    n_fresh += 1
        if not n_fresh and not q:
            return 0 

        dist = 0
        while q:
            for k in range(len(q)):
                i, j = q.popleft()
                addCell(i + 1, j)
                addCell(i - 1, j)
                addCell(i, j + 1)
                addCell(i, j - 1)
            dist += 1
        dist -= 1 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return dist

    