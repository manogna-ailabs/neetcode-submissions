class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac = set()
        atl = set()

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(i, j, visited):
            visited.add((i, j))
            for (di, dj) in directions:
                ni, nj = i + di, j + dj 
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited and heights[ni][nj] >= heights[i][j]:
                    dfs(ni, nj, visited)
            return True

        for i in range(m):
            dfs(i, 0, pac)
            dfs(i, n-1, atl) 

        for j in range(n):
            dfs(0, j, pac)
            dfs(m-1, j, atl)

        out = []
        for (i, j) in pac:
            if (i, j) in atl:
                out.append([i, j])
        return out
