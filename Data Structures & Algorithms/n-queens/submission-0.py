class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        result = []
        board  = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n):
                if self.is_valid(r, c, board):
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "."
        backtrack(0)
        return result        

    def is_valid(self, row, col, board) -> bool:
        
        r = row - 1
        while r >= 0:
            if board[r][col] == "Q":
                return False
            r -= 1
        
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        
        r, c = row - 1, col + 1
        while r >= 0 and c < len(board):
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1
        
        return True
        
        