class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = set()
        def backtrack(row, col, ind):
            if ind == len(word):
                return True

            if (row < 0 or row >= len(board) or 
                col < 0 or col >= len(board[0]) or
                (row, col) in visited or
                board[row][col] != word[ind]
            ): return False

            visited.add((row, col))
            res = (
                backtrack(row, col + 1, ind + 1) or
                backtrack(row + 1, col, ind + 1) or
                backtrack(row - 1, col, ind + 1) or
                backtrack(row, col - 1, ind + 1)
            )
            visited.remove((row, col))
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, 0):
                    return True
        
        return False
        
        



        
        