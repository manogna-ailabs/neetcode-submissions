class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j]==0:
                return 0
            grid[i][j] = 0
            area = 1 + dfs(i,j-1) + dfs(i,j+1) + dfs(i-1,j) + dfs(i+1,j)
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    area = dfs(i,j)
                    print(i,j, area)
                    res = max(res, area)
        return res