class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        board = [["."] * n for _ in range(n)]
        cols = set()
        diag1 = set()      # row + col
        diag2 = set()      # row - col

        def dfs(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue

                # Place queen
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)

                dfs(row + 1)

                # Backtrack
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)

        dfs(0)
        return res



        res = []
        def placeNQueens(row, queens):
            if row == n:
                res.append(queens)
                return
            valid_col = []

            for col in range(n):
                valid = True
                for (row_q, col_q) in queens:
                    if row + col == row_q + col_q or row - col == row_q - col_q or col == col_q:
                        valid = False
                        break
                if valid:
                    valid_col.append(col)
                    
            for col in valid_col:
                placeNQueens(row + 1, queens + [(row, col)])
            return            

        placeNQueens(0, [])

        boards = []  
        for queens in res:
            board = [["."] * n for _ in range(n)]
            for (row,col) in queens:
                board[row][col] = "Q"
            board = ["".join(r) for r in board]
            boards.append(board)

        return boards