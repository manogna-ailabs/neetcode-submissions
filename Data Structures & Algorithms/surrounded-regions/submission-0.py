class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != "O":
                return
            board[i][j] = "S"
            for (di, dj) in directions:
                dfs(i + di, j + dj)
            return

        for i in range(m):
            for j in [0, n-1]:
                if board[i][j] == "O":
                    dfs(i,j)
        
        for j in range(n):
            for i in [0, m-1]:
                if board[i][j] == "O":
                    dfs(i,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "S":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
