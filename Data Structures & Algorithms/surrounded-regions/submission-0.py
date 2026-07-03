class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows, cols = len(board), len(board[0])

        def dfs(r, c):

            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return

            board[r][c] = "#"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for row in range(rows):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][cols - 1] == "O":
                dfs(row, cols -1)
        for col in range(cols):
            if board[0][col] == "O":
                dfs(0, col)
            if board[rows - 1][col] == "O":
                dfs(rows - 1, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "#":
                    board[row][col] = "O"
        return

