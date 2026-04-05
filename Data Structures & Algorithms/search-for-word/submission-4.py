class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M , N = len(board), len(board[0])

        def backtrack(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= M or j < 0 or j >= N or word[k]!= board[i][j]:
                return False
            temp = board[i][j]
            board[i][j] = "#"
            if (backtrack(i, j+1, k+1) or
                backtrack(i, j-1, k+1) or
                backtrack(i+1, j, k+1) or
                backtrack(i-1, j, k+1)):
                return True    
            board[i][j] = temp
            return False

        for i in range(M):
            for j in range(N):
                if board[i][j] == word[0]:
                    out = backtrack(i, j, 0)
                    if out:
                        return True
        return False
