class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
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